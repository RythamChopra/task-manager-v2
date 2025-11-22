from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from . import db, models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='Task Manager API v2')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001", "http://localhost:8001", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.on_event('startup')
def on_startup():
    db.init_db()

@app.post('/tasks/', response_model=schemas.TaskOut)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task_in)

@app.get('/tasks/{task_id}', response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return task

@app.get('/tasks/', response_model=list[schemas.TaskOut])
def list_tasks(skip: int = 0, limit: int = 100, priority: str | None = Query(None), status: str | None = Query(None), db: Session = Depends(get_db)):
    return crud.list_tasks(db, skip=skip, limit=limit, priority=priority, status=status)

@app.patch('/tasks/{task_id}', response_model=schemas.TaskOut)
def update_task(task_id: int, updates: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return crud.update_task(db, task, updates)

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    crud.delete_task(db, task)
    return {'ok': True}

@app.post('/tasks/{task_id}/toggle', response_model=schemas.TaskOut)
def toggle_complete(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    task.completed = not task.completed
    db.commit()
    db.refresh(task)
    return task
