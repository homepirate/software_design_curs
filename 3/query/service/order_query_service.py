from query.repository import OrderQueryRepository
from query.dto import OrderDTO

class OrderQueryService:
    def __init__(self, repository: OrderQueryRepository):
        self.repository = repository

    def get_order_dto(self, order_id: int) -> OrderDTO:
        order_view = self.repository.get_order(order_id)
        if order_view is None:
            return None
        return OrderDTO(order_id=order_view.order_id, dishes=order_view.dishes, status=order_view.status)

    def get_all_order_dtos(self):
        order_views = self.repository.get_all_orders()
        return [OrderDTO(order_id=o.order_id, dishes=o.dishes, status=o.status) for o in order_views]
