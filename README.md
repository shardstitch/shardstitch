# ShardStitch

**3:47pm. Mid-refactor. "Rate limit reached."**

Your code is half-written. The session is blocked. The next AI needs to know what changed, why it changed, and where to continue.

ShardStitch builds a continuation packet from surviving project evidence: Git changes, files, dependency context, notes, and available local conversation history. Restart in the same tool or move to another with a clearer account of the unfinished work.

> 🚀 **[Launched on Product Hunt](https://www.producthunt.com/products/shardstitch)**

[Website](https://shardstitch.com/) · [VS Code](https://marketplace.visualstudio.com/items?itemName=shardstitch.shardstitch) · [npm](https://www.npmjs.com/package/shardstitch) · [PyPI](https://pypi.org/project/shardstitch/) · [Support](mailto:support@shardstitch.com)

## 📦 Install

Install the launcher through PyPI or npm:

```bash
pip install shardstitch
```

```bash
npm install -g shardstitch
```

Then install the application with your license key:

```bash
shardstitch install <your-license-key>
```

Run `shardstitch` to launch the local dashboard at <http://127.0.0.1:8765>.

## 🧩 What it does

1. **Inspects project state:** Git changes, files, recent commits, and available notes.
2. **Adds dependency context:** helps identify related files and the impact of unfinished changes.
3. **Uses available conversation history:** carries forward recorded decisions, constraints, and rejected approaches where capture is supported.
4. **Builds a continuation packet:** gives the next session a goal, supporting evidence, verification status, and a next action.
5. **Prepares the handoff:** through manual copy, supported instruction-file workflows, or MCP integrations.

Recovery depends on what was saved or captured. ShardStitch cannot recreate unsaved work or intent that was never recorded.

## 🗄️ Conversation recovery

Where supported and captured, local conversation history can help preserve the reasoning behind a change, including decisions, constraints, and approaches that failed.

A transcript is evidence to inspect, not proof that the repository still matches the conversation. Review the handoff against current files and checks before continuing.

Capture, resume, and recovery capabilities vary by tool. See the [supported-tools documentation](https://shardstitch.com/tools/) for the applicable workflow and limitations.

## 🔁 Restart or switch tools

A handoff can help you move to another coding tool or start a fresh session in the same one.

Try the tool's built-in recovery first when the original conversation is available. For Claude Code, that can include `--continue`, `--resume`, or context compaction. ShardStitch helps when you need to assemble surviving evidence or repeat the handoff process across tools.

[Read the recovery guide](https://shardstitch.com/guides/ai-coding-session-recovery/)

## 🤖 31 handoff targets

ShardStitch supports 31 handoff targets across native integrations and web-chat workflows.

A handoff target does not imply complete feature parity. Manual handoff, instruction-file pickup, MCP access, and conversation capture have different coverage.

| Workflow | What to expect |
|---|---|
| **Project scan** | Evidence from the local project and available Git state |
| **Manual handoff** | Review and copy a continuation packet into the destination tool |
| **Instruction-file handoff** | Supported tools can discover context through their project instruction files |
| **MCP integration** | Supported clients can discover and call exposed ShardStitch tools |
| **Conversation capture** | Availability depends on the tool, capture mechanism, and recorded history |

[Check individual tool support](https://shardstitch.com/tools/)

## ✅ Key capabilities

- **Continuation packets:** goals, changes, constraints, recorded decisions, and next actions
- **Conversation recap:** relevant intent and rejected approaches from available history
- **Dependency context:** relationships around the files involved in the task
- **Persistent project memory:** durable notes for future sessions
- **Trust labels:** distinguish verified state from inference
- **Local verification:** check surviving evidence before treating a handoff as current

## 🐾 Hivy

Hivy is ShardStitch's local verification engine. It helps surface drift and stale-path signals while verified context is rebuilt from current repository evidence.

## 🔒 Privacy

Normal recovery runs locally, with no ShardStitch telemetry. Installation requires downloading the application.

When you send a continuation packet to another AI service, that service's data policies apply. Review packets before sharing them, especially when a project contains credentials, private logs, or customer data.

[Privacy policy](https://shardstitch.com/privacy/)

## 🎨 Planned: ShardDesign

A visual editor for AI-built websites, letting you adjust copy, images, spacing, and layouts directly in your project files.

[Explore ShardDesign](https://shardstitch.com/design/)

## 🛡️ Planned: Guardrails MCP

A review workflow that helps AI coding tools examine website discovery, content quality, and technical search issues, then propose evidence-backed repairs.

**ShardDesign and Guardrails MCP are in planning and development, not publicly available yet.** Guardrails is a review workflow with no promise of rankings or traffic recovery.

## ♾️ Pricing

One-time purchase with no subscription. See the website for current pricing and license terms.

[Get ShardStitch](https://shardstitch.com/#pricing)

## 💬 Support

Contact [support@shardstitch.com](mailto:support@shardstitch.com).

For security reports, see [SECURITY.md](SECURITY.md).

---

🐾 *Harvey, our Chief Morale Officer, reviews all pull requests by sitting on the keyboard.*
