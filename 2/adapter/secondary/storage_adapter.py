from domain.models import Order
from domain.port import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def save(self, order: Order) -> None:
        self.orders[order.order_id] = order

    def update(self, order: Order) -> None:
        self.orders[order.order_id] = order

    def get(self, order_id: str) -> Order:
        return self.orders.get(order_id)
