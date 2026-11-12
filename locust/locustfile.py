
from locust import HttpUser, task, between


class StockTestUser(HttpUser):

    # Tiempo de espera entre solicitudes
    wait_time = between(1, 3)

    # Consultar productos
    @task(3)
    def get_products(self):
        self.client.get(
            "/products",
            name="GET /products"
        )

    # Consultar inventario
    @task(2)
    def get_inventory(self):
        self.client.get(
            "/inventory",
            name="GET /inventory"
        )

    # Consultar pedidos
    @task(1)
    def get_orders(self):
        self.client.get(
            "/orders",
            name="GET /orders"
        )
