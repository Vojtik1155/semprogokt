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
    def is_standing(self):
        return self._health > 0

    def visual_pointer(self, current, maximum):
        full = 20
        amount = int(current  / maximum * full)
        if amount == 0 and self.is_standing():
            amount = 1
        return f'[{"#"*amount}{"-"*(full-amount)}]'
    def visual_health(self):
        return self.visual_pointer(self._health, self._max_health)


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


class Winger(Ship):
    """
    A different class, that adds energy for laser research. 
    It demonstrates a whole bunch of things... trust me on that.
    """

    def __init__(self, name, health, damage, shield, dice, energy, laser_attack):
        super().__init__(name, health, damage, shield, dice)
        self._energy = energy
        self._max_energy = energy
        self._laser_attack = laser_attack

    def attack(self, opponent):
        if self._energy < self._max_energy:
            self._energy = min(self._max_energy, self._energy + 25)
            super().attack(opponent)
        else:
            hit = self._laser_attack + self._dice.throw()
            self.set_message(f'{self._name} is using its laser to attack for {hit} hp.')
            self._energy = 0
            opponent.defend(hit)

    def visual_energy(self):
        return self.visual_pointer(self._energy, self._max_energy)



class Juggernaut(Ship):
    def defend(self, hit):
        damage_taken = hit - (self._shield + self._dice.throw() + 5)
        if damage_taken > 0:
            message = f'{self._name} got hit for {damage_taken} damage.'
            self._health -= damage_taken
            if self._health < 0:
                self._health = 0
                message = f'{message[:-1]} and was destroyed.'
        else:
            message = f'{self._name} defended the attack with their shield.'
        self.set_message(message)
