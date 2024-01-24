from dataclasses import dataclass
import random

# this is  the die and dice class objects that have been given
# private access modifiers.


@dataclass
class Die:
    __value: int = 1

    def getvalue(self):
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)


class Dice:
    def __init__(self):
        self.__list_die: list = []

    def getlist(self):
        return self.__list_die

    def add_die(self, die):
        self.__list_die.append(die)

    def roll_all(self):
        for die in self.__list_die:
            die.roll()

    @property
    def list_dice(self) -> list:
        return tuple(self.__list_die)