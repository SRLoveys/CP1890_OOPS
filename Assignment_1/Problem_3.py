from dataclasses import dataclass
import csv


@dataclass
class Customer:
    # Customer class that holds attributes for the customer information and uses methods to convert the information
    # Into a printable format.
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
        # Method that determines the address format depending on the company attribute
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
    # get_customer function to take in the list of customers information and returns a list of a
    # specific customer's information.

    # Once a customer is found it applies that information to the Customer class and assigns it to the customer_info
    # class.

    # If no customer is found the function returns None allowing the main function to determine that the ID does not
    # Exist.
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
    customers = read_csv()      # converts the csv file into a list value

    while True:
        # Gets users desired customer ID and prints the information of that customer.
        # Allows user to continue as many times as they would like.
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
