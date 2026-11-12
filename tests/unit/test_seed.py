
from backend.app.core.seed import seed_products
from backend.app.storage import memory


def test_seed_products_creates_products():
    memory.reset_storage()

    seed_products(total=10, stock=50)

    assert len(memory.products) == 10
    assert memory.next_product_id == 11

    for product in memory.products.values():
        assert product.stock == 50


def test_seed_products_resets_previous_data():
    memory.reset_storage()

    seed_products(total=5, stock=20)

    memory.products[1].stock = 0

    seed_products(total=3, stock=100)

    assert len(memory.products) == 3
    assert memory.products[1].stock == 100
    assert memory.next_product_id == 4
    assert len(memory.orders) == 0
