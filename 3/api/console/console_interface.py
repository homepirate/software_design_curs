from api.facade import OrderFacade

class ConsoleInterface:
    def __init__(self, order_facade: OrderFacade):
        self.order_facade = order_facade

    def run(self):
        while True:
            print("\n--- Меню ---")
            print("1. Создать заказ")
            print("2. Добавить блюдо в заказ")
            print("3. Изменить заказ")
            print("4. Завершить заказ")
            print("5. Получить информацию по заказу")
            print("6. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                order_id = int(input("Введите ID заказа: "))
                self.order_facade.create_order(order_id)
                print("Заказ создан.")
            elif choice == "2":
                order_id = int(input("Введите ID заказа: "))
                dish_name = input("Введите название блюда: ")
                self.order_facade.add_dish(order_id, dish_name)
                print("Блюдо добавлено.")
            elif choice == "3":
                order_id = int(input("Введите ID заказа: "))
                dishes = input("Введите блюда через запятую: ").split(',')
                dishes = [dish.strip() for dish in dishes]
                self.order_facade.update_order(order_id, dishes)
                print("Заказ обновлён.")
            elif choice == "4":
                order_id = int(input("Введите ID заказа: "))
                self.order_facade.complete_order(order_id)
                print("Заказ завершён.")
            elif choice == "5":
                order_id = int(input("Введите ID заказа: "))
                order = self.order_facade.get_order(order_id)
                print("Информация о заказе:", order)
            elif choice == "6":
                print("Выход.")
                break
            else:
                print("Неверный выбор.")
