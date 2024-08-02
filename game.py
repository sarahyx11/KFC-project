import random
from typing import Tuple

class Chicken:
    def __init__(self):
        self.name = ""
        self.type = None
        self.health = None
        self.strength = None
        self.attack = []

    def set_type(self, type):
        if type == "Organic":
            self.type = "Organic"
            self.health = 60
            self.strength = 40
        else:
            self.type = "GMO"
            self.health = 50
            self.strength = 50

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def update_attack(self, attack, damage):
        pass


class NPC:
    def __init__(self, health, attacks, name):
        self.health = health
        self.attacks = {}
        self.name = name

    def set_attack(self, atk_name, dmg) -> None:
        self.attacks.update({atk_name: dmg})

    def get_attack(self) -> Tuple[str, int]:
        crit = random.choice([True, False])
        name = random.choice(list(self.attacks.keys()))
        if crit:
            dmg = int(1.2*self.attacks[name])
        else:
            dmg = self.attacks[name]
        return (name, dmg)

    def update_hp(self, change) -> None:
        self.health = self.health - change

    def get_name(self) -> str:
        return self.name

class Shop:
    pass

class Game:
    pass