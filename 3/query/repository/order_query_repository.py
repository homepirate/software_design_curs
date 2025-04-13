from query.model import OrderView

class OrderQueryRepository:
    def __init__(self):
        self.order_views: dict[int, OrderView] = {}

    def update_order(self, order_view: OrderView):
        self.order_views[order_view.order_id] = order_view

    def get_order(self, order_id: int) -> OrderView:
        return self.order_views.get(order_id)

    def get_all_orders(self):
        return list(self.order_views.values())
