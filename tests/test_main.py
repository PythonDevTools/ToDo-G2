'''
Tests for the "/" endpoint

For db tests, use the example:
    {
        "content": "string",
        "due": "2021-07-29T03:16:24.963Z"
    }
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient
from app.db import Base
from main import app, get_db

# Conect to the test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)

tasks_test = [
    {
        "content": "Task 1",
        "due": "2022-07-29T03:16:24.963Z"
    },
    {
        "content": "Task 2",
        "due": "2022-07-29T03:16:24.963Z"
    }
]


def test_read_main():
    '''
    Test that the "/" endpoint returns a 200 status code
    '''
    response = client.get("/")
    assert response.status_code == 200


def test_create_tasks():
    '''
    Test that the "/" endpoint returns a 200 status code
    '''
    for task in tasks_test:
        response = client.post("/", json=task)
        assert response.status_code == 200


def test_put_task_one():
    '''
    Test that the "/1" endpoint returns a 200 status code
    '''
    response = client.put("/1")
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Task 1"
    # assert data["due"] == "2022-07-29T03:16:24.963Z" # TODO: fix this


def test_put_task_two():
    '''
    Test that the "/2" endpoint returns a 200 status code
    '''
    response = client.put("/2")
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Task 2"
    # assert data["due"] == "2022-07-29T03:16:24.963Z" # TODO: fix this

