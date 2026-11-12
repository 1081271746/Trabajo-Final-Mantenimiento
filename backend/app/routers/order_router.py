
from fastapi import APIRouter, status

from backend.app.schemas.order import OrderCreate, OrderListResponse, OrderResponse
from backend.app.services.order_service import create_order
from backend.app.storage import memory

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def register_order(order_data: OrderCreate):
    return create_order(order_data)


@router.get(
    "",
    response_model=OrderListResponse,
    status_code=status.HTTP_200_OK
)
def list_orders():
    with memory.storage_lock:
        return {
            "total": len(memory.orders),
            "orders": list(memory.orders)
        }
