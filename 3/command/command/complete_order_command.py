from dataclasses import dataclass
from .command_interface import Command

@dataclass
class CompleteOrderCommand(Command):
    order_id: int
