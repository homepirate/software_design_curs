from command.command import CreateOrderCommand, AddDishCommand, UpdateOrderCommand, CompleteOrderCommand
from command.handler import AddDishHandler, UpdateOrderHandler, CompleteOrderHandler, CreateOrderHandler

class OrderFacade:
    def __init__(self, create_handler, add_handler, update_handler, complete_handler, query_service):
        self.create_handler = create_handler
        self.add_handler = add_handler
        self.update_handler = update_handler
        self.complete_handler = complete_handler
        self.query_service = query_service

    def create_order(self, order_id: int):
        cmd = CreateOrderCommand(order_id=order_id)
        return self.create_handler.handle(cmd)

    def add_dish(self, order_id: int, dish_name: str):
        cmd = AddDishCommand(order_id=order_id, dish_name=dish_name)
        return self.add_handler.handle(cmd)

    def update_order(self, order_id: int, new_dishes: list):
        cmd = UpdateOrderCommand(order_id=order_id, new_dishes=new_dishes)
        return self.update_handler.handle(cmd)

    def complete_order(self, order_id: int):
        cmd = CompleteOrderCommand(order_id=order_id)
        return self.complete_handler.handle(cmd)

    def get_order(self, order_id: int):
        return self.query_service.get_order_dto(order_id)

    def get_all_orders(self):
        return self.query_service.get_all_order_dtos()
