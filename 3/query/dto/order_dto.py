from dataclasses import dataclass
from query.model import OrderStatus

@dataclass
class OrderDTO:
    order_id: int
    dishes: list[str]
    status: OrderStatus