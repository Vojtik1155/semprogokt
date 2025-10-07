#!/usr/bin/env python3

import random

class Dice:
    def __init__(self, side_amount = 6):
        self.__side_amount = side_amount

    def hod(self):
        return random.randint(1,self.__side_amount)
    def __str__(self):
        return f'This is a dice with {self.__side_amount} sides.'

    def getSide_amount(self):
        return self.__side_amount
        
def main():
    d1 = Dice()
    d2 = Dice(120)
    print(d1.throw())
    print(d2.throw())

if __name__ == '__main__':
    main()
