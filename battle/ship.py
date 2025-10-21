#!/usr/bin/env python3

'''
Ships and their classes for the battle.
'''

class Ship:
    '''
    Basic class representing ships.
    '''

    def __init__(self, name, health, damage, shield, dice):
        self._name = name
        self._health = health
        self._max_health = health
        self._damage = damage
        self._shield = shield
        self._dice = dice
        self._message = ''

    def __str__(self):
        return str(self._name)

    def attack(self, opponent):
        hit = self._damage + self._dice.throw()
        message = f'{self._name} is dealing {hit} damage.'
        self.set_message(message)
        opponent.defend(hit)

    def defend(self, hit):
        damage_taken = hit - (self._shield + self._dice.throw())
        if damage_taken > 0:
            message = f'{self._name} got hit for {damage_taken} damage.'
            self._health -= damage_taken
            if self._health < 0:
                self._health = 0
                message = f'{message[:-1]} and was destroyed.'
        else:
            message = f'{self._name} defended the attack with their shield.'
        self.set_message(message)
    def set_message(self, message):
        self._message = message

    def send_message(self):
        return self._message