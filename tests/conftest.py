import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.task_manager.db import Base
import os
import tempfile

@pytest.fixture(scope='function')
def db_session(tmp_path):
    db_file = tmp_path / 'test.db'
    url = f"sqlite:///{db_file}"
    engine = create_engine(url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
