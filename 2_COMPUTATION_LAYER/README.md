# 2. Computation Layer

The framework-independent core: business rules and domain logic.

**Keep here:** notes and isolated snippets about domain modeling, type-driven
design (dataclasses, Pydantic vs ORM models, protocols, generics), service
objects, and exceptions-as-domain-signals. The test of "does this belong
here" — could this code run and be unit-tested with zero web framework and
zero database installed?

**Not here:** the running capstone application itself — that lives in
`/capstone`. This folder is for understanding and reference material *about*
this layer, extracted from that work.

**Maps to curriculum weeks:** 2 (modern Python for API systems), and the
service-layer parts of 5 (dependency injection & structure).
