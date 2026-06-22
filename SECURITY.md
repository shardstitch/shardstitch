# Security Policy

## Reporting

Email **support@shardstitch.com** with security concerns. We aim to respond
within 72 hours. Please do not open public issues for undisclosed
vulnerabilities.

**Good-faith safe harbor:** we will not pursue or support legal action against
researchers who discover and report vulnerabilities in good faith, without
violating user privacy or disrupting service. Report it, give us reasonable time
to fix it, and we'll credit you if you'd like.

## Closed source, verifiable binaries

ShardStitch is closed-source. Its integrity does not depend on you reading the
code — it depends on checksum-verified binaries you can confirm before
anything runs. Every claim below is verifiable from the outside: inspect the
published packages, check the SHA-256 of any download, and watch the network
yourself.

## Verify it yourself

- **Checksum-verified install.** The installer verifies each downloaded binary's
  SHA-256 against the checksum the storefront publishes for that exact file —
  before it ever runs. A mismatch aborts the install. You can re-compute the
  SHA-256 of the installed binary yourself and confirm it matches.
- **Inspect the packages.** The `npm` and `pip` packages contain no install-time
  scripts. You can unpack and read them before installing.
- **Watch the traffic.** By default the only network calls are a one-time
  license check and the verified binary download. The sole opt-in exceptions —
  off unless you turn them on — are importing a `claude.ai/share/…` link you
  paste, and an optional cloud LLM backend you configure with your own API key.
  Point a network monitor at it and confirm nothing else leaves your machine.

## Design principles

- **Local by default.** Your code and conversations never leave your machine.
  Zero telemetry, no analytics, no update checks, no account. The only always-on
  outbound calls are a one-time license activation and the SHA-256-verified
  binary download. Two features reach the network **only when you explicitly opt
  in** — importing a `claude.ai/share/…` link you paste, and routing context
  through a cloud LLM provider you configure with your own API key — and both are
  off by default.
- **HTTPS + SHA-256 verified downloads.** The app binary is downloaded over
  HTTPS and its SHA-256 is verified before it can run. Mismatches abort the
  install.
- **No lifecycle scripts.** `npm install shardstitch` and `pip install
  shardstitch` execute no code on install. The binary is only downloaded when
  you explicitly run `shardstitch install <key>`.
- **Browser capture uses localhost-only standard protocols.** Conversation
  capture connects to the browser via the same standard automation interfaces
  used by Puppeteer, Playwright, and VS Code. The connection is bound to
  localhost (127.0.0.1), and the debug port is not opened to web origins — we do
  not pass `--remote-allow-origins`, so the browser's default blocks cross-origin
  DevTools connections. It is never exposed to the network.

## Note for automated scanners

ShardStitch legitimately launches local AI tools, reads their on-disk data for
conversation capture, and downloads a verified binary during install. All of
this is user-initiated, local-only, and integrity-verified.
