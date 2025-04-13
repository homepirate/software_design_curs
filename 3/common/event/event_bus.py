from typing import Type, Callable

class EventBus:
    def __init__(self):
        self.subscribers: dict[Type, list[Callable]] = {}

    def subscribe(self, event_type: Type, handler: Callable):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event):
        for subscriber in self.subscribers.get(type(event), []):
            subscriber(event)

event_bus = EventBus()
