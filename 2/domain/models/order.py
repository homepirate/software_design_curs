import datetime
import uuid
from dataclasses import dataclass, field
from .order_status import OrderStatus

@dataclass
class Order:
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    products: dict = field(default_factory=dict)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    status: OrderStatus = OrderStatus.CREATED

    def send(self):
        if self.status != OrderStatus.CREATED:
            raise ValueError("Заказ можно отправить только если он в статусе CREATED.")
        self.status = OrderStatus.SENT

    def confirm(self):
        if self.status != OrderStatus.SENT:
            raise ValueError("Подтверждать можно только отправленный заказ.")
        self.status = OrderStatus.CONFIRMED

    def mark_delivered(self):
        if self.status != OrderStatus.CONFIRMED:
            raise ValueError("Поставку можно принять только если заказ подтверждён.")
        self.status = OrderStatus.DELIVERED

    def mark_returned(self):
        if self.status not in [OrderStatus.SENT, OrderStatus.CONFIRMED, OrderStatus.DELIVERED]:
            raise ValueError("Возврат возможен только после отправки заказа.")
        self.status = OrderStatus.RETURNED