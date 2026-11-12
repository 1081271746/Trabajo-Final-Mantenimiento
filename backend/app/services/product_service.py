
from backend.app.models.product import Product
from backend.app.schemas.product import ProductCreate
from backend.app.storage import memory


def create_product(product_data: ProductCreate) -> Product:

    with memory.storage_lock:

        product_id = memory.next_product_id

        product = Product(
            id=product_id,
            name=product_data.name,
            price=product_data.price,
            stock=product_data.stock
        )

        memory.products[product_id] = product

        memory.next_product_id += 1

    return product


def get_products():
    with memory.storage_lock:
        product_list = list(memory.products.values())

    return {
        "total": len(product_list),
        "products": product_list
    }
