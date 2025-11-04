#!/usr/bin/env python3

from dice import Dice 
from ship import Ship

class Sector:
    '''
    Two ships dukin' it out.
    '''

    def __init__(self, ship_1, ship_2, dice):
        self._ship_1 = ship_1
        self._ship_2 = ship_2
        self._dice = dice

    def war(self):
        print("Welcome to the Bluff sector.")
        print("============================")
        print()
        print(f"Today, the ships called {self._ship_1} and {self._ship_2} will go at it crazy style.")
        print("Press [ENTER] to begin...")
        input()

        while self._ship_1.is_standing() and self._ship_2.is_standing():
            self._ship_1.attack(self._ship_2)
            self._send_message(self._ship_1.send_message())
            self._send_message(self._ship_2.send_message())

            if self._ship_2.is_standing():
                self._ship_2.attack(self._ship_1)
                self._send_message(self._ship_2.send_message())
                self._send_message(self._ship_1.send_message())

    def _send_message(self, message):
        print(message)


if __name__ == '__main__':
    d = Dice(10)
    shippy = Ship("Big D. Randy", 100, 80, 50, d)
    pod = Ship("You", 40, 20, 30, d)
    bluff = Sector(shippy, pod, d)

    bluff.war()