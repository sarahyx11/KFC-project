import random
from typing import Tuple

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
