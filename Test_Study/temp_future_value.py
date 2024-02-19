import locale as lc
lc.setlocale(lc.LC_ALL, 'en-ca')


def get_monthly_investment():
    try:
        monthly_investment = float(input("Enter monthly investment: "))
        return monthly_investment
    except ValueError:
        print("Must be a valid number")


def get_interest_rate():
    try:
        interest_rate = float(input("Enter yearly interest rate: "))
        if interest_rate <= 0:
            print("Please enter a number greater than 0")
        return interest_rate
    except ValueError:
        print("Please enter a number greater than 0")


def get_number_of_years():
    try:
        years = int(input("Enter number of years: "))
        if years <= 0:
            print("Please enter a number greater than 0")
        return years
    except ValueError:
        print("Please enter a number greater than 0")


def get_future_value(monthly_investment, interest_rate, years):
    future_value = 0
    for i in range(years*12):
        future_value += monthly_investment
        monthly_interest = future_value * (interest_rate/(12*100))
        future_value += monthly_interest
    return future_value


def main():
    while True:
        monthly_investment = get_monthly_investment()
        interest_rate = get_interest_rate()
        years = get_number_of_years()
        future_value = get_future_value(monthly_investment, interest_rate, years)
        print(f"\nMonthly investment: {lc.currency(monthly_investment, grouping=True):>15}")
        print(f"Interest rate: {interest_rate:>20}")
        print(f"Years: {years:>28}")
        print(f"Future Value: {lc.currency(future_value, grouping=True):>21}")
        continue_check = input("\nDo you want to continue? (y/n): ")
        if continue_check.lower() == "n":
            break
        print("Bye!")


if __name__ == "__main__":
    main()
