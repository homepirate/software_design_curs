from dataclasses import dataclass


@dataclass
class OrderUpdatedEvent:
    order_id: int
    new_dishes: list[str]