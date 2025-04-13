from dataclasses import dataclass, field

from .order_status import OrderStatus
@dataclass
class Order:
    order_id: int
    dishes: list[str] = field(default_factory=list)
    status: OrderStatus = OrderStatus.NEW