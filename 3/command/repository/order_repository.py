from command.model import Order


class OrderRepository:
    def __init__(self):
        self.orders: dict[int, Order] = {}

    def save(self, order: Order):
        self.orders[order.order_id] = order

    def get(self, order_id: int) -> Order:
        return self.orders.get(order_id)

    def update(self, order: Order):
        self.orders[order.order_id] = order
