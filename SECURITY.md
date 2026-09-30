# Security Policy

## Reporting a Vulnerability

Email **support@shardstitch.com** with security concerns. We aim to provide an initial response within **72 hours**.

Please include the affected version, reproduction steps, potential impact, and any relevant logs with credentials and personal information removed. Do not open a public issue for an undisclosed vulnerability.

## Good-Faith Research

We welcome responsible security research. We will not pursue or support legal action against researchers conducting good-faith research within this policy, provided they:

- Test systems and installations they own or have permission to assess.
- Avoid accessing, retaining, or disclosing other people's private data.
- Avoid disrupting services or making destructive changes.
- Report findings privately and allow reasonable time for remediation.

We can credit researchers with their permission.

## Closed Source and Binary Integrity

ShardStitch is closed-source. Published packages, downloaded binaries, and observable network behavior can still be inspected.

A matching checksum confirms that a file matches the referenced download. It does not, by itself, establish that the software is secure or free from vulnerabilities.

## Verifying an Installation

- **Check the download:** compare the binary's SHA-256 with the checksum published for that exact release.
- **Inspect the launcher packages:** review the npm or PyPI package contents and installation configuration.
- **Observe network activity:** use a network monitor to examine your installed version during activation, recovery, conversation capture, and any optional integrations.
- **Report discrepancies:** contact us if observed behavior differs from the documented behavior for your version.

## Local Processing and Network Features

Normal project scanning and recovery are designed to run locally, with no ShardStitch telemetry.

Some operations require network access:

- Downloading the application binary.
- Validating a license with the applicable licensing provider.
- Importing a shared conversation link when requested.
- Using a cloud model provider that you explicitly configure.
- Sending a handoff to an external AI service.

Depending on the feature, these operations may transmit license information, request metadata, or selected content. External providers apply their own privacy and retention policies.

Review the settings and documentation for your installed version before enabling optional integrations. Remove secrets and sensitive information from handoffs before sharing them.

## Downloads and Package Installation

Application downloads should use HTTPS. The installer is intended to verify the downloaded binary against its published SHA-256 checksum and abort installation if verification fails.

The launcher packages and the application binary are separate components. Inspect the package for the version you intend to install rather than assuming identical behavior across releases.

## Browser Conversation Capture

Supported browser capture workflows may use local browser debugging or automation interfaces.

Keep debugging endpoints bound to loopback interfaces such as `127.0.0.1`. Do not expose them to your local network or the internet. Browser debugging access can expose sensitive session data, so enable it only for supported workflows and disable it when no longer needed.

A localhost connection alone does not guarantee protection from every process running on the same device.

## Guidance for Automated Scanners

Expected behavior may include reading local project files and supported conversation history, invoking configured local tools, and downloading an application binary during an explicitly requested installation.

These capabilities should be evaluated against the user's configuration and documented behavior. Unexpected outbound traffic, access to unrelated data, or failed integrity checks should be investigated and reported.

## Scope

This policy applies to ShardStitch. Planned ShardDesign and Guardrails MCP features are not publicly available and should not be treated as shipped security capabilities.
