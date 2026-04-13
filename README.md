# Learn2Earn Soroban — Learn. Earn. On-chain.

![Django CI](https://github.com/learn2earn/learn2earn/actions/workflows/django-ci.yml/badge.svg)
![Soroban CI](https://github.com/learn2earn/learn2earn/actions/workflows/soroban-ci.yml/badge.svg)
![Frontend CI](https://github.com/learn2earn/learn2earn/actions/workflows/frontend-ci.yml/badge.svg)
![Security](https://github.com/learn2earn/learn2earn/actions/workflows/security.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Learn2Earn Soroban is an open-source, incentive-driven learning platform built on **Stellar Soroban**.

Create quests, define milestones, lock rewards on-chain, and release payouts only when milestones are verified.

---

## Why Learn2Earn Soroban?

Traditional learning platforms rely on willpower alone. Learn2Earn Soroban adds skin in the game:

- mentors and teams fund quests with real tokens
- learners unlock rewards only by completing milestones
- contract logic enforces outcomes without centralized trust

### Who it helps

- **Companies**: onboard devs with milestone-based token rewards
- **DAOs**: fund community education with verifiable outcomes
- **Teachers**: incentivize students with micro-rewards
- **Mentors**: back a mentee's learning journey with financial commitment

---

## How it works

`Create Quest` → `Fund Quest` → `Learn` → `Verify` → `Earn`

1. A creator defines quest milestones.
2. Tokens are locked in the rewards contract.
3. Learner completes milestones off-chain.
4. Verifier confirms completion.
5. Contract releases milestone payout.

---

## Delivery stage

Learn2Earn Soroban is currently a **contract-first** project with a partially integrated frontend:

- Soroban contracts are implemented and tested in the Rust workspace.
- Frontend has wallet flows and selected reads wired.
- Some write flows remain intentionally mocked pending indexer/history completion.
- Earnings aggregate is available on-chain; detailed payout history indexing is in progress.

---

## Terminology

- **Project name:** `Learn2Earn Soroban`
- **Blockchain platform:** `Stellar`
- **Smart-contract runtime on Stellar:** `Soroban`

Folder names like `soroban-contracts/` are intentional and correct.
They describe the Soroban runtime target.

---

## Core features

- **Soroban contracts** for quests, enrollments, milestones, and reward release logic
- **Django API/indexer layer** for contract events and payout history preparation
- **GraphQL + REST** read APIs for app and analytics consumers
- **React + Vite frontend** with Freighter wallet integration scaffold
- **PostgreSQL + Redis + Celery** for durable ingestion and async processing
- **Kubernetes manifests** for production deployment patterns
- **CI/CD** with quality gates, docs checks, security audits, and release automation

---

## Architecture

```text
Soroban Contracts  ->  Ingestion Layer (Django mgmt/celery)  ->  PostgreSQL
                                            |
                                            +-> REST API
                                            +-> GraphQL API
                                            +-> Frontend (Vite + React)
```

Detailed architecture notes live in:
- `docs/ARCHITECTURE.md`

---

## Repository structure

```text
learn2earn-soroban/
├── soroban-contracts/
│   └── learn2earn_core/
│       ├── Cargo.toml
│       └── src/lib.rs
├── django-backend/
│   ├── learn2earn/
│   │   ├── core/            # settings, urls, celery, wsgi/asgi
│   │   └── ingest/      # models, views, schema, tasks, ingest command
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
├── k8s/
├── .github/workflows/
├── docs/
├── docker-compose.yml
└── LICENSE
```

---

## Quick start (local)

### Prerequisites

- Docker
- Docker Compose
- Node.js 20+
- pnpm 9+
- Rust stable toolchain

### Run

```bash
cp django-backend/.env.example django-backend/.env
docker compose up --build
```

### Quality checks

```bash
cd django-backend
pip install -r requirements.txt
ruff check .
pytest

cd ../frontend
pnpm install
pnpm lint
pnpm build

cd ../soroban-contracts/learn2earn_core
cargo fmt -- --check
cargo clippy --target wasm32-unknown-unknown -- -D warnings
cargo test
```

Services:
- REST API: `http://localhost:8000/api/events/`
- GraphQL Playground: `http://localhost:8000/graphql/`
- Django Admin: `http://localhost:8000/admin/`

---

## Smart contracts

```bash
cd soroban-contracts/learn2earn_core
cargo test
stellar contract build
```

---

## Frontend

```bash
cd frontend
pnpm install
cp .env.example .env.local
pnpm dev
```

Install Freighter, switch to Testnet, and connect.

---

## Production deployment (Kubernetes)

1. Build and push backend container image.
2. Create namespace + secrets/config.
3. Apply manifests in `k8s/`.
4. Verify backend, worker, and beat health.

```bash
kubectl apply -f k8s/
kubectl get pods -n learn2earn
```

---

## Roadmap (summary)

| Milestone | Status | Focus |
|---|---|---|
| M1 Quest Foundation | In Repo | Core contract structure, validation, tooling |
| M2 Quest Engine | In Progress | Deadlines live, discovery visibility, funding variants |
| M3 Neo-Brutalism UI | In Repo | Frontend screens + design system prototype |
| M4 Full Stack Integration | Partial | Wallet + reads wired, writes partly mocked |
| M5 Quality & Advanced | Planned | Security audit, indexing, advanced features |

---

## CI/CD workflows

- `django-ci.yml` (lint + test backend)
- `soroban-ci.yml` (contract build)
- `frontend-ci.yml` (lint + build frontend)
- `contract-quality.yml` (fmt + clippy + tests)
- `security.yml` (dependency audits)
- `codeql.yml` (static security analysis)
- `docs-ci.yml` (markdown + link checks)
- `release.yml` (tag-based release artifacts)

---

## Open-source readiness checklist

- MIT license
- Contributing guide
- Architecture docs
- Local/dev/prod deployment paths
- Typed/pinned dependencies
- CI + security workflows

---

## Contributing

See `CONTRIBUTING.md` for contribution workflow, coding standards, PR requirements, and quality gates.

See `SECURITY.md` for responsible disclosure.

See `CODE_OF_CONDUCT.md` for community standards.

## License

MIT — see `LICENSE`.
