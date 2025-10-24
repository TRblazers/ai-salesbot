# Architecture (v1)

**Goal:** Natural-language ? intent/parameters ? safe SQL templates ? results in Slack.

**High-level flow**
User (Slack)
/salesbot ? Azure Function API (/ask)
/ask ? Azure OpenAI (intent + parameter extraction)
/ask ? Azure SQL (read-only views) ? results
/ask ? Slack response (formatted)
Telemetry ? App Insights / Log Analytics
Secrets ? Azure Key Vault

**Resources (dev)**
- Resource Group: rg-salesai-dev
- Azure OpenAI: <name>, region <region>, deployment: gpt-4o-salesai
- App Insights: appi-salesai-dev
- Key Vault: kv-salesai-dev
- Azure SQL: <server>/<db> (read-only account)
