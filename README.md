# EngTogether ✍️

A **FastAPI + Vanilla JS** project for writing exercises with AI features.

---

## 📂 Project Structure

```
engtogether
├─ .python-version
├─ backend
│  ├─ api
│  │  ├─ coedits.py
│  │  ├─ exercises.py
│  │  ├─ spellings.py
│  │  └─ __init__.py
│  ├─ core
│  │  ├─ config.py
│  │  ├─ database.py
│  │  ├─ models.py
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ models
│  │  ├─ coedit_model.py
│  │  ├─ pygect5_model.py
│  │  ├─ spelling_model.py
│  │  └─ __init__.py
│  ├─ schemas
│  │  ├─ coedit.py
│  │  ├─ exercise.py
│  │  ├─ spelling.py
│  │  └─ __init__.py
│  ├─ services
│  │  ├─ coedit_service.py
│  │  ├─ exercise_service.py
│  │  ├─ pygect5_service.py
│  │  ├─ spelling_service.py
│  │  └─ __init__.py
│  ├─ utils
│  │  ├─ text_processing.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ frontend
│  ├─ css
│  │  └─ style.css
│  ├─ favicon.ico
│  ├─ index.html
│  └─ js
│     ├─ api.js
│     ├─ main.js
│     ├─ ui.js
│     └─ utils.js
├─ pyproject.toml
├─ README.md
├─ short_syntax.ipynb
├─ t.py
├─ tests
│  └─ test_coedit.py
└─ uv.lock

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
fastapi dev backend/main.py --host localhost --port 8000
```

👉 Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  
👉 Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore and test the API.

---

## 🧪 Running Tests

```bash
pytest tests/
```

