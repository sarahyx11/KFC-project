import random

from combat import Attack, Combatant
import gamedata


class Enemy(Combatant):

    def __init__(self, name: str, health: int, attacks: list[dict]):
        super().__init__(name, health)
        self.attacks = [
            Attack(attack["attack_name"], attack["atk"], attack["def"])
            for attack in attacks
        ]

    def get_attack(self) -> Attack:
        return random.choice(self.attacks)


def create_enemy(day_label: str) -> Enemy:
    enemydata = gamedata.enemies[day_label]
    return Enemy(enemydata["enemy_name"], enemydata["enemy_health"], enemydata["enemy_attacks"])
