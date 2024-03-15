from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = ""
    last_name: str = ""
    email_address: str = ""

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"


@dataclass
class Customer(Person):
    customer_number: str = ""


@dataclass
class Employee(Person):
    SSN: str = ""


def main():
    person = Person()
    print("Customer/Employee Data Entry")
    choice = "y"
    while choice.lower() == "y":
        selection = input("\nCustomer or Employee? (c/e): ")
        if selection.lower() == "c":
            person = Customer()
        elif selection.lower() == "e":
            person = Employee()

        if isinstance(person, Customer):
            print("\nDATA ENTRY")
            person.first_name = input("First Name: ").title()
            person.last_name = input("Last Name: ").title()
            person.email_address = input("Email: ")
            person.customer_number = input("Number: ")
            print("\nCUSTOMER")
            print(f"Name: {person.get_fullname()}")
            print(f"Email: {person.email_address}")
            print(f"Number: {person.customer_number}")
        elif isinstance(person, Employee):
            print("\nDATA ENTRY")
            person.first_name = input("First Name: ").title()
            person.last_name = input("Last Name: ").title()
            person.email_address = input("Email: ")
            person.SSN = input("SSN: ")
            print("\nEMPLOYEE")
            print(f"Name: {person.get_fullname()}")
            print(f"Email: {person.email_address}")
            print(f"SSN: {person.SSN}")
        choice = input("\nContinue? (y/n): ")
    print("\nBye!")


if __name__ == "__main__":
    main()
