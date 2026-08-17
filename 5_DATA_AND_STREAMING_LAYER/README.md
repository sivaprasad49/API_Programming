# 5. Data and Streaming Layer

Where state actually lives, and how it moves.

**Keep here:** notes and isolated snippets about PostgreSQL schema design,
transactions/isolation/locking, SQLAlchemy 2 + Alembic, Redis (caching,
rate limiting, coordination), background jobs, and event streaming (Redis
Streams, outbox pattern, at-least-once delivery).

**Not here:** the running capstone application itself — that lives in
`/capstone`. This folder is for understanding and reference material *about*
this layer, extracted from that work.

**Maps to curriculum weeks:** 8 (PostgreSQL & transactions), 9 (SQLAlchemy 2
& Alembic), 10 (Redis), 11 (background jobs & event processing).
