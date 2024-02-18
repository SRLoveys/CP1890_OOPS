from dataclasses import dataclass


@dataclass
class Product:
    name: str = ""
    price: float = 0.0
    discountPercent: int = 0.0

    def get_discount_amount(self):
        return self.price * self.discountPercent / 100

    def get_discount_price(self):
        return self.price - self.get_discount_amount()
