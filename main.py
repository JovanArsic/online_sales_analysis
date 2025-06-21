from product import Product
from product_manager import ProductManager
from cart import Cart

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


    cart = Cart()
    cart.add_to_cart(manager.products[0], 2)
    cart.add_to_cart(manager.products[1], 1)
    cart.add_to_cart(manager.products[2], 1)

    print("Sadržaj korpe:")
    cart.display_cart()
    print(f"Ukupna cena za naplatu: {cart.total_price()} RSD.")

if __name__ == "__main__":
    main()
