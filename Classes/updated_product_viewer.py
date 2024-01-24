from dataclasses import dataclass


@dataclass
class Product:

    name: str = ''
    __price: float = 0.0
    discount_percent: float = 0.0

    def __post_init__(self):
        self.price = self.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price Cannot be less than 0')
        else:
            self.__price = price

    def get_discount_amount(self) -> float:
        return self.price * (self.discount_percent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()

#    def __init__(self, name='', price=0.0, discount_percent=0.0):
#     self.__price: float = price
#        self.discount_percent: float = discount_percent
#        self.name: str = name
