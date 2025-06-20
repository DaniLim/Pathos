# Pathosphere Project Plan

This document captures the initial design discussion for Pathosphere, a social network based on emotion words. It summarizes the mission, features, tech stack, and timeline as outlined by the AI planning session.

## 1. Name & Branding
- **Pathosphere** – *Where feelings find friends* (recommended name and tagline)
- PathosPulse
- EmotiPath
- PathWave
- Feelos

## 2. Core Concept & UX
- Users share short words or phrases that evoke feelings.
- Home feed displays posts from followed accounts and "kindred" posts matched across languages via embeddings.
- Posts can be liked, commented on, and shared.
- Cross-language matching highlights related words with visual graphs.

## Wireframe Sketches
```
+---------------------+
|  [ Feelos Logo ]    |
|  "Share a feeling"  |
|  __________________ |
| | e.g., "gratitude"| |
|  ------------------ |
|  [ Post ]           |
+---------------------+
```
```
+------------------------------+
|  Home Feed                   |
|------------------------------|
| ❤️  "calma"   - Ana          |
| ❤️  "serenity" ↔ "calma"     |
|📣 2 🗝 1                     |
|------------------------------|
| ❤️  "nostalgia" - Yuki       |
|📣 5 🗝 0                     |
| ...                          |
+------------------------------+
```
```
+------------------------------------+
| Similar Feelings (graph preview)   |
|   "felicidad" ---- "joy"           |
|       \\            /              |
|        "feliz"   " 한모 "          |
+------------------------------------+
```

## 3. MVP Feature List
**Phase 0 (Week 1–4)**
- Minimal web app to post a word/phrase and show a basic feed.
- SQLite/PostgreSQL for storage.
- Prototype cross-language matching offline.

**Phase 1 (Week 5–8)**
- User accounts with auth.
- Likes, comments, notifications.
- WebSockets for real time updates.

**Phase 2 (Week 9–12)**
- Scalable matching layer with embeddings.
- Language detection, push notifications.
- Visual explore page.

## 4. Tech Stack Proposal
- **Frontend**: Next.js (React) or Flutter Web.
- **Backend**: Python + FastAPI.
- **Database**: PostgreSQL with `pgvector`; Redis optional.
- **ML Layer**: Sentence-transformer embeddings served via vector DB or pgvector.

```
[Frontend] <--REST/WebSocket--> [FastAPI API]
                                |
                                v
                 [PostgreSQL + pgvector]
                                |
                                v
                       [Redis (optional)]
                                |
                                v
            [Worker / Embedding Service]
```

## 5. Repository Structure
```
repo-root/
├── README.md
├── docs/
│   ├── adr/
│   └── api/
├── apps/
│   ├── web/
│   ├── api/
│   └── worker/
├── packages/
│   ├── shared-ui/
│   └── shared-lib/
├── infra/
│   ├── docker/
│   ├── terraform/
│   └── github/
└── .gitignore
```
- Trunk-based development using feature branches and flags.
- Pre-commit hooks and CI for linting, type checking and tests.

## Local Development
- `docker compose up` to start services.
- `.env.example` documents required env vars; secrets managed separately.
- Tests via `npm test`, `pytest`, and e2e with Playwright.

## Deployment & Hosting
- **MVP** hosted on Fly.io.
- **Scale up** with Kubernetes on GKE or AWS EKS, Postgres replicas and a CDN.
- CI/CD via GitHub Actions deploying to staging and production with zero downtime migrations.

## Growth & Monetization Ideas
- Word-challenge events and viral loops.
- Premium graph insights and paid API for analytics.

## Risks & Mitigations
- Moderation transformer to filter abuse.
- Prevent namespace squatting.
- Test across right-to-left and CJK scripts.

## 90-Day Timeline & Team Roles
Week-by-week plan covers setup, features, matching service, and launch. Roles include PM, FE dev, BE dev, ML engineer, designer and DevOps.
