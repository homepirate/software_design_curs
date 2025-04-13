from dataclasses import dataclass


@dataclass
class OrderCreatedEvent:
    order_id: int
