import random
from typing import Tuple

from combat import Attack, Combatant
import gamedata


class Enemy(Combatant):

    def __init__(self, name: str, health: int, attacks: list[dict]):
        super().__init__(name, health)
        self.attacks = [
            Attack(attack["attack_name"], attack["atk"], attack["def"])
            for attack in attacks
        ]

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> Tuple[str, int]:
        attack_index = random.randint(0, len(self.attacks) - 1)
        name = self.attacks[attack_index].name
        dmg = self.attacks[attack_index].attack
        return (name, dmg)

    def get_hp(self):
        return self.health

    def update_hp(self, change) -> int:
        if change < self.health:
            self.health -= change
        else:
            self.health = 0
        return self.health


def create_enemy(day_label: str) -> Enemy:
    enemydata = gamedata.enemies[day_label]
    return Enemy(enemydata["enemy_name"], enemydata["enemy_health"], enemydata["enemy_attacks"])
