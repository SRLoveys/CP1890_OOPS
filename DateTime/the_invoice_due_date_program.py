from datetime import date, datetime, timedelta


def title():
    print("The Invoice Due Date Program")


def get_invoice_date():
    invoice_date = input("Enter the invoice date (MM/DD/YY): ")
    invoice_date = datetime.strptime(invoice_date, "%m/%d/%y)")
    return invoice_date


def get_due_date(invoice_date):
    due_date = invoice_date + timedelta(days=30)
    return due_date


def main():
    title()
    current_date = date.today()
    invoice_date = get_invoice_date()
    due_date = get_due_date(invoice_date)
    overdue_days = (current_date - due_date).days
    while True:
        print(f"Invoice Date: {invoice_date}")
        print(f"Due Date: {due_date}")
        print(f"Current Date: {current_date}")
        print(f"Overdue Days: {overdue_days}")


main()
