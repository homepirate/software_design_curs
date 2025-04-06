import datetime

from domain import IInventoryRepository, Product


class InventoryService:
    def __init__(self, repository: IInventoryRepository):
        self.repo = repository

    def add_new_product(self, product: Product):
        self.repo.add(product)

    def use_product(self, product_id: int, quantity_used: int):
        self.repo.update_quantity(product_id, -quantity_used)

    def adjust_inventory(self, product_id: int, new_quantity: int):
        self.repo.adjust(product_id, new_quantity)

    def remove_expired_products(self, current_date: datetime.date) -> list[int]:
        return self.repo.remove_expired(current_date)

    def generate_report(self) -> list[Product]:
        return self.repo.list_all()

    def list_critical_products(self) -> list[Product]:
        return self.repo.list_critical()