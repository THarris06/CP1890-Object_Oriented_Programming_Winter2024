# The changed class is in Inherit_basics look for __str__ and __eq__ methods.
# from Inherit_basics import Product
#
# product1 = Product('Stanley hammer', 5.489, 10)
# print(str(product1))
# print()
# # print(dir(product1))
#
# product2 = Product('Stanley hammer', 6.00, 20)
# print(product1 == product2)
# from dataclasses import dataclass
# import random
#
#
# @dataclass
# class Die:
#     __value: int = 1
#
#     def getvalue(self):
#         return self.__value
#
#     def roll(self):
#         self.__value = random.randint(1, 6)
#
#
# class Dice:
#     def __init__(self):
#         self.__list_die: list = []
#
#     def getlist(self):
#         return self.__list_die
#
#     def add_die(self, die):
#         self.__list_die.append(die)
#
#     def roll_all(self):
#         for die in self.__list_die:
#             die.roll()
#
#     @property
#     def list_dice(self) -> list:
#         return self.__list_die
#
#     def __iter__(self):
#         for Die in self.__list_die:
#             yield str(die)
#
#
# dice = Dice()
# dice.add_die(Die(6))
# dice.add_die(Die(4))
# dice.add_die(Die(3))
#
# for die in dice:
#     die.roll()
#     print(str(die))

from Subclass_matt import CustomRequestError


def read_movie():
    try:
        movie = []
        with open('movie.csv') as file_movie:
            pass
    except FileNotFoundError:
        raise CustomRequestError('This is my error')
    except Exception:
        raise CustomRequestError('This is my generic error')


try:
    movie = read_movie()
except CustomRequestError as e:
    print("CustomRequestError", e)
