# Task Manager v2

## Overview
Task Manager v2 is a small RESTful task-tracking application implemented in Python using FastAPI for the API, SQLAlchemy (SQLite) for persistence, and Typer for a command-line interface. It is designed as an interview/project submission: clean, minimal, and easy to run.

## Features
- Create, read, update, delete tasks (CRUD)
- List tasks with optional filters (priority, status)
- Mark tasks complete/incomplete
- Priority: low / medium / high
- Data persists to a local SQLite file (`tasks_v2.db`)
- CLI (Typer) and API (FastAPI) share the same database/CRUD logic
- Basic validation via Pydantic schemas
- Simple test using `pytest`

## Tech stack
- Python 3.8+
- FastAPI (API)
- Uvicorn (ASGI server)
- SQLAlchemy (ORM)
- Pydantic (validation)
- Typer (CLI)
- pytest (tests)

## Quick setup (Windows PowerShell)
1. Extract the ZIP and open PowerShell **inside** the project folder:
   - Example folder: `C:\Users\<you>\Downloads\task-manager-v2`

2. Create & activate a virtual environment (only first time):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
