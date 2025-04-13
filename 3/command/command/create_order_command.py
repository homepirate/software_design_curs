from dataclasses import dataclass
from .command_interface import Command

@dataclass
class CreateOrderCommand(Command):
    order_id: int
