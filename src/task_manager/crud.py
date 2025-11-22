from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional, List

def create_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(
        title=task_in.title,
        description=task_in.description or '',
        priority=models.Priority(task_in.priority.value if hasattr(task_in.priority, 'value') else task_in.priority),
        due_date=task_in.due_date,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def list_tasks(db: Session, skip: int = 0, limit: int = 100, priority: Optional[str] = None, status: Optional[str] = None) -> List[models.Task]:
    q = db.query(models.Task)
    if priority:
        try:
            q = q.filter(models.Task.priority == models.Priority(priority))
        except Exception:
            pass
    if status:
        q = q.filter(models.Task.status == status)
    return q.order_by(models.Task.created_at.desc()).offset(skip).limit(limit).all()

def update_task(db: Session, task: models.Task, updates: schemas.TaskUpdate) -> models.Task:
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: models.Task):
    db.delete(task)
    db.commit()
