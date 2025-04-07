from abc import ABC, abstractmethod
from ...models import Order

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def update(self, order: Order) -> None:
        pass

    @abstractmethod
    def get(self, order_id: str) -> Order:
        pass