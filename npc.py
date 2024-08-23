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
        attack_index = random.randint(0, len(self.attacks)-1)
        name = self.attacks[attack_index]["attack_name"]
        dmg = self.attacks[attack_index]["atk"]
        return (name, dmg)

    def get_hp(self):
        return self.health

    def update_hp(self, change) -> int:
        if change < self.health:
            self.health = self.health - change
        else:
            self.health = 0
        return self.health
