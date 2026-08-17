# 6. Distributed Systems

Concerns that only appear once more than one process/service is involved.

**Keep here:** notes and isolated snippets about distributed locks and their
failure modes, idempotency across retries and duplicate delivery, consistency
boundaries between services, observability across a request path
(logs/metrics/traces, correlation IDs), and deployment/rollout strategies
(rolling, blue/green, canary) where multiple instances coexist.

**Not here:** the running capstone application itself — that lives in
`/capstone`. This folder is for understanding and reference material *about*
this layer, extracted from that work.

**Maps to curriculum weeks:** 7 (idempotency, webhooks), 13 (observability),
15 (containers, CI/CD, deployment) — plus the distributed-lock caveats
covered under Week 10 (Redis).
