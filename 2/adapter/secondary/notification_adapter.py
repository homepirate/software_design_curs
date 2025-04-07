from domain.models import Order
from domain.port import NotificationService

class ConsoleNotificationService(NotificationService):
    def notify_supplier(self, order: Order) -> None:
        print(f"Уведомление отправлено поставщику по заказу {order.order_id}")
