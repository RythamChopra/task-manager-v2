# Task Manager v2

A small RESTful task-tracking application implemented in Python using **FastAPI**, **SQLAlchemy (SQLite)** for persistence, and **Typer** for a command-line interface.  
Built as an interview assignment — clean, simple, and easy to run.

---

## 🚀 Features
- Create / Read / Update / Delete tasks (CRUD)
- List tasks with filters (priority, status)
- Mark tasks complete / incomplete
- Priority levels: `low`, `medium`, `high`
- Persistent SQLite database (`tasks_v2.db`)
- Shared CRUD logic between API and CLI
- Validation using Pydantic models
- Basic tests using `pytest`
- Simple static frontend (`/static/index.html`)

---

## 🧰 Tech Stack
- Python 3.8+
- FastAPI
- SQLAlchemy (ORM)
- Uvicorn (ASGI server)
- Typer (CLI)
- Pydantic
- pytest

---

# ⚡ Quick Start (Complete Instructions)

These commands allow **ANY reviewer** to run the project on **Windows / Linux / macOS**.

---

## 1. Clone the repository
```bash
git clone https://github.com/RythamChopra/task-manager-v2
cd task-manager-v2
```

---

## 2. Create & activate a virtual environment  
### Windows (PowerShell)
```bash
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
If reviewers want a clean database:

```bash
del tasks_v2.db          # Windows
rm tasks_v2.db           # macOS/Linux
```

Run once to auto-create tables:
```bash
python -c "from src.task_manager.db import Base, engine; Base.metadata.create_all(engine)"
```

---

## 5. Run the FastAPI backend
```bash
uvicorn src.task_manager.main:app --reload --port 8000
```

Backend available at:
**http://127.0.0.1:8000**

API docs:
**http://127.0.0.1:8000/docs**

---

## 6. Open the frontend UI  
Simply open this file in a browser:

```
static/index.html
```

The UI automatically connects to:

```
http://127.0.0.1:8000
```

---

## 7. Use the CLI (Typer)
Examples:

### Create a task
```bash
python -m src.task_manager.cli create "Buy milk" --description "From store" --priority high
```

### List tasks
```bash
python -m src.task_manager.cli list
```

### Mark complete
```bash
python -m src.task_manager.cli complete 1
```

---

## 8. Run tests
```bash
pytest -q
```

---

##  Project Structure
```
task-manager-v2/
│── src/
│   └── task_manager/
│       ├── main.py          # FastAPI app
│       ├── cli.py           # Typer CLI
│       ├── db.py            # DB session + base
│       ├── models.py        # SQLAlchemy models
│       ├── schemas.py       # Pydantic models
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
- No virtual environments or large files are included in the repo.
- The project runs identically on Windows, Linux, and macOS.
- API + CLI share the same database and logic.

---

##  Done!
This project is fully ready for review.  
If you need anything else, feel free to reach out!

