from dataclasses import dataclass
import random


@dataclass
class Die:
    value: int

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


class Dice:
    dice: list

    def add_dice(self, value):
        self.dice.append(value)

    def roll_all(self, dice):
        for value in dice:
            dice[value].Die.roll(self)


