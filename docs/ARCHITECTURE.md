# Learn2Earn Soroban Indexer Architecture

Learn2Earn Soroban Indexer follows a hybrid on-chain/off-chain architecture.

## On-chain Layer

The Soroban contract:
- stores admin identity
- controls authorized indexers
- emits normalized `EventRecord` structures

## Off-chain Layer

Django services:
- poll and ingest Soroban-related events
- persist events in PostgreSQL
- expose REST and GraphQL APIs
- dispatch signed webhooks asynchronously via Celery

## Production Targets

- Horizontal backend scaling via Kubernetes deployments
- Independent worker scaling by queue
- Redis-backed task and retry orchestration
- Secret management through Kubernetes secrets / External Secrets
