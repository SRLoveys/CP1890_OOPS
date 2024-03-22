import random


class RandomIntList(list):
    def __init__(self, length):
        for x in range(length):
            rand_int = random.randint(1, 100)
            self.append(rand_int)

    def __str__(self):
        return ', '.join(map(str, list(self)))

    def get_count(self):
        return len(self)

    def get_total(self):
        return sum(self)

    def get_average(self):
        return sum(self) / self.get_count()


def main():
    choice = "y"
    while choice == "y":
        print("Random Integer List")
        while True:
            number = int(input("\nHow many random integers should the list contain?: "))
            if number < 1 or number > 100:
                print("please enter a valid number")
            else:
                break
        print("\nRandom Integers")
        print("="*15)
        int_list = RandomIntList(number)
        print(f"Integers: {int_list}")
        count = int_list.get_count()
        print(f"Count: {count}")
        total = int_list.get_total()
        print(f"Total: {total}")
        average = int_list.get_average()
        print(f"Average: {average:.3f}")
        choice = input("\nContinue? (y/n): ")
    print("Bye!")


if __name__ == "__main__":
    main()
