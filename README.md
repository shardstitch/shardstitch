# ShardStitch

**3:47pm. Mid-refactor. "Rate limit reached."**

Your code is half-written. Your plan is in your head. ShardStitch captures your entire session — git diff, changed files, dependency graph, intent — and stitches it into the next AI tool. One hotkey. Keep building like nothing happened.

[Website](https://shardstitch.com) · [VS Code](https://marketplace.visualstudio.com/items?itemName=shardstitch.shardstitch) · [npm](https://www.npmjs.com/package/shardstitch) · [PyPI](https://pypi.org/project/shardstitch/) · [Support](mailto:support@shardstitch.com)

## Install

```bash
# One-line installer (pip → npm → binary fallback)
curl -sL https://shardstitch.com/install.sh | bash

# Or install directly
pip install shardstitch
npm install -g shardstitch

# Run without installing
npx shardstitch
```

## What it does

When Claude, Cursor, Codex, or Gemini locks you out mid-session, ShardStitch:

1. **Scans your project** — git diff, changed files, recent commits, your notes
2. **Builds a dependency graph** — impact radius, architecture communities — and warns the next AI what's dangerous to touch
3. **Generates a continuation prompt** formatted for the target tool
4. **Injects it** into the tool's pickup file (CLAUDE.md, AGENTS.md, GEMINI.md, .cursorrules) for automatic discovery

Under 30 seconds, end to end.

## Not just for switching tools

The same trick fixes a bloated session in the *same* tool. Long AI chats accumulate a huge context tree — token burn climbs, responses slow down, and eventually you hit "Service is busy" even with quota left.

ShardStitch is the clean-restart button: extract a compact context, open a fresh window of the same tool, paste, keep going. Same model, fraction of the tokens, none of the drag.

## 22 supported AI tools

Claude Code, Claude Desktop, Cursor, Codex CLI, Gemini CLI, Windsurf, Aider, Kiro, Amazon Q Developer, DeepSeek, OpenCode, Trae, Factory Droid, OpenClaw, Amp, Cline, Roo Code, Kilo Code, Crush, Kimi, Qwen Code, and Antigravity.

## 7 surfaces

| Surface | Description |
|---------|-------------|
| **Web dashboard** | Scan, generate, copy, download |
| **VS Code / Cursor extension** | Alt+G hotkey |
| **MCP server** | 15 tools — Claude Code and Cursor call it directly |
| **CLI** | `pip install shardstitch && shardstitch` |
| **Desktop app** | Standalone Windows exe |
| **Autosave hooks** | Auto-inject on session end |
| **Local LLM failover** | Ollama, vLLM, LM Studio (zero cloud) |

## Key features

- **Per-agent formatting** — 22 format adapters, one for each tool
- **AI task router** — semantic matching picks the best tool for each task
- **Persistent memory** — project decisions survive across sessions and tools
- **Team coordination** — shared `.shardstitch/` directory for multi-dev handoffs
- **Tamper-evident audit trail** — hash-chained timeline logs
- **Dependency graph analysis** — impact radius, god nodes, architecture communities
- **Rate limit detection** — scans tool logs, suggests alternatives

## Honest comparison

| Capability | Free CLI scripts | Chat wrappers | ShardStitch |
|---|---|---|---|
| **Tools covered** | 1–2 narrow targets | Web chat UI only | **22 AI coding targets** |
| **Cross-tool handoff** | Partial or one-way | No codebase handoff | **Core workflow** |
| **Git awareness** | Usually none | None | **Auto diff, commits, worktree scan** |
| **Dependency graph** | None | Blind to codebase structure | **Impact radius and god-node detection** |
| **Rate-limit detection** | None | None | **Local log scanning and switch recommendation** |
| **File injection** | Manual files or clipboard | Clipboard only | **AGENTS.md, GEMINI.md, .cursorrules** |
| **Interface** | CLI | Web app | **Dashboard, Alt+G, VS Code extension, installer** |
| **Privacy / telemetry** | Local | Data routed to vendor cloud | **Air-gapped, local-only audit chain** |
| **Works while locked out** | Yes | Needs API/provider access | **No API needed — rebuilds from disk** |

## 100% local

Your code never leaves your machine. No cloud, no telemetry, no account required. No dependencies beyond Python stdlib. All processing happens on your hardware.

## Pricing

**Launch week: $19** (normally $49). One-time purchase, lifetime license, no subscription.

[Get ShardStitch →](https://shardstitch.com)

## Support

support@shardstitch.com — the founder personally answers every email within 24 hours.
