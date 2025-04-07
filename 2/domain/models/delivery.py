import datetime
from dataclasses import dataclass


@dataclass
class Delivery:
    delivery_id: str
    supply_order_id: str
    dispatched_at: datetime.datetime = None
    received_at: datetime.datetime = None

    def dispatch(self):
        self.dispatched_at = datetime.datetime.now()

    def receive(self):
        if not self.dispatched_at:
            raise ValueError("Нельзя принять поставку до отправки.")
        self.received_at = datetime.datetime.now()