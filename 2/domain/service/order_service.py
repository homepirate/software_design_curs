from ..models import Order
from ..port import OrderManagementPort, OrderRepository, NotificationService

class OrderService(OrderManagementPort):
    def __init__(self, repository: OrderRepository, notifier: NotificationService):
        self.repository = repository
        self.notifier = notifier

    def create_order(self, products: dict) -> Order:
        order = Order(products=products)
        self.repository.save(order)
        return order

    def send_order(self, order_id: str) -> None:
        order = self.repository.get(order_id)
        if order is None:
            raise ValueError("Заказ не найден")
        order.send()
        self.repository.update(order)
        self.notifier.notify_supplier(order)

    def confirm_order(self, order_id: str) -> None:
        order = self.repository.get(order_id)
        if order is None:
            raise ValueError("Заказ не найден")
        order.confirm()
        self.repository.update(order)

    def track_order(self, order_id: str) -> Order:
        order = self.repository.get(order_id)
        if order is None:
            raise ValueError("Заказ не найден")
        return order

    def mark_delivered(self, order_id: str) -> None:
        order = self.repository.get(order_id)
        if order is None:
            raise ValueError("Заказ не найден")
        order.mark_delivered()
        self.repository.update(order)

    def handle_return(self, order_id: str) -> None:
        order = self.repository.get(order_id)
        if order is None:
            raise ValueError("Заказ не найден")
        order.mark_returned()
        self.repository.update(order)
