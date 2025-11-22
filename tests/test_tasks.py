from src.task_manager import crud, schemas

def test_create_and_get(db_session):
    task_in = schemas.TaskCreate(title='Test', description='x')
    task = crud.create_task(db_session, task_in)
    assert task.id is not None
    fetched = crud.get_task(db_session, task.id)
    assert fetched.title == 'Test'
