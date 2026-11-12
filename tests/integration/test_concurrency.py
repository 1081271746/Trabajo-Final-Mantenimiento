
from concurrent.futures import ThreadPoolExecutor

from fastapi import HTTPException

from backend.app.schemas.order import OrderCreate
from backend.app.schemas.product import ProductCreate
from backend.app.services.order_service import create_order
from backend.app.services.product_service import create_product
from backend.app.storage import memory


def test_concurrent_orders():
    memory.reset_storage()

    product = create_product(
        ProductCreate(
            name="Teclado Gamer",
            price=120000,
            stock=5
        )
    )

    def make_order():
        try:
            create_order(
                OrderCreate(
                    product_id=product.id,
                    quantity=1
                )
            )
            return True

        except HTTPException as error:
            if error.status_code == 400:
                return False
            raise

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(
            lambda _: make_order(),
            range(10)
        ))

    successful_orders = results.count(True)
    rejected_orders = results.count(False)

    assert successful_orders == 5
    assert rejected_orders == 5

    assert memory.products[product.id].stock == 0
    assert len(memory.orders) == 5
