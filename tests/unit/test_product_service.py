
from backend.app.schemas.product import ProductCreate
from backend.app.services.product_service import create_product
from backend.app.storage.memory import products, reset_storage


def test_create_product():
    reset_storage()

    product_data = ProductCreate(
        name="Teclado Gamer",
        price=120000,
        stock=20
    )

    product = create_product(product_data)

    assert product.id == 1
    assert product.name == "Teclado Gamer"
    assert product.price == 120000
    assert product.stock == 20


def test_product_is_saved_in_memory():
    reset_storage()

    product_data = ProductCreate(
        name="Mouse Gamer",
        price=80000,
        stock=15
    )

    product = create_product(product_data)

    assert 1 in products
    assert products[1] == product


def test_product_ids_are_incremented():
    reset_storage()

    first_product = ProductCreate(
        name="Teclado",
        price=120000,
        stock=10
    )

    second_product = ProductCreate(
        name="Mouse",
        price=80000,
        stock=15
    )

    product_one = create_product(first_product)
    product_two = create_product(second_product)

    assert product_one.id == 1
    assert product_two.id == 2
