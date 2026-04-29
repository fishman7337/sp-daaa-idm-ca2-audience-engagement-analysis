# Security Policy

## Supported Scope

This repository is a student analytics project. Security maintenance focuses on:

- Preventing accidental commits of credentials.
- Keeping local configuration out of version control.
- Checking Python dependencies for known vulnerabilities in CI.
- Avoiding unsafe file handling in reusable scripts.

## Reporting a Vulnerability

If you find a security issue, do not open a public issue containing sensitive details. Contact the project maintainers privately or use the relevant Singapore Polytechnic academic channel.

Please include:

- A short description of the issue.
- The affected file or workflow.
- Steps to reproduce, if safe to share.
- Suggested remediation, if known.

## Secrets and Environment Files

No real secrets are required for this project. Use `.env.example` only as a template. A real `.env` file should remain local and is ignored by git.
