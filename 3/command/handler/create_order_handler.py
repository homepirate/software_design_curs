from command.command import CreateOrderCommand
from command.model import Order
from command.repository import OrderRepository
from common.event import event_bus, OrderCreatedEvent

class CreateOrderHandler:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def handle(self, command: CreateOrderCommand):
        order = Order(order_id=command.order_id)
        self.repository.save(order)
        event_bus.publish(OrderCreatedEvent(order_id=command.order_id))
        return order
