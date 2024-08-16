import random
from typing import Tuple

class NPC:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> Tuple[str, int]:
        crit = random.choice([True, False])
        name = random.choice(list(self.attacks.keys()))
        if crit:
            dmg = int(1.2*self.attacks[name])
        else:
            dmg = self.attacks[name]
        return (name, dmg)

    def get_hp(self):
        return self.health

    def update_hp(self, change) -> int:
        self.health = self.health - change
        return self.health
