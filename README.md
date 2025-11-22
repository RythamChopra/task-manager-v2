# Task Manager v2

A simple RESTful task-tracking application implemented in Python using FastAPI, SQLAlchemy (SQLite) for persistence, and Typer for a command-line interface. Designed as a clean, minimal technical assignment that is easy to run and evaluate.

---

## Features
- Create / Read / Update / Delete tasks (CRUD)
- Filter tasks by priority or completion status
- Mark tasks complete / incomplete
- Task fields: title, description, status, priority, created_at, due_date
- SQLite persistence (`tasks_v2.db`)
- CLI tool using Typer
- API using FastAPI with automatic docs
- Simple HTML frontend (`static/index.html`)
- Unit test using pytest

---

## Tech stack
- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Typer (CLI)
- pytest

---

#  Quick Start (Complete Instructions)

These commands allow ANY reviewer on Windows, macOS or Linux to run the project.

---

## 1. Clone the repository
```bash
git clone https://github.com/RythamChopra/task-manager-v2
cd task-manager-v2
