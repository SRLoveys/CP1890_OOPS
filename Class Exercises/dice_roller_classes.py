import random
from dataclasses import dataclass


@dataclass
class Die:
    value: int = 1

    def roll(self):
        self.value = random.randint(1, 6)


class Dice:
    def __init__(self):
        self.list_die = []

    def add_die(self, die):
        self.list_die.append(die)

    def roll_all(self):
        for die in self.list_die:
            die.roll()
