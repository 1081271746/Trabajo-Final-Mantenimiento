
from backend.app.models.product import Product
from backend.app.storage.memory import products, reset_storage


def test_product_creation():
    product = Product(
        id=1,
        name="Teclado Gamer",
        price=120000,
        stock=20
    )

    assert product.id == 1
    assert product.name == "Teclado Gamer"
    assert product.price == 120000
    assert product.stock == 20


def test_memory_storage():
    reset_storage()

    product = Product(
        id=1,
        name="Mouse Gamer",
        price=80000,
        stock=15
    )

    products[product.id] = product

    assert len(products) == 1
    assert products[1].name == "Mouse Gamer"

    reset_storage()

    assert len(products) == 0
