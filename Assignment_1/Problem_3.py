from dataclasses import dataclass
import csv


@dataclass
class Customer:
    id: str = ''
    firstName: str = ''
    lastName: str = ''
    company: str = ''
    address: str = ''
    city: str = ''
    state: str = ''
    zip: str = ''

    def get_name(self):
        return f'{self.firstName} {self.lastName}'

    def get_full_address(self):
        if self.company != '':
            return f'{self.company}\n{self.address}\n{self.city}, {self.state} {self.zip}'
        else:
            return f'{self.address}\n{self.city}, {self.state} {self.zip}'


def read_csv():
    customer = []
    with open('customers.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            customer.append(row)
    return customer


def get_customer(customers):
    customer_info = None
    while True:
        customerID = input('Enter customer ID: ')
        print()

        if customerID.isnumeric():

            for i, customer in enumerate(customers):
                if customer[0] == customerID:
                    customer_info = Customer(id=customerID, firstName=customer[1], lastName=customer[2],
                                             company=customer[3], address=customer[4], city=customer[5],
                                             state=customer[6], zip=customer[7])
            return customer_info

        else:
            print("Please enter a valid integer.\n")


def main():
    print("Customer Viewer\n")
    customers = read_csv()

    while True:
        customer_info = get_customer(customers)
        if customer_info is not None:
            print(customer_info.get_name())
            print(customer_info.get_full_address())
            print()
        else:
            print("No customer with that ID.\n")

        while True:
            user_input = input("Continue? (y/n): ")
            if user_input.lower() == 'n':
                print("\nBye!")
                return
            elif user_input.lower() == 'y':
                print()
                break
            else:
                print("Invalid Input")


if __name__ == "__main__":
    main()
