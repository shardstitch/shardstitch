# ShardStitch — Claude Code plugin

The **Claude Code doorway** to ShardStitch: one install wires up session recovery,
verified project memory, and cross-tool handoff — without manually configuring an
MCP server or hooks.

> **This is the integration layer, not the product.** It requires the local
> ShardStitch backend (`pip install shardstitch`, `npm i -g shardstitch`, or the
> desktop app). The plugin just tells Claude Code how to talk to it. ShardStitch
> stays cross-tool — this is one polished doorway among many (Cursor, Codex,
> Gemini, etc. use the MCP server / file injection directly).

## What it bundles
| Component | What it does |
|---|---|
| **MCP server** | All ShardStitch tools (`shardstitch_handover`, `shardstitch_memory_recall`, …) — started via `mcp_launcher.py`, which locates your installed backend. |
| **Stop hook** | Auto-checkpoints the session into ShardStitch when Claude stops (best-effort, silent, local). |
| **`/shardstitch:handoff`** | Build a paste-ready continuation prompt for the next tool. |
| **`/shardstitch:recall`** | Recall verified project memory (with ✅/⚠️/❌ trust tags) before deciding. |
| **`/shardstitch:memory`** | List project memory with verification. |
| **Skill** | Auto-triggers on rate-limit signals / heavy context to offer capture + handoff. |

## Install

**From the marketplace (once published):**
```bash
claude plugin marketplace add github:shardstitch/shardstitch
claude plugin install shardstitch@shardstitch
```

**Local dev / testing (from this repo):**
```bash
claude --plugin-dir ./claude-plugin
# then in a session: /reload-plugins  and try  /shardstitch:handoff
claude plugin validate ./claude-plugin
```

## Requirements
- **ShardStitch backend installed** — `pip install shardstitch` (or the exe). The
  plugin's `mcp_launcher.py` resolves it via `$SHARDSTITCH_HOME`, the `shardstitch`
  Python package, or common install paths; if it can't find it, it prints how to
  install.
- Python 3 on PATH (to run the launcher + hook).

## Paths
`${CLAUDE_PLUGIN_ROOT}` is substituted to this plugin's install dir at runtime, so
the launcher/hook resolve regardless of where Claude Code caches the plugin.
