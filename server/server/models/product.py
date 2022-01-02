class Product:
    def __init__(self, name: str, price: float, quantity: float, is_countable: bool):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_countable = is_countable
        self.total = self.price * self.quantity
