
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


def test_create_product_api():
    response = client.post(
        "/products",
        json={
            "name": "Teclado Gamer",
            "price": 120000,
            "stock": 20
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Teclado Gamer"
    assert data["stock"] == 20


def test_get_products_api():
    client.post(
        "/products",
        json={
            "name": "Mouse Gamer",
            "price": 80000,
            "stock": 15
        }
    )

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 1
    assert len(data["products"]) == 1
    assert data["products"][0]["name"] == "Mouse Gamer"


def test_get_empty_products_api():
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == {
        "total": 0,
        "products": []
    }


def test_invalid_product_api():
    response = client.post(
        "/products",
        json={
            "name": "Teclado",
            "price": -100,
            "stock": 10
        }
    )

    assert response.status_code == 422


def test_product_response_is_json():
    response = client.get("/products")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith(
        "application/json"
    )
