from dataclasses import dataclass

@dataclass
class Product:
    name: str = ""
    __price: float = 0.0
    discountPercent: int = 0

    def __post_init__(self):
        self.price = self.__price