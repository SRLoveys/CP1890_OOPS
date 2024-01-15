from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discountPercent: float

    def get_discount_amount(self):
        return self.price * (self.discountPercent / 100)

    def get_discount_price(self):
        return self.price - self.get_discount_amount()


product1 = Product(name="Stanley 13 Ounce Wood Hammer", price=12.99, discountPercent=62)
product2 = Product(name='National Hardware 3/4" Wire Nails', price=15.50, discountPercent=48)
product3 = Product(name="Economy Duct Tape, 60 yds, Silver", price=9.99, discountPercent=31)


def title():
    print("The Product Viewer Program\n")


def product_list():
    print("PRODUCTS")
    print('1. Stanley 13 Ounce Wood Hammer\n2. National Hardware 3/4" Wire Nails')
    print("3. Economy Duct Tape, 60 yds, Silver")


def main():
    title()
    product_list()
    choice = "y"
    while choice.lower() == "y":
        product_choice = int(input("Enter product number: "))
        if product_choice == 1:
            print("\nProduct Data")
            print(f"Product Name:\t\t {product1.name}")
            print(f"Product Price:\t\t {product1.price:.2f}")
            print(f"Discount Percent:\t {product1.discountPercent:d}%")
            print(f"Discount Amount:\t {product1.get_discount_amount():.2f}")
            print(f"Discount Price:\t\t {product1.get_discount_price():.2f}")

            choice = input("\nView another product? (y/n): ")
        elif product_choice == 2:
            print("\nProduct Data")
            print(f"Product Name:\t\t {product2.name}")
            print(f"Product Price:\t\t {product2.price:.2f}")
            print(f"Discount Percent:\t {product2.discountPercent:d}%")

            print(f"Discount Amount:\t {product2.get_discount_amount():.2f}")
            print(f"Discount Price:\t\t {product2.get_discount_price():.2f}")
            choice = input("\nView another product? (y/n): ")
        elif product_choice == 3:
            print("\nProduct Data")
            print(f"Product Name:\t\t {product3.name}")
            print(f"Product Price:\t\t {product3.price:.2f}")
            print(f"Discount Percent:\t {product3.discountPercent:d}%")

            print(f"Discount Amount:\t {product3.get_discount_amount():.2f}")
            print(f"Discount Price:\t\t {product3.get_discount_price():.2f}")
            choice = input("\nView another product? (y/n): ")
        else:
            print("Bye!")


main()
