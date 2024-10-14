class Chicken:

    def __init__(self):
        self.name = ""
        self.type = None
        self.health = None
        self.max_health = None
        self.strength = None
        self.attack = {}

    def set_type(self, type):
        if type == "1":
            self.type = "GMO"
            self.health = 60
            self.max_health = self.health
            self.strength = 40
        else:
            self.type = "Organic"
            self.health = 50
            self.max_health = self.health
            self.strength = 50

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

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
