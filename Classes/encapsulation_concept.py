from dataclasses import dataclass
import random


@dataclass
class Die:
    __value: int = 1

    def get_value(self):
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)


die1 = Die()
die1.__value = 10
print("Die value: ", die1.__value, die1.get_value())
