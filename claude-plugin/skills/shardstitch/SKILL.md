---
name: shardstitch
description: Session recovery and cross-tool handoff. Use when the session is bloated or rate-limited, when the user asks to hand off / switch tools / continue elsewhere, or to recall or save durable project memory. Auto-triggers on rate-limit signals ("limit reached", "try again later", "usage limit") and heavy-context slowdowns.
---

# ShardStitch — session recovery & handoff

ShardStitch keeps a durable, local, cross-tool memory of this project and can
package the whole session for the next AI tool. It runs 100% locally through the
bundled MCP server (tools prefixed `shardstitch_`). Nothing leaves the machine.

## When to use it
- **Rate-limited / "limit reached" / "try again later"** → capture the session now
  and build a handoff so no context is lost, then continue in another tool.
- **Context bloated / responses slowing** → extract a compact, verified context and
  suggest a fresh window (same tool) or a switch — same model, fraction of the tokens.
- **User asks to hand off, switch tools, or "continue elsewhere"** → build the
  handoff with `shardstitch_handover`.
- **Before a decision** → `shardstitch_memory_recall` to check prior decisions,
  rules, and gotchas. Act on ✅ verified freely; re-check ⚠️ stale first.
- **After a decision** → `shardstitch_memory_remember` to save it durably so the
  next session (in any tool) keeps it.

## How
1. `shardstitch_scan` — quick project state.
2. `shardstitch_handover` — a continuation prompt (git diff, changed files,
   blast-radius graph, verified memory, next steps). Pass a target tool if the user
   named one, so the format is tuned for it.
3. `shardstitch_memory_recall` / `shardstitch_memory_remember` — the durable
   memory loop; recall surfaces trust tags so you never act on a stale fact.

## Notes
- 100% local — no cloud, no account.
- This plugin is the Claude Code *doorway*; if a `shardstitch_*` tool is
  unavailable, the ShardStitch backend isn't running — tell the user to start it
  (`shardstitch`) or install it (`pip install shardstitch`).
