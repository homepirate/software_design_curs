from abc import ABC, abstractmethod
from ...models import Order

class NotificationService(ABC):
    @abstractmethod
    def notify_supplier(self, order: Order) -> None:
        pass
