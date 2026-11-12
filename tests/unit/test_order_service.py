
import pytest
from fastapi import HTTPException

from backend.app.schemas.product import ProductCreate
from backend.app.schemas.order import OrderCreate

from backend.app.services.product_service import create_product
from backend.app.services.order_service import create_order

from backend.app.storage.memory import (
    products,
    orders,
    reset_storage
)


def test_create_order_successfully():
    reset_storage()

    product = create_product(
        ProductCreate(
            name="Teclado Gamer",
            price=120000,
            stock=20
        )
    )

    order = create_order(
        OrderCreate(
            product_id=product.id,
            quantity=3
        )
    )

    assert order.id == 1
    assert order.product_name == "Teclado Gamer"
    assert order.quantity == 3
    assert order.total == 360000
    assert order.status == "confirmed"


def test_order_reduces_product_stock():
    reset_storage()

    product = create_product(
        ProductCreate(
            name="Mouse Gamer",
            price=80000,
            stock=15
        )
    )

    create_order(
        OrderCreate(
            product_id=product.id,
            quantity=5
        )
    )

    assert products[product.id].stock == 10


def test_order_with_nonexistent_product():
    reset_storage()

    with pytest.raises(HTTPException) as error:
        create_order(
            OrderCreate(
                product_id=999,
                quantity=2
            )
        )

    assert error.value.status_code == 404


def test_order_with_insufficient_stock():
    reset_storage()

    product = create_product(
        ProductCreate(
            name="Monitor",
            price=500000,
            stock=5
        )
    )

    with pytest.raises(HTTPException) as error:
        create_order(
            OrderCreate(
                product_id=product.id,
                quantity=10
            )
        )

    assert error.value.status_code == 400
    assert products[product.id].stock == 5
    assert len(orders) == 0


def test_order_is_saved_in_memory():
    reset_storage()

    product = create_product(
        ProductCreate(
            name="Teclado",
            price=120000,
            stock=10
        )
    )

    order = create_order(
        OrderCreate(
            product_id=product.id,
            quantity=2
        )
    )

    assert len(orders) == 1
    assert orders[0] == order
