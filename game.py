class Chicken:

    def __init__(self):
        self.name = ""
        self.type = None
        self.health = None
        self.strength = None
        self.attack = {}

    def set_type(self, type):
        if type == "1":
            self.type = "GMO"
            self.health = 60
            self.strength = 40
        else:
            self.type = "Organic"
            self.health = 50
            self.strength = 50

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def update_attack(self, attack, damage):
        self.attack[attack] = damage

    def update_health(self, change):
        self.health += change

    def update_strength(self, change):
        self.strength += change

    def get_type(self):
        return self.type

    def get_strength(self):
        return self.strength

    def get_health(self):
        return self.health

    def get_damage(self, attack):
        return self.attack[attack]


class Npc:
    pass


class Shop:
    pass


class Game:
    def __init__(self):
        self.name = None
        self.day = 0
        
    def update_player_name(self, name):
        self.name = name
        
    def welcome(self):
        print("Welcome to KFC!\n")
        name = input("State your name: ")
        self.update_player_name(name)
        
        print("\nYou, Harland, have been selected to enter the renowned King of Fighting Chickens Tournament!!!!!! You have to fight your way through ruthless, savage chickens to become the CHAMPION, where you will be crowned KING of the chickens, and earn a grand prize.\n")

    def choose_chicken(self):
        print("Sanders, please choose your chicken wisely: ")
        print("1. GMO Chicken \nThe model chicken. Perfectly well-balanced in every aspect, feisty and aggressive. Ready to murder any chickens for your love.\n\n")

        print("2. Organic Chicken: \nRaised with very green grass, crystal clear water, and the best conditions all around. Tanky and right in the pink of health. Could and would block a bullet for you.\n")

        chicken = Chicken()
        choice = input("Your choice: ")
        while choice not in "12":
            choice = input("Invalid choice, reinput: ")
        chicken.set_type(choice)

        print(f"\nCongratulations on receiving your one and only {chicken.get_type()} Chicken! What will their name be? \n")
        chicken_name = input("Your choice: ")

        print(f"\n{chicken_name} pecks your face in affection.\n\n")
        
        return chicken

    def set_day(self, day):
        self.day = day

