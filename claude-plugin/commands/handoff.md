---
description: Build a ShardStitch handoff for the current project, ready to paste into the next AI tool.
---
Use the `shardstitch_handover` MCP tool for the current project directory to
generate a continuation prompt (git diff, changed files, dependency / blast-radius
graph, verified project memory, and what to do next). If I named a target tool in
"$ARGUMENTS", pass it as the target so the format is tuned for that tool. Then show
me the handoff and confirm it's ready to paste into whatever I'm switching to.
