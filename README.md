# AI Sales Q&A Bot

Azure-based Slack bot that answers natural-language sales questions using safe, parameterized NL?SQL templates.

### Tech Stack
- **Azure SQL (read-only)** — source of truth for sales data  
- **Azure OpenAI** — interprets natural language  
- **Azure Functions or Container Apps** — serves the API layer  
- **Slack App** — chat interface for internal users  
- **App Insights + Log Analytics** — monitoring & telemetry  

### Goals (Phase 1)
- Support 20–30 common question types (e.g., totals, top N, comparisons)
- =90% numeric accuracy from SQL results  
- P50 latency = 3 seconds  
- No exposure of PII (aggregated data only)

### Current Phase
Phase A — Environment Setup and Architecture Planning
