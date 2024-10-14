from chicken import Chicken
from npc import NPC
from shop import Shop
import text

chicken = Chicken()


class Game:
    def __init__(self):
        self.player_name = None
        self.day = 0
        self.shopee = None
        self.inventory = {"Coins" : 100, "Corn" : 3, "Water" : 2}
        
    def update_player_name(self, name: str):
        self.player_name = name

    def get_player_name(self):
        return self.player_name

    def set_chicken_type(self, choice):
        chicken.set_type(choice)
        
    def get_chicken_type(self):
        return chicken.get_type()

    def set_chicken_name(self, chicken_type, chicken_name):
        chicken.set_type(chicken_type)
        chicken.set_name(chicken_name)
          
    def get_chicken_name(self):
        return chicken.get_name()

    def get_inventory(self):
        return self.inventory
        
    def add_inventory(self, item, quantity):
        if self.get_inventory().get(item.capitalize()) == None:
            self.inventory[item] = quantity
        else:
            self.inventory[item] += quantity

    def remove_from_inventory(self, item, quantity):
        self.inventory[item] -= quantity

    def create_shop(self):
        inventory = [40, 30, 20]
        price = [10, 20, 25]
        items = ["Water", "Chicken feed", "Corn" ]
        item_desc = ["Increase HP by 4", "Increase HP by 7", "Increase HP by 10"]
        self.shopee = Shop(inventory, price, items, item_desc)

    def get_shop(self):
        return self.shopee

    def shop(self):
        shop = self.get_shop()
        print(text.shop_message)
        print("\nRemember not to spend too much! If your coins remain negative at end of day 5, you lose :(")
        exit = False
        while not exit:
            print()
            print(f"\nYour coins: {self.get_inventory()["Coins"]}")
            print(text.shop_options, "\n")
            choice = input(text.ask_choice)
            while choice not in "123":
                choice = input("Invalid choice, input 1, 2 or 3: ")
            if choice == "1":
                shop.get_price_list()
            elif choice == "2":
                item, quantity, cost = shop.purchase_item()
                self.add_inventory(item, quantity)
                self.deduct_coins(cost)
                
            else:
                coins = self.get_inventory()["Coins"]
                if coins < 0:
                    print(f"\nYou have {coins} coins left. If coins remain negative at the end of the game, you lose! Be mindful of your spending !\n")
                else:
                    print(f"\nYou have {coins} coins left\n")
                exit = True

    def go_shop(self):
        if chicken.get_health() < 30:
            print("Chicken health is low remember to buy some food to replenish its health!")
        choice = input("You see a shop! Would you like to enter? Y/N: ")
        while choice.upper() not in "YN":
            choice = input("Invalid choice, " + text.ask_choice)
            
        if choice.upper() == "Y":
            self.shop()
    
    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day
        
    def day_is_over(self):
        pass

    def intro(self):
        print(f"====== DAY {self.day} ======")

    def prep_day(self):
        data = text.enemy_data[self.day - 1]
        npc = NPC(data["enemy_name"], data["enemy_health"], data["enemy_attacks"])
        return npc

    def deduct_coins(self, coins):
        self.inventory["Coins"] -= int(coins)

    def add_coins(self, coins):
        self.inventory["Coins"] += int(coins)
    
    def fight_is_over(self, npc):
        if npc.get_hp() <= 0:
            return True
        elif chicken.get_health() <= 0:
            return True
        return False

    def fight_over_message(self, npc):
        if npc.get_hp() <= 0:
            self.add_coins(50)
            print(f"You have beaten {npc.get_name()}!!")
            print("You get 50 coins for winning!\n")
        elif chicken.get_health() <= 0:
            self.deduct_coins(100)
            chicken.update_health(chicken.get_max_health())
            print("You have fainted :(")
            print("100 coins will be deducted for the defeat, try harder next time!\n")
        

    def enemy_beaten(self, npc):
        if self.fight_is_over(npc) and npc.get_hp() <= 0:
            return True
        else:
            return False

    def npc_attacks(self, npc, defence):
        attack_name, atk = npc.get_attack()
        print(f"{npc.get_name()} attacked you with {attack_name}!")
        if defence:
            atk -= defence
            print(f"Your defence has reduced your damage taken by {defence}.")
        print(f"Your health decreased from {chicken.get_health()} to {chicken.update_health(-atk)}.")
    
    def print_stats(self, npc):
        print(f"Your Strength: {chicken.strength}")
        print(f"Your Health: {chicken.health}")
        print(f"Enemy's Health: {npc.health}")

    def prompt_player(self):
        print("Moves available: ")
        for i in range(len(text.attack_list[self.day - 1])):
            print(f"{i+1}. {text.attack_list[self.day - 1][i]["name"]}")
        choice = input("Pick your move: ")
        while not 0 < int(choice) <= len(text.attack_list[self.day - 1]):
            print("Invalid choice")
            choice = input("Pick your move: ")
        return int(choice)

    def do(self, choice, npc):
        move = text.attack_list[self.day - 1][choice - 1]
        if move["atk"]:
            print(f"{npc.get_name()}'s health has decreased from {npc.get_hp()} to {npc.update_hp(move["atk"])}.\n")
        return move["def"]

    ###### TO CHANGE!!!!
    def debrief(self): 
        if chicken.get_health() < 30:
            print("Your chicken is on low health. Feed it some food or it might die tomorrow.")
            print(f"Your chicken's health: {chicken.get_health()} (Try to increase till at least (50 + day * 10) hp)")
        choice = input("Before the day ends, would you like to use items in your inventory? Y/N: ")
        while choice.upper() not in "YN":
            choice = input("Invalid choice, " + text.ask_choice)
        if choice.upper() == "Y":
            self.use_inventory()
            again = input("Would you like to use anything else? Y/N: ")
            while again.upper() not in "YN":
                again = input("Invalid. Input Y/N: ")
            while again.upper() == "Y":
                self.use_inventory()
                again = input("Would you like to use anything else? Y/N: ")
                while again.upper() not in "YN":
                    again = input("Invalid. Input Y/N: ")
                    
        print("Rest well !\n")

    def use_inventory(self):
        print("Your inventory:")
        print(self.get_inventory())
        item = input("Enter item you want to use: ").capitalize()
        while self.get_inventory().get(item) == None:
            item = input("Invalid item, enter again: ").capitalize()
        max = self.get_inventory()[item]
        quantity = input("Enter quantity: ")
        while not quantity.isdigit() or int(quantity) > max:
            quantity = input("Enter valid quantity: ")
        quantity = int(quantity)
        original_health = chicken.get_health()
        if item == "Corn":
            increase = 10 * quantity
            chicken.update_health(increase)
        elif item == "Chicken feed":
            increase = 7 * quantity
            chicken.update_health(increase)
        elif item == "Water":
            increase = 4* quantity
            chicken.update_health(increase)
        print(f"Your chicken's health increased from {original_health} to {original_health + increase}")
        self.remove_from_inventory(item, quantity)

    #ending - if coins -tve lose, coins +ve win!!
        
if __name__ == "__main__":
    game = Game()
    game.create_shop()
    game.shop()
