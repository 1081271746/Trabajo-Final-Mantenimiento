
from backend.app.schemas.product import ProductCreate
from backend.app.services.product_service import create_product
from backend.app.services.inventory_service import get_inventory
from backend.app.storage.memory import reset_storage


def test_get_inventory():
    reset_storage()

    create_product(
        ProductCreate(
            name="Teclado",
            price=120000,
            stock=20
        )
    )

    create_product(
        ProductCreate(
            name="Mouse",
            price=80000,
            stock=15
        )
    )

    inventory = get_inventory()

    assert inventory["total_products"] == 2
    assert inventory["total_units"] == 35
    assert len(inventory["inventory"]) == 2


def test_empty_inventory():
    reset_storage()

    inventory = get_inventory()

    assert inventory["total_products"] == 0
    assert inventory["total_units"] == 0
    assert inventory["inventory"] == []


def test_inventory_stock_values():
    reset_storage()

    create_product(
        ProductCreate(
            name="Monitor",
            price=500000,
            stock=10
        )
    )

    inventory = get_inventory()

    assert inventory["inventory"][0]["available_stock"] == 10
    assert inventory["inventory"][0]["name"] == "Monitor"
