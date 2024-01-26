from encapsulation_die_class_object import Die
from dataclasses import dataclass ,field


@dataclass
class Game:
    __turn: int = 1
    __score: int = 0
    __score_this_turn: int = 0
    __is_turn_over: bool = False
    __is_game_over: bool = False
    __die: Die = field(default_factory=Die)

    def play(self):
        while not self.__is_game_over:
            self.take_turn()

    def take_turn(self):
        print('TURN', self.__turn)
        self.__score_this_turn = 0
        self.__is_turn_over = False
        while not self.__is_turn_over:
            choice = input('Roll or Hold? (r/h)')
            if choice.lower() == 'r':
                self.roll_die()
            elif choice.lower() == 'h':
                self.hold_turn()
            else:
                print('Invalid input, check options.')

    def roll_die(self):
        self.__die.roll()
        print("Die: ", self.__die.getvalue())
        if self.__die.getvalue() == 1:
            self.__score_this_turn = 0
            self.__turn += 1
            self.__is_turn_over = True
            print("This turn is over, You get no score. \n")
        else:
            self.__score_this_turn += self.__die.getvalue()

    def hold_turn(self):
        self.__score += self.__score_this_turn
        self.__is_turn_over = True
        print("Score for turn: ", self.__score_this_turn)
        print("Total score: ", self.__score)
        if self.__score >= 20:
            self.__is_game_over = True
            print("You finished in", self.__turn, "turns!")
        else:
            self.__turn += 1
