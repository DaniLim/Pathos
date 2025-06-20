# Pathosphere

*Where feelings find friends*

Pathosphere is a multilingual microblogging platform for sharing single words or short phrases that evoke feelings. Users can like, comment and share posts across languages.

The repository stores planning documents and progress logs for building the MVP.

- See [PLAN.md](PLAN.md) for the project roadmap.
- Daily updates: `progress/daily/`
- Weekly summaries: `progress/weekly/`

## Running Locally

1. Copy `.env.example` to `.env`.
2. Start the API and frontend with `docker compose up`.
   - Web: <http://localhost:3000>
   - API docs: <http://localhost:8000/docs>

Install dependencies from `apps/api/requirements.txt` if you want to run the
tests directly and then execute `pytest`.

Licensed under the MIT License.
