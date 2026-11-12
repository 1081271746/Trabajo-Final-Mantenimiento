
from fastapi.testclient import TestClient

from backend.app.main import app, startup_event


def test_home_endpoint():
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Bienvenido a StockTest",
        "status": "API funcionando correctamente"
    }


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "application": "StockTest"
    }


def test_startup_event():
    startup_event()

    from backend.app.storage import memory

    assert len(memory.products) == 500
    assert memory.next_product_id == 501
