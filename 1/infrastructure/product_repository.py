from domain import IProductRepository, Product


class ProductRepository(IProductRepository):
    def __init__(self):
        self.products: dict[int, Product] = {}

    def add_product(self, product: Product):
        if product.product_id in self.products:
            raise ValueError("Продукт с таким ID уже существует.")
        self.products[product.product_id] = product

    def get_product(self, product_id: int) -> Product:
        if product_id not in self.products:
            raise ValueError("Продукт не найден.")
        return self.products[product_id]

    def update_product(self, product: Product):
        if product.product_id not in self.products:
            raise ValueError("Продукт не найден.")
        self.products[product.product_id] = product

    def delete_product(self, product_id: int):
        if product_id not in self.products:
            raise ValueError("Продукт не найден.")
        del self.products[product_id]

    def list_all_products(self) -> list[Product]:
        return list(self.products.values())
