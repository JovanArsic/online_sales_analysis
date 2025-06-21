class Cart:
    def __init__(self):
        self.cart_items = []  # lista tuple (product, quantity)

    def add_to_cart(self, product, quantity):
        self.cart_items.append((product, quantity))

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.cart_items)
    
    def display_cart(self):
        for item, quantity in self.cart_items:
            print(f"{item.name} - {item.price} RSD - {quantity} kom.")
