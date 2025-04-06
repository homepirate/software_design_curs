import datetime

from application.inventory_service import InventoryService
from domain import Product
from infrastructure.inventory_repository import InventoryRepository


def print_product(product: Product):
    print(f"ID: {product.product_id} | Наименование: {product.name} | Количество: {product.quantity} "
          f"| Срок годности: {product.expiry_date} | Мин: {product.minimum_stock} | Опт: {product.optimal_stock} | Крит: {product.critical_level}")

def console_interface():
    repo = InventoryRepository()
    service = InventoryService(repo)

    while True:
        print("\nМеню управления инвентаризацией:")
        print("1. Добавить новый продукт")
        print("2. Использовать продукт (уменьшить количество)")
        print("3. Провести инвентаризацию (корректировка запасов)")
        print("4. Списать просроченные продукты")
        print("5. Сгенерировать отчет по запасам")
        print("6. Показать продукты с критическим уровнем")
        print("0. Выход")
        choice = input("Введите номер операции: ").strip()

        if choice == "1":
            try:
                product_id = int(input("ID продукта: "))
                name = input("Наименование продукта: ")
                quantity = int(input("Количество: "))
                expiry_input = input("Срок годности (ГГГГ-ММ-ДД): ")
                expiry_date = datetime.datetime.strptime(expiry_input, "%Y-%m-%d").date()
                minimum_stock = int(input("Минимальный запас: "))
                optimal_stock = int(input("Оптимальный запас: "))
                critical_level = int(input("Критический уровень: "))
                product = Product(
                    product_id=product_id,
                    name=name,
                    quantity=quantity,
                    expiry_date=expiry_date,
                    minimum_stock=minimum_stock,
                    optimal_stock=optimal_stock,
                    critical_level=critical_level
                )
                service.add_new_product(product)
                print("Продукт успешно добавлен.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            try:
                product_id = int(input("ID продукта: "))
                quantity_used = int(input("Количество для списания: "))
                service.use_product(product_id, quantity_used)
                print("Количество продукта обновлено.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            try:
                product_id = int(input("ID продукта для корректировки: "))
                new_quantity = int(input("Новое количество: "))
                service.adjust_inventory(product_id, new_quantity)
                print("Запасы успешно скорректированы.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            try:
                today = datetime.date.today()
                expired_ids = service.remove_expired_products(today)
                if expired_ids:
                    print(f"Списаны просроченные продукты с ID: {expired_ids}")
                else:
                    print("Просроченных продуктов не найдено.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            products = service.generate_report()
            if not products:
                print("Запасы пусты.")
            else:
                print("Отчет по запасам:")
                for prod in products:
                    print_product(prod)

        elif choice == "6":
            critical_products = service.list_critical_products()
            if not critical_products:
                print("Нет продуктов с критическим уровнем запасов.")
            else:
                print("Продукты с критическим уровнем запасов:")
                for prod in critical_products:
                    print_product(prod)

        elif choice == "0":
            print("Выход из системы...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")