# main.py
from command.command import CreateOrderCommand, AddDishCommand, UpdateOrderCommand, CompleteOrderCommand
from command.handler.create_order_handler import CreateOrderHandler
from command.handler.add_dish_handler import AddDishHandler
from command.handler.update_order_handler import UpdateOrderHandler
from command.handler.complete_order_handler import CompleteOrderHandler
from command.repository.order_repository import OrderRepository

from query.repository.order_query_repository import OrderQueryRepository
from query.service.order_query_service import OrderQueryService

from common.event.event_bus import event_bus
from common.event import OrderCreatedEvent, DishAddedEvent, OrderUpdatedEvent, OrderCompletedEvent

from query.service.event_handlers import (
    handle_order_created,
    handle_dish_added,
    handle_order_updated,
    handle_order_completed
)

from api.facade import OrderFacade
from api.console.console_interface import ConsoleInterface

def main():
    # Инициализация репозиториев
    order_repository = OrderRepository()
    order_query_repository = OrderQueryRepository()

    # Подписываем обработчики событий для обновления read модели
    event_bus.subscribe(OrderCreatedEvent, lambda event: handle_order_created(event, order_query_repository))
    event_bus.subscribe(DishAddedEvent, lambda event: handle_dish_added(event, order_query_repository))
    event_bus.subscribe(OrderUpdatedEvent, lambda event: handle_order_updated(event, order_query_repository))
    event_bus.subscribe(OrderCompletedEvent, lambda event: handle_order_completed(event, order_query_repository))

    # Инициализация обработчиков команд
    create_order_handler = CreateOrderHandler(order_repository)
    add_dish_handler = AddDishHandler(order_repository)
    update_order_handler = UpdateOrderHandler(order_repository)
    complete_order_handler = CompleteOrderHandler(order_repository)

    # Инициализация сервисов запросов
    order_query_service = OrderQueryService(order_query_repository)

    # Создаём фасад, объединяющий операции командной и запросной сторон
    order_facade = OrderFacade(create_order_handler, add_dish_handler, update_order_handler, complete_order_handler, order_query_service)

    # Запускаем консольный интерфейс
    console = ConsoleInterface(order_facade)
    console.run()

if __name__ == '__main__':
    main()
