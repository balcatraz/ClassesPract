import random


class Insect:
    def __init__(self, w=2, l=4):
        self.__wings = w
        self.__legs = l
        self.__lof = 0

    def fly(self):
        self.__lof = random.randint(1, 10)

    def get_lof(self):
        return self.__lof
