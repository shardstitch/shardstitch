#!/usr/bin/env python3
"""Stop hook — best-effort auto-checkpoint the session into the running ShardStitch
app so the handoff/bedrock is always fresh. 100% local. Silent + non-blocking: if
the app isn't running it exits 0 and never interrupts the session.
"""
import argparse
import json
import sys
import urllib.request


def _post(port: int, path: str, body: dict, timeout: float = 3.0) -> bool:
    try:
        req = urllib.request.Request(
            f"http://127.0.0.1:{port}{path}",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(req, timeout=timeout)  # noqa: S310 (localhost only)
        return True
    except Exception:
        return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="")
    args, _ = ap.parse_known_args()
    body = {"projectPath": args.project, "trigger": "session-stop"}
    # Try the ShardStitch app on its known local ports; first success wins.
    for port in (8765, 8766, 8767, 8768):
        if _post(port, "/api/autosave", body) or _post(port, "/api/checkpoint", body):
            break
    sys.exit(0)  # always succeed — a stop hook must never block the session


if __name__ == "__main__":
    main()
