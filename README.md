# ShardStitch

**3:47pm. Mid-refactor. "Rate limit reached."**

Your code is half-written. Your plan is in your head. ShardStitch captures your entire session — git diff, changed files, dependency graph, *and the conversation itself* — and stitches it into the next AI tool. One hotkey. Keep building like nothing happened.

> 🚀 **Launching soon on Product Hunt.**

[Website](https://shardstitch.com) · [VS Code](https://marketplace.visualstudio.com/items?itemName=shardstitch.shardstitch) · [npm](https://www.npmjs.com/package/shardstitch) · [PyPI](https://pypi.org/project/shardstitch/) · [Support](mailto:support@shardstitch.com)

## Install

```bash
# Install from PyPI
pip install shardstitch

# …or via npm
npm install -g shardstitch

# Then download the app with your license key — verifies the binary's
# SHA-256 against Polar's checksum before it ever runs
shardstitch install <your-license-key>
```

Then run `shardstitch` to launch the dashboard at <http://127.0.0.1:8765>.

## What it does

When Claude, Cursor, Codex, or Gemini locks you out mid-session, ShardStitch:

1. **Scans your project** — git diff, changed files, recent commits, your notes
2. **Builds a dependency graph** — impact radius, god nodes, architecture communities — and warns the next AI what's dangerous to touch
3. **Recovers the conversation** — distills it into intent, decisions, rules, and what you already tried and rejected — *the "why" a repo scan can't reconstruct*
4. **Generates a continuation prompt** formatted for the target tool
5. **Injects it** into the tool's pickup file (CLAUDE.md, AGENTS.md, GEMINI.md, .cursorrules) for automatic discovery

Under 30 seconds, end to end. A normal scan completes in 1–4 seconds.

## Your conversation survives the crash

ShardStitch keeps an **always-on local vault** of every AI tool's transcript in `~/.shardstitch/session_vault/`. Default-on, content-addressed, zero cloud. So a rate-limit, a crash, or an accidental delete no longer loses your conversation — and it even restores a Claude Code session you deleted by mistake (delete-with-no-undo, undone).

That vault feeds **Conversation Recap**: every handoff carries not just *what* changed on disk, but the decisions and dead-ends behind it.

## Not just for switching tools

The same trick fixes a bloated session in the *same* tool. Long AI chats accumulate a huge context tree — token burn climbs, responses slow down, and eventually you hit "Service is busy" even with quota left.

ShardStitch is the clean-restart button: extract a compact context, open a fresh window of the same tool, paste, keep going. Same model, fraction of the tokens, none of the drag.

## 23 supported AI tools

Claude Code, Claude Desktop, Cursor, Codex CLI, Gemini CLI, Windsurf, Aider, Kiro, Amazon Q Developer, DeepSeek, OpenCode, Trae, Factory Droid, OpenClaw, Amp, Cline, Roo Code, Kilo Code, Crush, Qwen Code, Antigravity, ChatGPT, and Grok. Plus 4 browser-only chat surfaces (Perplexity, Claude.ai, Kimi, Gemini Web).

**Disk scan and manual copy/paste work for all 23** — they read your project, not the AI tool. The other features vary by tool:

| Capability | Coverage |
|---|---|
| **Disk scan** (git + files + graph) | All 23 tools |
| **Manual handoff** (copy/paste) | All 23 tools |
| **File injection** (auto-pickup) | Claude Code, Cursor, Codex, Gemini, Windsurf, Aider, Cline, Roo Code, Kilo Code, Trae, Kiro |
| **MCP** (16 tools, native call) | Claude Code, Cursor, Windsurf |
| **Recall** (live conversation capture) | **16 of 27 capture surfaces** verified, 5 partial/beta, 6 pending (see below) |

### Recall status — honest coverage

- **Verified end-to-end (13 tools + 3 browser surfaces):** Claude Code, Codex CLI, Gemini CLI, Aider, OpenCode, Qwen Code, Cursor, Cline, Antigravity, Claude Desktop, ChatGPT, Claude.ai, Gemini Web, DeepSeek, Kimi, Grok
- **Partial / beta:** Windsurf (needs Codeium login), Roo Code, Kilo Code (parser in progress), Trae, Kiro (CDP beta, untested)
- **Pending:** Amazon Q, Amp, Crush, Factory Droid, OpenClaw, Perplexity (no confirmed log or debug port yet)

Disk scan still gives every one of these a full project handoff regardless of Recall status.

## 7 surfaces

| Surface | Description |
|---|---|
| **Web dashboard** | Scan, generate, copy, download |
| **VS Code / Cursor extension** | Alt+G hotkey |
| **MCP server** | 16 tools — Claude Code and Cursor call it directly |
| **CLI** | `pip install shardstitch && shardstitch` |
| **Desktop app** | Standalone Windows exe |
| **Autosave hooks** | Auto-inject on session end + always-on vault |
| **Local LLM failover** | Ollama, vLLM, LM Studio (zero cloud) |

## Key features

- **Conversation Recap** — distills intent, decisions, rules, and tried-and-rejected paths into every handoff
- **Always-on session vault** — every transcript backed up locally; survives crashes, rate-limits, and misclick-deletes
- **Per-agent formatting** — 22 format adapters tuned to each tool's context style
- **Dependency graph analysis** — impact radius, god nodes, architecture communities
- **AI task router** — semantic matching picks the best tool for each task
- **Persistent memory** — project decisions survive across sessions and tools
- **Team coordination** — shared `.shardstitch/` directory for multi-dev handoffs
- **Hash-chained audit trail** — append-only SHA-256 timeline (tamper-detecting)
- **Rate-limit detection** — scans tool logs, suggests alternatives

## Honest comparison

| Capability | Free CLI scripts | Chat wrappers | ShardStitch |
|---|---|---|---|
| **Tools covered** | 1–2 narrow targets | Web chat UI only | **23 AI coding targets** |
| **Cross-tool handoff** | Partial or one-way | No codebase handoff | **Core workflow** |
| **Git awareness** | Usually none | None | **Auto diff, commits, worktree scan** |
| **Dependency graph** | None | Blind to codebase | **Impact radius + god-node detection** |
| **Conversation recovery** | None | None | **Vault + distilled recap** |
| **Rate-limit detection** | None | None | **Local log scanning + switch rec** |
| **Privacy / telemetry** | Local | Routed to vendor cloud | **Local-only, hash-chained audit** |
| **Works while locked out** | Limited | Needs API access | **No API needed — rebuilds from disk** |

## 100% local

Your code never leaves your machine. No cloud, no telemetry, no account required. No runtime dependencies beyond the Python standard library. Binaries are downloaded over HTTPS and SHA-256–verified before they run; npm and pip packages run no install-time scripts. All processing happens on your hardware.

## Pricing

**Launch week: $19** (normally $49). One-time purchase, lifetime license, no subscription.

[Get ShardStitch →](https://shardstitch.com)

## Support

<support@shardstitch.com> — the founder personally answers every email within 24 hours. Security reports: see [SECURITY.md](SECURITY.md).
