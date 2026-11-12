
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


def test_create_order_api():
    client.post(
        "/products",
        json={
            "name": "Teclado Gamer",
            "price": 120000,
            "stock": 20
        }
    )

    response = client.post(
        "/orders",
        json={
            "product_id": 1,
            "quantity": 3
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["product_id"] == 1
    assert data["quantity"] == 3
    assert data["total"] == 360000
    assert data["status"] == "confirmed"


def test_order_reduces_inventory_api():
    client.post(
        "/products",
        json={
            "name": "Mouse Gamer",
            "price": 80000,
            "stock": 15
        }
    )

    client.post(
        "/orders",
        json={
            "product_id": 1,
            "quantity": 5
        }
    )

    response = client.get("/inventory")

    data = response.json()

    assert response.status_code == 200
    assert data["inventory"][0]["available_stock"] == 10


def test_order_with_nonexistent_product_api():
    response = client.post(
        "/orders",
        json={
            "product_id": 999,
            "quantity": 2
        }
    )

    assert response.status_code == 404


def test_order_with_insufficient_stock_api():
    client.post(
        "/products",
        json={
            "name": "Monitor",
            "price": 500000,
            "stock": 5
        }
    )

    response = client.post(
        "/orders",
        json={
            "product_id": 1,
            "quantity": 10
        }
    )

    assert response.status_code == 400

    inventory_response = client.get("/inventory")

    assert inventory_response.json()["total_units"] == 5


def test_get_orders_api():
    client.post(
        "/products",
        json={
            "name": "Teclado",
            "price": 120000,
            "stock": 10
        }
    )

    client.post(
        "/orders",
        json={
            "product_id": 1,
            "quantity": 2
        }
    )

    response = client.get("/orders")

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 1
    assert len(data["orders"]) == 1
    assert data["orders"][0]["product_name"] == "Teclado"
