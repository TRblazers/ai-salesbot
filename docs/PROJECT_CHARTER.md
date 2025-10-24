# Project Charter — AI Sales Q&A Bot (Phase A Closure)

## Purpose
Deliver a Slack-based assistant that answers natural-language questions about sales using safe, parameterized NL?SQL against read-only views in Azure SQL. Establish a reusable Azure OpenAI + API pattern for future datasets.

## Scope (v1)
- Natural-language queries mapped to **20–30 supported intents** (totals, trends, top-N, breakdowns, MoM/YoY).
- Parameter extraction (dates, product, channel, top-N).
- Clarifying question on ambiguity (single follow-up).
- Slack integration for internal users.
- Read-only SQL access via **contracted views** (no PII).

## Out of Scope (v1)
- Open-ended analytics / anomaly hunting.
- Arbitrary free-form SQL generation.
- Multi-turn conversational memory.
- Multi-dataset joins (single sales source only).
- Predictive modeling and dashboards.

## Stakeholders
- **Owner/Developer:** YOU (Data Engineering)
- **Sponsor:** Dept leadership
- **Optional reviewers:** IT/Infra (security, networking)

## Success Metrics (targets at launch)
- **Numeric accuracy:** = 90–95% on evaluation set
- **Intent recognition:** = 90% (in-scope)
- **Clarification rate:** = 30% of queries
- **Latency:** P50 = 3s; P95 = 6s
- **Uptime (API):** = 95% (dev/prod baseline)
- **User satisfaction (pilot):** = 75% “useful”

## Milestones & Dates (current plan)
- **Phase A — Foundations:** ? Complete (Nov 2025)
- **Phase B — Data Layer & Semantics:** Nov 17 – Dec 5
- **Phase C — API Skeleton:** Dec 8 – Dec 19
- **Phase D — NL?SQL Core (v1):** Jan 6 – Jan 31
- **Phase E — Slack Pilot:** Feb 3 – Feb 21
- **Phase F — Tuning & Eval (v1.1):** Feb 24 – Mar 14
- **Phase G — Launch:** Mar 17 – Mar 28
- **Phase H — Stabilize & Review:** Mar 31 – Apr 4

## Assumptions
- Solo developer with ad-hoc support; ~10 hrs/week average.
- Azure tenant access for OpenAI, SQL, Functions, Key Vault, App Insights.
- One flattened sales table as the source of truth.

## Risks (high-level)
- Ambiguous business definitions ? Mitigation: **Metric dictionary** and validation harness.
- Latency spikes (cold start) ? Mitigation: connection pooling, warm-up, prompt size.
- Scope creep ? Mitigation: enforce **intent catalog**; refuse out-of-scope politely.

## Deliverables (Phase A close-out)
- Architecture v1 diagram (Mermaid)
- Charter & metrics (this document)
- Environment setup plan (Key Vault / App Insights)
- Codegen policy (Codex usage boundaries)
