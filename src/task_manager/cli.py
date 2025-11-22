import typer
from .db import SessionLocal, init_db
from . import crud, schemas

app = typer.Typer(help='Task Manager CLI v2')

@app.command()
def init():
    init_db()
    typer.echo('DB initialized (tasks_v2.db)')

@app.command()
def create(title: str, description: str = '', priority: str = 'medium'):
    db = SessionLocal()
    task_in = schemas.TaskCreate(title=title, description=description, priority=priority)
    task = crud.create_task(db, task_in)
    typer.echo(f'Created task {task.id} - {task.title}')

@app.command('list')
def _list(priority: str = None, status: str = None):
    db = SessionLocal()
    tasks = crud.list_tasks(db, priority=priority, status=status)
    if not tasks:
        typer.echo('No tasks found')
        return
    for t in tasks:
        typer.echo(f"{t.id}: {t.title} | priority={t.priority.name if hasattr(t.priority,'name') else t.priority} | completed={t.completed} | due={t.due_date}")

@app.command()
def complete(task_id: int):
    db = SessionLocal()
    task = crud.get_task(db, task_id)
    if not task:
        typer.echo('Task not found')
        raise typer.Exit(code=1)
    task.completed = True
    db.commit()
    typer.echo('Task marked complete')

if __name__ == '__main__':
    app()
