from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    # Dodavanje proizvoda
    manager.add_product(Product("Laptop", 80000, 5))
    manager.add_product(Product("Mobilni telefon", 50000, 10))
    manager.add_product(Product("Smartwatch", 40000, 12))

    # Prikaz proizvoda
    manager.display_all_products()

    # Prikaz ukupne vrednosti
    print(f"Ukupna vrednost inventara: {manager.total_value()} RSD.")

if __name__ == "__main__":
    main()
