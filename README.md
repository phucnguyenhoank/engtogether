# EngTogether ✍️

A **FastAPI + Vanilla JS** project for writing exercises with AI features.

---

## 📂 Project Structure

```
engtogether
├─ backend/                 # FastAPI backend
│  ├─ api/                  # API routes (HTTP endpoints only)
│  │  ├─ coedits.py
│  │  ├─ spellings.py
│  │  └─ __init__.py
│  ├─ core/                 # Core configs
│  │  ├─ config.py
│  │  └─ __init__.py
│  ├─ main.py               # FastAPI entrypoint
│  ├─ models/               # ML/NLP models (thin wrappers)
│  │  ├─ coedit_model.py
│  │  ├─ spelling_model.py
│  │  └─ __init__.py
│  ├─ schemas/              # Pydantic request/response classes
│  │  ├─ coedit.py
│  │  ├─ spelling.py
│  │  └─ __init__.py
│  ├─ services/             # Business logic (glue between API & models)
│  │  ├─ coedit_service.py
│  │  ├─ spelling_service.py
│  │  └─ __init__.py
│  └─ __init__.py
│
├─ frontend/                # Static frontend (served by FastAPI)
│  ├─ css/
│  │  └─ style.css
│  ├─ favicon.ico
│  ├─ index.html            # Entry HTML
│  └─ js/
│     ├─ api.js             # Fetch wrappers for backend
│     ├─ main.js            # App entrypoint
│     ├─ ui.js              # DOM rendering
│     └─ utils.js           # Helpers (debounce, etc.)
│
├─ tests/                   # Unit tests
│  └─ test_coedit.py
│
├─ pyproject.toml           # Dependencies (Poetry / PDM style)
├─ uv.lock                  # Lock file
├─ short_syntax.ipynb       # Playground notebook
├─ t.py                     # Scratch script
├─ .python-version          # Python version pin
└─ README.md
```

---

## 📝 Key Components

* **`backend/api/*.py`** → Defines FastAPI routes only.
* **`backend/services/*.py`** → Business logic (calls models, prepares responses).
* **`backend/models/*.py`** → Thin wrappers simulating ML/NLP models.
* **`backend/schemas/*.py`** → Pydantic request/response classes (validation + docs).
* **`backend/core/config.py`** → Configuration (CORS, settings, env vars).
* **`frontend/index.html`** → Minimal UI with exercises + buttons.
* **`frontend/js/`** → Plain JS frontend (UI + API + utils).
* **`tests/`** → Unit tests.

---

## 🚀 How to Run Locally

From project root:

### Option 1: With Uvicorn

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: With FastAPI CLI (>=0.111.0)

```bash
fastapi dev backend/main.py --host 0.0.0.0 --port 8000
```

👉 Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  
👉 Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore and test the API.

---

## 🧪 Running Tests

```bash
pytest tests/
```

