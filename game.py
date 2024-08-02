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
        

class Npc:
    pass

class Shop:
    pass

class Game:
    pass