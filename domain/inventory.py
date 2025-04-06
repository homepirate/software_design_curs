import datetime
from dataclasses import dataclass, field

from .product import Product


@dataclass
class Inventory:
    products: dict[int, Product] = field(default_factory=dict)

    def add_product(self, product: Product):
        if product.product_id in self.products:
            raise ValueError("Продукт с таким ID уже существует.")
        self.products[product.product_id] = product

    def update_product_quantity(self, product_id: int, quantity_change: int):
        if product_id not in self.products:
            raise ValueError("Продукт не найден.")
        product = self.products[product_id]
        product.quantity += quantity_change
        if product.quantity < 0:
            product.quantity = 0

    def adjust_inventory(self, product_id: int, new_quantity: int):
        if product_id not in self.products:
            raise ValueError("Продукт не найден.")
        self.products[product_id].quantity = new_quantity

    def remove_expired_products(self, current_date: datetime.date) -> list[int]:
        expired_ids = [pid for pid, prod in self.products.items() if prod.is_expired(current_date)]
        for pid in expired_ids:
            del self.products[pid]
        return expired_ids

    def get_all_products(self) -> list[Product]:
        return list(self.products.values())

    def get_critical_products(self) -> list[Product]:
        return [prod for prod in self.products.values() if prod.quantity <= prod.critical_level]
