from dataclasses import dataclass
import datetime

@dataclass
class Product:
    product_id: int
    name: str
    quantity: int
    expiry_date: datetime.date
    minimum_stock: int
    optimal_stock: int
    critical_level: int

    def is_expired(self, current_date: datetime.date) -> bool:
        return self.expiry_date < current_date