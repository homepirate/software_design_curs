from abc import ABC, abstractmethod

from .product import Product


class IProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        ...

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        ...

    @abstractmethod
    def update_product(self, product: Product):
        ...

    @abstractmethod
    def delete_product(self, product_id: int):
        ...

    @abstractmethod
    def list_all_products(self) -> list[Product]:
        ...