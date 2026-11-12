
from fastapi import FastAPI

from backend.app.core.seed import seed_products
from backend.app.routers.inventory_router import router as inventory_router
from backend.app.routers.order_router import router as order_router
from backend.app.routers.product_router import router as product_router

app = FastAPI(
    title="StockTest API",
    description="API REST para la gestión de inventario y pedidos",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    seed_products(total=500, stock=500)


app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(order_router)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a StockTest",
        "status": "API funcionando correctamente"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "StockTest"
    }
