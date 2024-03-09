from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    price: float = 0.0
    discountPercent: int = 0

    def get_discount_amount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()

    def get_description(self) -> str:
        return self.name


@dataclass
class Book(Product):
    author: str = ''

    def get_description(self) -> str:
        return f"{Product.get_description(self)} by {self.author}"


@dataclass
class Movie(Product):
    year: int = 0

    def get_description(self) -> str:
        return f"{Product.get_description(self)}  {self.year}"


def main():
    product1 = Product('Quartet Marker', 2.99, 20)
    book1 = Book('The Shining', 12.00, 10, 'Stephen King')
    movie1 = Movie('Venom', 12.00, 5, 2013)
    print("PRODUCT DATA")
    if isinstance(product1, Product):
        print(f"Name: {product1.get_description()}")
        print(f"Discount Price: {product1.get_discount_price()}")

