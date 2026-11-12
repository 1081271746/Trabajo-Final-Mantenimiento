
import pytest
from pydantic import ValidationError

from backend.app.schemas.product import ProductCreate


def test_valid_product():
    product = ProductCreate(
        name="Teclado Gamer",
        price=120000,
        stock=20
    )

    assert product.name == "Teclado Gamer"
    assert product.price == 120000
    assert product.stock == 20


def test_product_name_removes_extra_spaces():
    product = ProductCreate(
        name="  Mouse Gamer  ",
        price=80000,
        stock=15
    )

    assert product.name == "Mouse Gamer"


def test_product_name_cannot_be_empty():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="   ",
            price=80000,
            stock=15
        )


def test_product_price_must_be_positive():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="Teclado",
            price=0,
            stock=10
        )


def test_product_price_cannot_be_negative():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="Teclado",
            price=-500,
            stock=10
        )


def test_product_stock_cannot_be_negative():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="Mouse",
            price=80000,
            stock=-5
        )
