
from dataclasses import dataclass


@dataclass
class Order:
    id: int
    product_id: int
    product_name: str
    quantity: int
    unit_price: float
    total: float
    status: str
