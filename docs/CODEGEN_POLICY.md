# Codegen Policy (Codex / Copilot-style tools)

## Purpose
Use AI code generation for **boilerplate and scaffolding**, not for data logic or security-critical code.

## Allowed (?)
- Project scaffolding (folders, configs, CI YAML)
- Azure Function/FastAPI boilerplate (HTTP triggers, routing)
- Typed DTOs / request/response models
- Logging wrappers, small utilities
- Test stubs and mocks
- Markdown/doc formatting

## Not Allowed (??)
- Business logic for metrics or transformations
- SQL generation against production data (templates only, hand-reviewed)
- Authentication/authorization logic
- Secrets handling (Key Vault integration code must be reviewed manually)
- Anything that weakens PII protection or governance

## Review Rules
- All AI-generated code must be **diff-reviewed** before merge.
- Add a PR note: “Contains AI-generated scaffolding only; no data logic.”
- Never paste secrets into prompts.
- If AI suggests SQL, convert to a **parameterized template** and validate manually.

## Attribution / Compliance
- Keep an audit trail: mention in PR description when AI tools were used.
- Maintain license headers on any copied snippets.

## Rationale
- Protects numeric accuracy and governance.
- Keeps security-sensitive paths human-authored.
- Speeds non-critical boilerplate without risking data integrity.
