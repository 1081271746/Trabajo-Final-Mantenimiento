
from pydantic import BaseModel, Field, ConfigDict


class OrderCreate(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    product_name: str
    quantity: int
    unit_price: float
    total: float
    status: str


class OrderListResponse(BaseModel):
    total: int
    orders: list[OrderResponse]
