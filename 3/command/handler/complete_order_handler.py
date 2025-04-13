from command.command import CompleteOrderCommand
from command.repository import OrderRepository
from common.event import event_bus, OrderCompletedEvent
from command.model import OrderStatus

class CompleteOrderHandler:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def handle(self, command: CompleteOrderCommand):
        order = self.repository.get(command.order_id)
        if order is None:
            raise Exception("Order not found")
        order.status = OrderStatus.COMPLETED
        self.repository.update(order)
        event_bus.publish(OrderCompletedEvent(order_id=command.order_id))
        return order
