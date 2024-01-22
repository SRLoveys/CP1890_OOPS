from dataclasses import dataclass
import random


@dataclass
class Die:
    __value: int = 1

<<<<<<< HEAD
    def get_value(self):
=======
    def getValue(self):
>>>>>>> origin/master
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)

<<<<<<< HEAD

die1 = Die()
die1.__value = 10
print("Die value: ", die1.__value, die1.get_value())
=======
die2 = Die()
die2.__value = 10
print("Die value: ", die2.__value, die2.getValue())
>>>>>>> origin/master
