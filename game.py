from chicken import Chicken
from npc import NPC
from shop import Shop

colours = {"white": "\x1b[0m", "red": "\x1b[31m", "green": "\x1b[32m", "yellow":  "\x1b[33m", "blue": "\x1b[34m", "purple": "\x1b[35m"}

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
        
        print(f"\nYou, {self.name}, have been selected to enter the renowned {colours["red"]}King of Fighting Chickens Tournament!!!!!!{colours["white"]} You have to fight your way through ruthless, savage chickens to become the {colours["yellow"]}CHAMPION{colours["white"]}, where you will be crowned KING of the chickens, and earn a grand prize.\n")

    def choose_chicken(self):
        print("Sanders, please choose your chicken wisely: ")
        print(f"1. GMO Chicken \nThe model chicken. Perfectly well-balanced in every aspect, {colours["red"]}feisty and aggressive{colours["white"]}. Ready to murder any chickens for your love.\n")

        print(f"2. Organic Chicken: \nRaised with the {colours["green"]}greenest grass{colours["white"]}, {colours["blue"]}crystal clear water{colours["white"]}, and the best conditions all around. Tanky and right in the {colours["purple"]}pink of health{colours["white"]}. Could and would block a bullet for you.\n")

        chicken = Chicken()
        choice = input("Your choice: ")
        while choice not in "12":
            choice = input("Invalid choice, input 1 or 2: ")
        chicken.set_type(choice)

        print(f"\nCongratulations on receiving your one and only {chicken.get_type()} Chicken! What will their name be? \n")
        chicken_name = input("Your choice: ")
        chicken.set_name(chicken_name)

        print(f"\n{chicken.name} pecks your face with affection.\n\n")
        
        return chicken

    def set_day(self, day):
        self.day = day

