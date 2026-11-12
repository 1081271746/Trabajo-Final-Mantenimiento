
from itertools import count

from locust import HttpUser, task, between


product_counter = count(1)


class StockTestOrderUser(HttpUser):

    wait_time = between(1, 3)

    @task
    def create_order(self):

        product_id = ((next(product_counter) - 1) % 500) + 1

        with self.client.post(
            "/orders",
            json={
                "product_id": product_id,
                "quantity": 1
            },
            name="POST /orders",
            catch_response=True
        ) as response:

            if response.status_code == 201:
                response.success()
            else:
                response.failure(
                    f"Error al registrar pedido: {response.status_code}"
                )
