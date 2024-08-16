from chicken import Chicken
from npc import NPC
from shop import Shop
import text

chicken = Chicken()

class Game:
    def __init__(self):
        self.name = None
        self.day = 0
        
    def update_player_name(self, name):
        self.name = name

    def get_player_name(self):
        return self.name
        
    def welcome(self):
        print(text.welcome)
        name = input(text.askname)
        self.update_player_name(name)
        
        print(text.welcome_intro.format(self.name))

    def choose_chicken(self):
        print(text.chicken_reminder.format(self.get_player_name()))
        print(text.gmo_desc)

        print(text.organic_desc)

        choice = input(text.ask_choice)
        while choice not in "12":
            choice = input("Invalid choice, input 1 or 2: ")
        self.set_chicken_type(choice)

        print(f"\nCongratulations on receiving your one and only {chicken.get_type()} Chicken! What will their name be? \n")
        chicken_name = input(text.ask_choice)
        self.set_chicken_name(chicken_name)
        print(f"\n{chicken.name} pecks your face with affection.\n\n")

    def set_chicken_type(self, choice):
        chicken.set_type(choice)
       
        
    def get_chicken_type(self):
        return chicken.get_type()

    def set_chicken_name(self, chicken_name):
        chicken.set_name(chicken_name)
          
    def get_chicken_name(self):
        return chicken.get_name()
        
    

    def set_day(self, day):
        self.day = day
######### NOT DONE PLS DO THANKS IDK HOW TO
    def day_is_over(self):
        pass

    def intro(self):
        print(f"====== DAY {self.day} ======")
        print(text.intros[self.day - 1].format(chicken.name))

    def prep_day(self):
        data = text.enemy_data[self.day - 1]
        npc = NPC(data["enemy_name"], data["enemy_health"], data["enemy_attacks"])
        return npc
        
    def print_stats(self, npc):
        print(f"Your Strength: {chicken.strength}")
        print(f"Your Health: {chicken.health}")
        print(f"Enemy's Health: {npc.health}\n")

    def prompt_player(self):
        print("Moves available: ")
        for num, move in enumerate(text.attack_list[self.day - 1]):
            print(f"{num+1}. {move}")
        choice = input("Pick your move: ")
        while not 0 < int(choice) <= len(text.attack_list[self.day - 1]):
            print("Invalid choice")
            choice = input("Pick your move: ")
        return choice

    def do(self, choice):
        pass