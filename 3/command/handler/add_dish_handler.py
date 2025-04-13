from command.command import AddDishCommand
from command.repository import OrderRepository
from common.event import event_bus, DishAddedEvent


class AddDishHandler:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def handle(self, command: AddDishCommand):
        order = self.repository.get(command.order_id)
        if order is None:
            raise Exception("Order not found")
        order.dishes.append(command.dish_name)
        self.repository.update(order)
        event_bus.publish(DishAddedEvent(order_id=command.order_id, dish_name=command.dish_name))
        return order
