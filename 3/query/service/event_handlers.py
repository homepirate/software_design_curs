from common.event import OrderCreatedEvent, DishAddedEvent, OrderUpdatedEvent, OrderCompletedEvent
from query.model import OrderView, OrderStatus
from query.repository import OrderQueryRepository

def handle_order_created(event: OrderCreatedEvent, repository: OrderQueryRepository):
    order_view = OrderView(order_id=event.order_id, dishes=[], status=OrderStatus.NEW)
    repository.update_order(order_view)

def handle_dish_added(event: DishAddedEvent, repository: OrderQueryRepository):
    order_view = repository.get_order(event.order_id)
    if order_view:
        order_view.dishes.append(event.dish_name)
        repository.update_order(order_view)

def handle_order_updated(event: OrderUpdatedEvent, repository: OrderQueryRepository):
    order_view = repository.get_order(event.order_id)
    if order_view:
        order_view.dishes = event.new_dishes
        repository.update_order(order_view)

def handle_order_completed(event: OrderCompletedEvent, repository: OrderQueryRepository):
    order_view = repository.get_order(event.order_id)
    if order_view:
        order_view.status =  OrderStatus.COMPLETED
        repository.update_order(order_view)
