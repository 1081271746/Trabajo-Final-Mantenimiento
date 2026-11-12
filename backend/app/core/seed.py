
from backend.app.storage import memory
from backend.app.models.product import Product


def seed_products(total: int = 500, stock: int = 500):
    """
    Carga productos de prueba para evaluar el rendimiento de StockTest.
    """

    memory.reset_storage()

    with memory.storage_lock:
        for product_id in range(1, total + 1):
            product = Product(
                id=product_id,
                name=f"Producto de prueba {product_id}",
                price=10000 + (product_id * 100),
                stock=stock
            )

            memory.products[product_id] = product

        memory.next_product_id = total + 1

    print(f"Se cargaron {total} productos correctamente.")
    print(f"Cada producto tiene {stock} unidades disponibles.")
