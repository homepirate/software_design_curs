from dataclasses import dataclass
from .command_interface import Command

@dataclass
class AddDishCommand(Command):
    order_id: int
    dish_name: str
