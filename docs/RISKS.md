# Risks & Mitigations

| Risk                                 | Likelihood | Impact | Mitigation                                   | Owner  |
|--------------------------------------|------------|--------|-----------------------------------------------|--------|
| Ambiguous time zone logic            | Med        | High   | Fix offset in views; document in dictionary   | You    |
| SQL permissions too broad            | Low        | High   | Read-only login; no PII in views              | You    |
| Latency spikes (cold start)          | Med        | Med    | Keep Functions warm; short prompts            | You    |
