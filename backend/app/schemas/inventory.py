
from pydantic import BaseModel


class InventoryItem(BaseModel):
    product_id: int
    name: str
    available_stock: int


class InventoryResponse(BaseModel):
    total_products: int
    total_units: int
    inventory: list[InventoryItem]
