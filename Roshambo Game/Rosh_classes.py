"""
The class for the Roshambo game that will be imported the
Game file 'Rosh_game'
"""

from dataclasses import dataclass
import random
rosh_choices = ("rock", "paper", "scissors")


@dataclass
class Player:

    name: str = ""
    roshambo: str = ""
    __wins: int = 0
    __losses: int = 0

    def generate_roshambo(self):
        self.roshambo = rosh_choices[0]

    def play_roshambo(self, other_player):
        player_value = self.roshambo
        opponent_value = other_player.roshambo

        if player_value == opponent_value:
            return None

        if player_value == "rock":
            if opponent_value == "scissors":
                return self
            elif opponent_value == "paper":
                return other_player

        if player_value == "scissors":
            if opponent_value == "paper":
                return self
            elif opponent_value == "rock":
                return other_player

        if player_value == "paper":
            if opponent_value == "rock":
                return self
            elif opponent_value == "scissors":
                return other_player

    @property
    def wins(self):
        return self.__wins

    @property
    def losses(self):
        return self.__losses

    def add_win(self):
        self.__wins += 1

    def add_loss(self):
        self.__losses += 1

    def __str__(self):
        return f"{self.name}: {self.roshambo}"


@dataclass
class Bart(Player):

    def __post_init__(self):
        self.name = "Bart"


@dataclass
class Lisa(Player):

    def __post_init__(self):
        self.name = "Lisa"

    def generate_roshambo(self):
        ran_num = random.randint(0, 2)
        self.roshambo = rosh_choices[ran_num]



