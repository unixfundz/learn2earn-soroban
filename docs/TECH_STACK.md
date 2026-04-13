# Learn2Earn Soroban Tech Stack

## On-chain

- Soroban smart contracts (Rust)
- `soroban-sdk` for contract interfaces and storage patterns

## Backend

- Django 5
- Django REST Framework
- Strawberry GraphQL
- Celery + Redis for async workers
- PostgreSQL for durable storage

## Frontend

- React 18 + TypeScript
- Vite
- ESLint

## DevOps and quality

- GitHub Actions CI workflows
- CodeQL static analysis
- Dependency audits (`pip-audit`, `safety`, `cargo-audit`)
- Docker Compose for local stack
- Kubernetes manifests for production deployment templates

