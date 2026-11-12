
from fastapi import HTTPException

from backend.app.models.order import Order
from backend.app.schemas.order import OrderCreate
from backend.app.storage import memory


def create_order(order_data: OrderCreate) -> Order:

    with memory.storage_lock:

        # Buscar el producto solicitado
        product = memory.products.get(order_data.product_id)

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        # Comprobar existencias disponibles
        if product.stock < order_data.quantity:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "Insufficient stock",
                    "available": product.stock,
                    "requested": order_data.quantity
                }
            )

        # Calcular el valor del pedido
        total = product.price * order_data.quantity

        # Crear el pedido
        order = Order(
            id=memory.next_order_id,
            product_id=product.id,
            product_name=product.name,
            quantity=order_data.quantity,
            unit_price=product.price,
            total=total,
            status="confirmed"
        )

        # Guardar el pedido
        memory.orders.append(order)

        # Descontar las existencias
        product.stock -= order_data.quantity

        # Actualizar el identificador
        memory.next_order_id += 1

    return order
