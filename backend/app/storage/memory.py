
from threading import Lock

from backend.app.models.order import Order
from backend.app.models.product import Product

products: dict[int, Product] = {}
orders: list[Order] = []

next_product_id = 1
next_order_id = 1

storage_lock = Lock()


def reset_storage():
    global next_product_id, next_order_id

    with storage_lock:
        products.clear()
        orders.clear()

        next_product_id = 1
        next_order_id = 1
