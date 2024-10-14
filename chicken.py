import gamedata


class Chicken:

    def __init__(self, name: str, type: str, health: int, strength: int):
        self.name = name
        self.type = type
        self.health = health
        self.max_health = health
        self.strength = strength
        self.attack = {}

    def update_attack(self, attack, damage):
        self.attack[attack] = damage

    def update_health(self, change):
        if self.health + change < 0:
            self.health = 0
        else:
            self.health += change
        return self.health

    def update_strength(self, change):
        self.strength += change

    def get_type(self):
        return self.type

    def get_strength(self):
        return self.strength

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.max_health

    def get_damage(self, attack):
        return self.attack[attack]


def create_chicken(chicken_type: str, chicken_name: str) -> Chicken:
    chickendata = gamedata.chicken[chicken_type]
    return Chicken(chicken_name, chickendata["type"], chickendata["health"], chickendata["strength"])

