# Metrics & Definitions (v1)

**Accuracy (numeric)** = correct answers / total (on evaluation set)
**Intent hit-rate** = % of in-scope questions mapped to a supported intent
**Latency** = P50/P95 time from API ingress to Slack response
**Token usage** = avg prompt + completion tokens per request
**Uptime** = Function availability (dev; later prod)
**User feedback** = % 'useful' responses

**Logging fields (planned)**
- ts, requestId, userHash, question, intent, params, durationMs, model, tokensPrompt, tokensCompletion, outcome, error, source
