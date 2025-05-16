import pytest
from src.utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_todo(api_client):
    response = api_client.get_todo(1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_todo(api_client):
    new_todo = {
        "userId": 1,
        "title": "Learn API testing",
        "completed": False
    }
    response = api_client.create_todo(new_todo)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Learn API testing"

def test_update_todo(api_client):
    updated_todo = {
        "userId": 1,
        "title": "Updated title",
        "completed": True
    }
    response = api_client.update_todo(1, updated_todo)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated title"
    assert data["completed"] is True

def test_delete_todo(api_client):
    response = api_client.delete_todo(1)
    assert response.status_code in [200, 204]