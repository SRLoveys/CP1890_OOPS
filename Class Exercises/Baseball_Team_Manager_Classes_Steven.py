from dataclasses import dataclass


@dataclass
class Player:
    __first_name: str = ''
    __last_name: str = ''
    __position: str = ''
    __atBats: int = 0
    __hits: int = 0

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    def avg(self):
        return self.__hits / self.__atBats
