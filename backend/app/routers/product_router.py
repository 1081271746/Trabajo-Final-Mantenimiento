
from fastapi import APIRouter, status

from backend.app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductListResponse
)

from backend.app.services.product_service import (
    create_product,
    get_products
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def register_product(product_data: ProductCreate):
    product = create_product(product_data)

    return product


@router.get(
    "",
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK
)
def list_products():
    return get_products()
