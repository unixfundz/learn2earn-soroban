# Contributing to Learn2Earn Soroban

Thanks for your interest in contributing to Learn2Earn Soroban.
This project aims to be a reliable open-source learning + reward platform on Soroban/Stellar.

## Code of conduct

By participating, you agree to collaborate respectfully and constructively.

## Ways to contribute

- Report bugs
- Propose features
- Improve docs
- Add tests
- Optimize ingestion/performance
- Improve deployment and operations tooling

## Development setup

### Prerequisites

- Python 3.11+
- Docker + Docker Compose
- Rust toolchain (for contract work)
- Node.js 20+
- pnpm 9+

### Local run

```bash
cp django-backend/.env.example django-backend/.env
docker compose up --build
```

Backend URLs:
- REST: `http://localhost:8000/api/events/`
- GraphQL: `http://localhost:8000/graphql/`

## Branching and commits

- Branch from `main`
- Use focused branches: `feat/...`, `fix/...`, `docs/...`, `chore/...`
- Follow Conventional Commits:
  - `feat:` new features
  - `fix:` bug fixes
  - `docs:` documentation
  - `refactor:` internal improvements
  - `test:` tests
  - `chore:` maintenance

Example:
```bash
git checkout -b feat/webhook-signature-v2
git commit -m "feat: add webhook replay-protection timestamp"
```

## Pull request requirements

Before opening a PR:

1. Rebase on latest `main`
2. Ensure lint/test pass locally
3. Add or update tests for behavior changes
4. Update docs when behavior/config changes
5. Keep PR scope focused and reviewable

PR template checklist:

- [ ] Change is scoped and documented
- [ ] Tests added/updated
- [ ] Backward-compatibility impact considered
- [ ] Security impact considered
- [ ] Migration impact documented (if any)

## Quality gates

### Backend

```bash
cd django-backend
pip install -r requirements.txt
ruff check .
pytest
```

### Soroban contract

```bash
cd soroban-contracts/learn2earn_core
cargo fmt -- --check
cargo clippy --target wasm32-unknown-unknown -- -D warnings
cargo test
```

### Frontend

```bash
cd frontend
pnpm install
pnpm lint
pnpm build
```

## Issue reporting guideline

Include:
- expected behavior
- actual behavior
- reproduction steps
- relevant logs/errors
- environment (OS, Python/Rust versions)

## Security issues

Do not open public issues for sensitive vulnerabilities.
Share details privately with maintainers and allow time for coordinated disclosure.

## License

By contributing, you agree your contributions are licensed under the MIT License.
