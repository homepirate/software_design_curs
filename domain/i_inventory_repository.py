import datetime
from abc import ABC, abstractmethod

from .product import Product


class IInventoryRepository(ABC):

    @abstractmethod
    def add(self, product: Product) -> None:

        ...
    @abstractmethod
    def update_quantity(self, product_id: int, quantity_change: int) -> None:
        ...

    @abstractmethod
    def adjust(self, product_id: int, new_quantity: int) -> None:
        ...

    @abstractmethod
    def remove_expired(self, current_date: datetime.date) -> list[int]:
        ...

    @abstractmethod
    def list_all(self) -> list[Product]:
        ...

    @abstractmethod
    def list_critical(self) -> list[Product]:
        ...