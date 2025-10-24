# Environment Setup Plan — Key Vault & Application Insights

## Goals
- Keep secrets **out of source control**.
- Use **.env** only for local dev; move to **Azure Key Vault** and **App Settings** in cloud.
- Capture telemetry (latency, success rate, token usage) via **Application Insights** once the API is live.

---

## Local Development (now)
- Secrets live in **.env** (ignored by Git).
- Scripts load env vars via python-dotenv.
- Keys/connection strings are never committed.

**Required vars**
- \AZURE_OPENAI_ENDPOINT\, \AZURE_OPENAI_KEY\, \AZURE_OPENAI_DEPLOYMENT\
- \SQL_CONN_RO\
- \APPINSIGHTS_CONNECTION_STRING\ (optional during Phase A)

---

## Cloud Deployment (Phase C/D)
### Secrets
- Store secrets in **Azure Key Vault**.
- The compute (Azure Functions or Container Apps) will read secrets via:
  - **Managed Identity** ? Key Vault access policy (preferred), or
  - **App Settings** (less preferred; acceptable for dev).

**Planned Key Vault secrets**
- \openai-endpoint\
- \openai-key\
- \openai-deployment\
- \sql-conn-ro\
- (later) \slack-bot-token\, \slack-signing-secret\

### Telemetry
- Enable **Application Insights** on the API.
- Emit structured logs:
  - \	s\, \equestId\, \userHash\, \question\, \intent\, \params\, \durationMs\, \model\, \	okensPrompt\, \	okensCompletion\, \outcome\, \error\, \source\.

**Sampling**
- Start with 100% in dev; consider sampling in prod if volume grows.

---

## Provisioning Notes (to execute in Phase C)
> Record-only for now; do not run yet.

- Create Key Vault:
  - Name: \kv-salesai-dev\
  - Access: your user + API's managed identity (when created)
- Add secrets:
  - \openai-endpoint\, \openai-key\, \openai-deployment\, \sql-conn-ro\
- Grant **Get/List** on secrets to the API's **system-assigned managed identity**.
- Enable Application Insights (workspace-based) on the API.

---

## Security & Governance
- Rotate keys every 90 days (document calendar reminders).
- Restrict SQL to **read-only**; deny DML.
- No PII in logs; hash Slack user IDs; never store raw prompts with sensitive values.

---

## Acceptance for Phase A
- This plan is documented and checked into \/docs/ENVIRONMENT_SETUP.md\.
- Actual provisioning and wiring occur during **Phase C**.
