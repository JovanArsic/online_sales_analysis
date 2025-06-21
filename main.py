from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    # Dodavanje proizvoda
    manager.add_product(Product("Tablet", 80000, 5))
    manager.add_product(Product("Smartphone", 50000, 10))
    manager.add_product(Product("Smartwatch", 40000, 12))

if __name__ == "__main__":
    main()
