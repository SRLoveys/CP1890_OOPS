from dataclasses import dataclass


# @dataclass
# class Product:
#     name: str = ""
#     price: float = 0.0
#     discountPercent: int = 0.0

class Product:
    def __init__(self, name="", price=0.0, discount_percent=0.0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent


product = Product()
product = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)
product = Product("Stanley 13 Ounce Wood Hammer", 12.99)