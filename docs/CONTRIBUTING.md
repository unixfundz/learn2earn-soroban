# Contributing to Learn2Earn Soroban

## Development Standards

- Open an issue for non-trivial changes before implementation.
- Follow Conventional Commits.
- Add tests for all behavior changes.
- Keep PRs small and focused.

## Local Setup

```bash
cp django-backend/.env.example django-backend/.env
docker compose up --build
```

Frontend setup:

```bash
cd frontend
pnpm install
pnpm dev
```

## Code Quality

Backend checks:

```bash
ruff check django-backend
pytest
```

Contract checks:

```bash
cd soroban-contracts/learn2earn_core
cargo fmt --check
cargo clippy -- -D warnings
```

Frontend checks:

```bash
cd frontend
pnpm lint
pnpm build
```
