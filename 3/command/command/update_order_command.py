from dataclasses import dataclass
from .command_interface import Command

@dataclass
class UpdateOrderCommand(Command):
    order_id: int
    new_dishes: list