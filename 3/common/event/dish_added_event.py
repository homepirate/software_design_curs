from dataclasses import dataclass


@dataclass
class DishAddedEvent:
    order_id: int
    dish_name: str