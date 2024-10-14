import random
from typing import Tuple

import gamedata


class Attack:

    def __init__(self, name: str, attack: int, defence: int):
        self.name = name
        self.attack = attack
        self.defence = defence


class EnemyAttack:

    def __init__(self, name: str, attack: int):
        self.name = name
        self.attack = attack


class Enemy:

    def __init__(self, name: str, health: int, attacks: list[dict]):
        self.name = name
        self.health = health
        self.attacks = [
            EnemyAttack(attack["attack_name"], attack["atk"])
            for attack in attacks
        ]

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> Tuple[str, int]:
        attack_index = random.randint(0, len(self.attacks) - 1)
        name = self.attacks[attack_index]["attack_name"]
        dmg = self.attacks[attack_index]["atk"]
        return (name, dmg)

    def get_hp(self):
        return self.health

    def update_hp(self, change) -> int:
        if change < self.health:
            self.health -= change
        else:
            self.health = 0
        return self.health


def create_attack(day_label: str) -> Attack:
    attackdata = gamedata.attacks[day_label]
    return Attack(attackdata["attack_name"], attackdata["atk"], attackdata["def"])

def create_enemy(day_label: str) -> Enemy:
    enemydata = gamedata[day_label]
    return Enemy(enemydata["enemy_name"], enemydata["enemy_health"], enemydata["enemy_attacks"])
