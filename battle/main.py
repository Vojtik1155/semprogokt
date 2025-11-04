#!/usr/bin/env python3

from dice import Dice 
from ship import Ship

class Sector:
    '''
    Two ships dukin' it out.
    '''

    def __init__(self, ship_1, ship_2, dice, name='noname'):
        self._name = name
        self._ship_1 = ship_1
        self._ship_2 = ship_2
        self._dice = dice

    def _clean(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

    def _write_ship(self, ship):
        print(ship) 
        print(f'Health: {ship._health}\n')

    def _draw(self):
        self._clean()
        print(f'====================== The {self._name} Sector ======================')
        print('Ships:\n')
        self._write_ship(self._ship_1)
        self._write_ship(self._ship_2)
        print()

    def war(self):
        print(f"Welcome to the {self._name} sector.")
        print("==============================================================")
        print()
        print(f"Today, these ship swill go at it crazy style:\n")
        self._write_ship(self._ship_1)
        self._write_ship(self._ship_2)
        print("Press [ENTER] to begin...")
        input()
        
        import random
        if random.randint(0, 1):
            self._ship_1, self._ship_2 = self._ship_2, self._ship_1

        while self._ship_1.is_standing() and self._ship_2.is_standing():
            self._ship_1.attack(self._ship_2)
            self._draw()
            self._send_message(self._ship_1.send_message())
            self._send_message(self._ship_2.send_message())

            if self._ship_2.is_standing():
                self._ship_2.attack(self._ship_1)
                self._draw()
                self._send_message(self._ship_2.send_message())
                self._send_message(self._ship_1.send_message())

    def _send_message(self, message):
        import time as _time
        if message:
            print(message)
            _time.sleep(0.8)

if __name__ == '__main__':
    d = Dice(10)
    shippy = Ship("Big D. Randy", 67, 80, 15, d)
    pod = Ship("You", 420, 20, 20, d)
    boi = Ship("You again", 420, 20, 20, d)

    bluff = Sector(shippy, pod, d, "Bluff")
    gamma = Sector(shippy, boi, d, "Gamma")

    bluff.war()
    gamma.war()