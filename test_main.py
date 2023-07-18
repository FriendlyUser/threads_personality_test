# tests/test_items.py

from app.models import Item

from main import app
from fastapi.testclient import TestClient

test_client = TestClient(app)

def test_create_item():
    # Test creating an item
    response = test_client.post(
        "/reports/", 
        json={"name": "Foo", "description": "Something foo"}
    )
    
    assert response.status_code == 200
    # assert response.json() == {
    #     "id": 1, 
    #     "name": "Foo",
    #     "description": "Something foo",
    # }


def test_get_item():
    # Test getting an item
    response = test_client.get("/reports")
    
    assert response.status_code == 200  