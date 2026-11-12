
import pytest
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.storage.memory import reset_storage


client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_storage():
    reset_storage()
    yield
    reset_storage()


def test_get_inventory_api():
    client.post(
        "/products",
        json={
            "name": "Teclado",
            "price": 120000,
            "stock": 20
        }
    )

    client.post(
        "/products",
        json={
            "name": "Mouse",
            "price": 80000,
            "stock": 15
        }
    )

    response = client.get("/inventory")

    assert response.status_code == 200

    data = response.json()

    assert data["total_products"] == 2
    assert data["total_units"] == 35
    assert len(data["inventory"]) == 2


def test_empty_inventory_api():
    response = client.get("/inventory")

    assert response.status_code == 200

    assert response.json() == {
        "total_products": 0,
        "total_units": 0,
        "inventory": []
    }


def test_inventory_contains_product_stock():
    client.post(
        "/products",
        json={
            "name": "Monitor",
            "price": 500000,
            "stock": 10
        }
    )

    response = client.get("/inventory")

    data = response.json()

    assert data["inventory"][0]["name"] == "Monitor"
    assert data["inventory"][0]["available_stock"] == 10
