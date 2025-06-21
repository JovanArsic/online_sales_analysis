from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def display_all_products(self):
        for product in self.products:
            print(product.display_info())

    def total_value(self):
        return sum(product.price * product.quantity for product in self.products)
    
    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

