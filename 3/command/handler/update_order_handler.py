from command.command import UpdateOrderCommand
from command.repository import OrderRepository
from common.event import event_bus, OrderUpdatedEvent

class UpdateOrderHandler:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def handle(self, command: UpdateOrderCommand):
        order = self.repository.get(command.order_id)
        if order is None:
            raise Exception("Order not found")
        order.dishes = command.new_dishes
        self.repository.update(order)
        event_bus.publish(OrderUpdatedEvent(order_id=command.order_id, new_dishes=command.new_dishes))
        return order
