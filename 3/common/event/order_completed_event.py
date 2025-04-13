from dataclasses import dataclass


@dataclass
class OrderCompletedEvent:
    order_id: int