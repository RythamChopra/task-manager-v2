# Task Manager v2

A small RESTful task-tracking application implemented in Python using **FastAPI**, **SQLAlchemy (SQLite)** for persistence, and **Typer** for a command-line interface.  
Built as an interview assignment — clean, simple, and easy to run.

---

## Features
- Create / Read / Update / Delete tasks (CRUD)
- List tasks with filters (priority, status)
- Mark tasks complete / incomplete
- Priority levels: `low`, `medium`, `high`
- Persistent SQLite database (`tasks_v2.db`)
- Shared CRUD logic between API and CLI
- Validation using Pydantic models
- Basic tests using `pytest`
- Simple static frontend (`/static/index.html`) that interacts with the API

---

## Tech Stack
- Python 3.8+
- FastAPI
- SQLAlchemy (ORM)
- Uvicorn (ASGI server)
- Typer (CLI)
- Pydantic
- pytest

---

# Quick Start (Complete Instructions)

These commands allow **ANY reviewer** to run the project on **Windows / macOS / Linux**.

---

## 1. Clone the repository
```bash
git clone https://github.com/RythamChopra/task-manager-v2
cd task-manager-v2
```

---

## 2. Create & activate a virtual environment  

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 4. (Optional) Reset the database  
If you want a clean DB:

```powershell
del tasks_v2.db      # Windows
```

```bash
rm tasks_v2.db       # macOS/Linux
```

Recreate tables:
```bash
python -c "from src.task_manager.db import Base, engine; Base.metadata.create_all(engine)"
```

---

## 5. Start the FastAPI backend
```bash
uvicorn src.task_manager.main:app --reload --host 127.0.0.1 --port 8000
```

Backend available at:
- **http://127.0.0.1:8000**
- **API Docs:** http://127.0.0.1:8000/docs

---

## 6. Serve the frontend UI (Important)

Do **NOT** double-click the HTML file.  
Browsers block API calls from `file://` pages.

Instead, serve the `static/` folder using Python’s built-in server:

### Windows / macOS / Linux
```bash
cd static
python -m http.server 8001
```

Open the UI in a browser:
```
http://127.0.0.1:8001/index.html
```

The UI automatically communicates with:
```
http://127.0.0.1:8000
```

---

## 7. Use the CLI (Typer)

### Create a task
```bash
python -m src.task_manager.cli create "Buy milk" --description "From store" --priority high
```

### List tasks
```bash
python -m src.task_manager.cli list
```

### Mark task complete
```bash
python -m src.task_manager.cli complete 1
```

---

## 8. Run tests
```bash
pytest -q
```

---

# Project Structure

```
task-manager-v2/
│── src/
│   └── task_manager/
│       ├── main.py          # FastAPI app
│       ├── cli.py           # Typer CLI
│       ├── db.py            # DB session factory + Base
│       ├── models.py        # SQLAlchemy models
│       ├── schemas.py       # Pydantic schemas
│       ├── crud.py          # CRUD functions
│── static/
│   └── index.html           # Frontend UI
│── tests/
│── requirements.txt
│── README.md
│── tasks_v2.db
```

---

##  Notes
- Virtual environment is **not** included in the repo.
- Works identically on Windows, macOS, and Linux.
- API + CLI share the same database logic.
- Frontend requires running a static server.

---

##  Done!
Your project is fully ready for review.  
If you need deployment help or enhancements, feel free to ask!

