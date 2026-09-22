#!/usr/bin/env python3
"""ShardStitch MCP launcher (Claude Code plugin).

A Claude Code plugin can't bundle the full ShardStitch backend (it's a whole
Python app / packaged exe), so this thin launcher locates an ALREADY-INSTALLED
ShardStitch and execs its stdio MCP server, forwarding any args. The plugin is
the *doorway*; the backend is still the product.

IMPORTANT: a real `shardstitch install <key>` install is a COMPILED binary at
~/.shardstitch/app/ShardStitch(.exe) — not a loose mcp_server.py source file.
There is no mcp_server.py anywhere on a real customer's machine; the pip
package itself doesn't ship one either (it's just the download/launch
wrapper). The frozen exe has its own built-in `--mcp` stdio mode (see
app.py's `if "--mcp" in sys.argv` branch) — that is the real entry point.

Resolution order (first hit wins):
  1. $SHARDSTITCH_HOME/mcp_server.py          (dev/source-checkout override —
     only for someone running from a V-numbered dev folder, not a customer)
  2. the installed `shardstitch` pip package's own exe-finder
     (shardstitch._find_exe() — the SAME resolution logic `shardstitch
     install` and `shardstitch launch` already use, so this launcher can
     never drift out of sync with how the real app actually gets installed)
  3. common local install locations, exe form, as a last-resort fallback if
     the pip package itself isn't importable for some reason
If none is found it prints how to install ShardStitch and exits non-zero, so the
plugin fails loudly with a fix instead of silently doing nothing.
"""
import os
import subprocess
import sys
from pathlib import Path

_EXE_NAME = "ShardStitch.exe" if sys.platform == "win32" else "shardstitch"


def _source_override():
    """Dev-only: a source checkout with a real mcp_server.py file."""
    home = os.environ.get("SHARDSTITCH_HOME")
    if home:
        p = Path(home) / "mcp_server.py"
        if p.is_file():
            return ("source", p)
    return None


def _installed_exe():
    """The real, compiled app — same lookup the pip package itself uses."""
    try:
        import shardstitch  # type: ignore
        found = shardstitch._find_exe()  # noqa: SLF001 — intentional reuse
        if found:
            return ("exe", Path(found))
    except Exception:
        pass
    for p in (
        Path.home() / ".shardstitch" / "app" / _EXE_NAME,
        Path.home() / "ShardStitch" / _EXE_NAME,
    ):
        if p.is_file():
            return ("exe", p)
    return None


def main() -> None:
    for finder in (_source_override, _installed_exe):
        hit = finder()
        if not hit:
            continue
        kind, path = hit
        try:
            # subprocess.run (not os.execv) — execv mishandles argv on Windows
            # when a path contains a space (confirmed: silently truncates at
            # the first space, e.g. "V12 Development" -> "V12"), which would
            # break this launcher for any install path with a space in it,
            # including a Windows username like "John Doe". subprocess.run
            # quotes correctly on every platform and inherits stdio by
            # default, so the MCP stdio pipes still pass straight through.
            argv = ([sys.executable, str(path), *sys.argv[1:]] if kind == "source"
                    else [str(path), "--mcp", *sys.argv[1:]])
            sys.exit(subprocess.run(argv).returncode)
        except OSError:
            continue
    sys.stderr.write(
        "ShardStitch backend not found. Install it first:\n"
        "  shardstitch install <your-license-key>   (after pip install shardstitch\n"
        "  or npm i -g shardstitch)\n"
        "or set SHARDSTITCH_HOME to a source checkout containing mcp_server.py.\n"
        "The Claude Code plugin is only the integration layer — it needs the "
        "local ShardStitch app installed and activated to run.\n"
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
