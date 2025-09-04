## Project tree

```
engtogether
├─ .pytest_cache
│  ├─ CACHEDIR.TAG
│  ├─ README.md
│  └─ v
│     └─ cache
│        ├─ lastfailed
│        └─ nodeids
├─ .python-version
├─ backend
│  ├─ api
│  │  ├─ grammars.py
│  │  └─ __init__.py
│  ├─ core
│  │  ├─ config.py
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ models
│  │  ├─ grammar_model.py
│  │  └─ __init__.py
│  ├─ schemas
│  │  ├─ grammar.py
│  │  └─ __init__.py
│  ├─ services
│  │  ├─ grammar_service.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ frontend
│  ├─ assets
│  ├─ css
│  │  └─ styles.css
│  ├─ index.html
│  └─ js
│     └─ script.js
├─ pyproject.toml
├─ README.md
├─ tests
│  └─ test_grammar.py
└─ uv.lock

```


## Short descriptions

* `backend/api/grammars.py` — **routes** only. Receives HTTP requests and returns responses.
* `backend/services/grammar_service.py` — business logic glue: calls the model, prepares results for the API.
* `backend/models/grammar_model.py` — a thin wrapper that *simulates* your ML model.
* `backend/schemas/grammar.py` — Pydantic request/response classes (validation + documentation).
* `backend/core/config.py` — simple place for settings (CORS origin value used by FastAPI middleware).
* `frontend/index.html` — tiny UI that posts text to the backend and shows corrected text.
* `tests/` — unit tests for your service functions.


## How to run locally

From project root:

```bash
uvicorn backend.main:app --reload --port 8000
```
