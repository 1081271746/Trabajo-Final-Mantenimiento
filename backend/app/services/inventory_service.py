
from backend.app.storage import memory


def get_inventory():
    with memory.storage_lock:

        inventory = [
            {
                "product_id": product.id,
                "name": product.name,
                "available_stock": product.stock
            }
            for product in memory.products.values()
        ]

        total_products = len(inventory)

        total_units = sum(
            product["available_stock"]
            for product in inventory
        )

    return {
        "total_products": total_products,
        "total_units": total_units,
        "inventory": inventory
    }
