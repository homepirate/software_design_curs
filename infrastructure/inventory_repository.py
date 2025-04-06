import datetime

from domain import IInventoryRepository, Product, Inventory


class InventoryRepository(IInventoryRepository):

    def __init__(self):
        self.inventory = Inventory()

    def add(self, product: Product) -> None:
        self.inventory.add_product(product)

    def update_quantity(self, product_id: int, quantity_change: int) -> None:
        self.inventory.update_product_quantity(product_id, quantity_change)

    def adjust(self, product_id: int, new_quantity: int) -> None:
        self.inventory.adjust_inventory(product_id, new_quantity)

    def remove_expired(self, current_date: datetime.date) -> list[int]:
        return self.inventory.remove_expired_products(current_date)

    def list_all(self) -> list[Product]:
        return self.inventory.get_all_products()

    def list_critical(self) -> list[Product]:
        return self.inventory.get_critical_products()
