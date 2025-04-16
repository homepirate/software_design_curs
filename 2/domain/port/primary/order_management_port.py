from abc import ABC, abstractmethod
from ...models import Order

class OrderManagementPort(ABC):
    @abstractmethod
    def create_order(self, products: dict) -> Order:
        pass

    @abstractmethod
    def send_order(self, order_id: str) -> None:
        pass

    @abstractmethod
    def confirm_order(self, order_id: str) -> None:
        pass

    @abstractmethod
    def track_order(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def handle_return(self, order_id: str) -> None:
        pass