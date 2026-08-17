# 7. AI Integration Layer

Bolting AI/LLM features onto a production API, once the fundamentals are solid.

**Keep here:** notes and isolated snippets about calling LLM APIs from a
service (streaming responses, timeouts, retries, cost/latency trade-offs),
tool use / function calling, RAG-style data plumbing, and the same production
concerns (auth, rate limiting, observability) applied to AI-backed endpoints.

**Not here:** the running capstone application itself — that lives in
`/capstone`. This folder is for understanding and reference material *about*
this layer, extracted from that work.

**Maps to curriculum weeks:** none directly — this layer isn't covered by
`fastapi_litestar_api_curriculum.html`. Treat it as a self-directed extension
to tackle after the 18-week roadmap, applying the same engineering standards
(validation, tests, error handling, observability) to AI-specific endpoints.
