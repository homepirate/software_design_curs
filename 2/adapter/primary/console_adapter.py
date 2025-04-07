from domain.service import OrderService
from ..secondary import InMemoryOrderRepository, ConsoleNotificationService

def run_console_app():
    repository = InMemoryOrderRepository()
    notifier = ConsoleNotificationService()
    service = OrderService(repository, notifier)

    while True:
        print("\nВыберите операцию:")
        print("1. Создать заказ")
        print("2. Отправить заказ")
        print("3. Подтвердить заказ")
        print("4. Отследить заказ")
        print("5. Отметить доставку")
        print("6. Обработать возврат")
        print("0. Выход")

        choice = input("Введите номер операции: ")
        try:
            if choice == "1":
                products_input = input("Введите продукты в формате key:value, разделенные запятыми: ")
                # Простой разбор ввода в словарь
                products = {}
                for pair in products_input.split(","):
                    key, value = pair.split(":")
                    products[key.strip()] = value.strip()
                order = service.create_order(products)
                print(f"Заказ создан. ID: {order.order_id}")
            elif choice == "2":
                order_id = input("Введите ID заказа для отправки: ")
                service.send_order(order_id)
                print("Заказ отправлен поставщику.")
            elif choice == "3":
                order_id = input("Введите ID заказа для подтверждения: ")
                service.confirm_order(order_id)
                print("Заказ подтверждён.")
            elif choice == "4":
                order_id = input("Введите ID заказа для отслеживания: ")
                order = service.track_order(order_id)
                print(f"Статус заказа: {order.status.name}")
            elif choice == "5":
                order_id = input("Введите ID заказа для отметки доставки: ")
                service.mark_delivered(order_id)
                print("Поставка отмечена как доставленная.")
            elif choice == "6":
                order_id = input("Введите ID заказа для обработки возврата: ")
                service.handle_return(order_id)
                print("Возврат обработан.")
            elif choice == "0":
                print("Выход из приложения.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")

