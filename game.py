from chicken import Chicken
from npc import NPC
from shop import Shop
import text

class Game:
    def __init__(self):
        self.name = None
        self.day = 0
        
    def update_player_name(self, name):
        self.name = name
        
    def welcome(self):
        print(text.welcome)
        name = input(text.askname)
        self.update_player_name(name)
        
        print(text.intro_d0)

    def choose_chicken(self):
        print("Sanders, please choose your chicken wisely: ")
        print("1. GMO Chicken \nThe model chicken. Perfectly well-balanced in every aspect, feisty and aggressive. Ready to murder any chickens for your love.\n")

        print("2. Organic Chicken: \nRaised with the greenest grass, crystal clear water, and the best conditions all around. Tanky and right in the pink of health. Could and would block a bullet for you.\n")

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

