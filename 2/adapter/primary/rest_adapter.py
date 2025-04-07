from domain.service import OrderService
from ..secondary import InMemoryOrderRepository, ConsoleNotificationService

class RestAPIAdapter:
    def __init__(self):
        repository = InMemoryOrderRepository()
        notifier = ConsoleNotificationService()
        self.service = OrderService(repository, notifier)

    def create_order(self, products: dict):
        order = self.service.create_order(products)
        return {"order_id": order.order_id, "status": order.status.name}

    def send_order(self, order_id: str):
        self.service.send_order(order_id)
        order = self.service.track_order(order_id)
        return {"order_id": order.order_id, "status": order.status.name}

    def confirm_order(self, order_id: str):
        self.service.confirm_order(order_id)
        order = self.service.track_order(order_id)
        return {"order_id": order.order_id, "status": order.status.name}

    def track_order(self, order_id: str):
        order = self.service.track_order(order_id)
        return {"order_id": order.order_id,
                "products": order.products,
                "created_at": order.created_at.isoformat(),
                "status": order.status.name}

    def mark_delivered(self, order_id: str):
        self.service.mark_delivered(order_id)
        order = self.service.track_order(order_id)
        return {"order_id": order.order_id, "status": order.status.name}

    def handle_return(self, order_id: str):
        self.service.handle_return(order_id)
        order = self.service.track_order(order_id)
        return {"order_id": order.order_id, "status": order.status.name}
