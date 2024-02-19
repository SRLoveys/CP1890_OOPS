import random
from dataclasses import dataclass


@dataclass
class Die:
    __value: int = 1

    def roll(self):
        self.__value = random.randint(1, 6)

    @property
    def get_value(self):
        return self.__value


class Dice:
    def __init__(self):
        self.__list_die = []

    def add_die(self, die):
        self.__list_die.append(die)

    def roll_all(self):
        for die in self.__list_die:
            die.roll()

    @property
    def list_dice(self):
        return tuple(self.__list_die)

print("test")
