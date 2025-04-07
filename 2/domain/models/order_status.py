from enum import Enum


class OrderStatus(Enum):
    CREATED = "CREATED"
    SENT = "SENT"
    CONFIRMED = "CONFIRMED"
    DELIVERED = "DELIVERED"
    RETURNED = "RETURNED"