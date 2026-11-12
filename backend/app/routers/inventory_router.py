
from fastapi import APIRouter, status

from backend.app.schemas.inventory import InventoryResponse
from backend.app.services.inventory_service import get_inventory

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.get(
    "",
    response_model=InventoryResponse,
    status_code=status.HTTP_200_OK
)
def list_inventory():
    return get_inventory()
