from chicken import Chicken
from npc import NPC
from shop import Shop
import text

chicken = Chicken()

class Game:
    def __init__(self):
        self.name = None
        self.day = 0
        self.shopee = None
        
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

    def set_chicken_type(self, choice):
        chicken.set_type(choice)

    def set_chicken_name(self, chicken_name):
        chicken.set_name(chicken_name)

        print(f"\n{chicken.name} pecks your face with affection.\n\n")
        
        return chicken

    def create_shop(self):
        inventory = [40, 30, 20]
        price = [1, 4, 7]
        items = ["Water", "Chicken feed", "Corn" ]
        self.shopee = Shop(inventory, price, items)

    def get_shop(self):
        return self.shopee
        
    def shop(self):
        shop = self.get_shop()
        print(text.shop_message)
        exit = False
        while not exit:
            print()
            print(text.shop_options)
            print()
            choice = input(text.ask_choice)
            while choice not in "123":
                choice = input("Invalid choice, input 1, 2 or 3: ")
            if choice == "1":
                shop.get_price_list()
            elif choice == "2":
                shop.purchase_item()
            else:
                exit = True
        
    def set_day(self, day):
        self.day = day

    def day_is_over(self):
        pass

    def intro(self):
        print(text.intros[self.day - 1].format(chicken.name))

if __name__ == "__main__":
    game = Game()
    game.create_shop()
    game.shop()