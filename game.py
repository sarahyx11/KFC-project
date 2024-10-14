import chicken
import gamedata
from npc import NPC
from shop import Shop
import text

class Game:
    def __init__(self):
        self.chicken = None
        self.player_name = None
        self.day = 0
        self.shopee = None
        self.inventory = gamedata.inventory.copy()
        
    def update_player_name(self, name: str):
        self.player_name = name

    def get_player_name(self):
        return self.player_name

    def set_chicken(self, chicken_type: str, chicken_name: str) -> None:
        self.chicken = chicken.create_chicken(chicken_type, chicken_name)

    def get_inventory(self):
        return self.inventory
        
    def add_inventory(self, item: str, quantity: int) -> None:
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

    def get_shop(self) -> Shop:
        return self.shopee

    def shop(self):
        shop = self.get_shop()
        print(text.shop_message)
        print("\nRemember not to spend too much! If your coins remain negative at end of day 5, you lose :(")
        exit = False
        while not exit:
            print()
            print(f"\nYour coins: {self.get_inventory()["Coins"]}")
            choice = text.prompt_valid_choice(
                options=text.shop_options,
                prompt=text.shop_message + "\n" + text.coin_reminder
            )
            if choice == "Check price list":
                shop.display_price_list()
            elif choice == "Buy item":
                item_name = text.prompt_valid_choice(
                    options=list(self.inventory),
                    prompt="Which item do you want to buy?"
                )
                quantity = text.prompt_valid_range(
                    start=0,
                    end=shop.inventory[item_name],
                    prompt="How many?"
                )
                cost = shop.purchase(item_name, quantity)
                self.add_inventory(item_name, quantity)
                self.deduct_coins(cost)
            else:
                coins = self.get_inventory()["Coins"]
                if coins < 0:
                    print(f"\nYou have {coins} coins left. If coins remain negative at the end of the game, you lose! Be mindful of your spending !\n")
                else:
                    print(f"\nYou have {coins} coins left\n")
                exit = True

    def go_shop(self):
        if self.chicken.get_health() < 30:
            print("Chicken health is low remember to buy some food to replenish its health!")
        choice = text.prompt_y_or_n("You see a shop! Would you like to enter?")
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
        elif self.chicken.get_health() <= 0:
            return True
        return False

    def fight_over_message(self, npc):
        if npc.get_hp() <= 0:
            self.add_coins(50)
            print(f"You have beaten {npc.get_name()}!!")
            print("You get 50 coins for winning!\n")
        elif self.chicken.get_health() <= 0:
            self.deduct_coins(100)
            self.chicken.update_health(self.chicken.get_max_health())
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
        print(f"Your health decreased from {self.chicken.get_health()} to {self.chicken.update_health(-atk)}.")
    
    def print_stats(self, npc):
        print(f"Your Strength: {self.chicken.strength}")
        print(f"Your Health: {self.chicken.health}")
        print(f"Enemy's Health: {npc.health}")

    def prompt_player(self) -> str:
        attack_names = [attk["name"] for attk in text.attack_list[self.day - 1]]
        choice = text.prompt_valid_choice(
            options=attack_names,
            prompt="Moves available: "
        )
        return choice

    def do(self, choice: str, npc):
        # FIX: fix to treat choice as move name
        move = text.attack_list[self.day - 1][choice - 1]
        if move["atk"]:
            print(f"{npc.get_name()}'s health has decreased from {npc.get_hp()} to {npc.update_hp(move["atk"])}.\n")
        return move["def"]

    ###### TO CHANGE!!!!
    def debrief(self): 
        if self.chicken.get_health() < 30:
            print("Your chicken is on low health. Feed it some food or it might die tomorrow.")
            print(f"Your chicken's health: {self.chicken.get_health()} (Try to increase till at least (50 + day * 10) hp)")
        choice = text.prompt_y_or_n("Before the day ends, would you like to use items in your inventory?")
        if choice.upper() == "Y":
            self.use_inventory()
            again = text.prompt_y_or_n("Would you like to use anything else?")
            while again.upper() == "Y":
                self.use_inventory()
                again = text.prompt_y_or_n("Would you like to use anything else?")
        print("Rest well !\n")

    def use_inventory(self):
        options = [f"{item} ({count})" for item, count in self.inventory.items()]
        choice = text.prompt_valid_choice(
            options=options,
            prompt="Use an item from your inventory:"
        )
        quantity = text.prompt_valid_range(
            start=0, end=self.inventory[choice],
            prompt="Use how many?"
        )
        original_health = self.chicken.get_health()
        if choice == "Corn":
            increase = 10 * quantity
            self.chicken.update_health(increase)
        elif choice == "Chicken feed":
            increase = 7 * quantity
            self.chicken.update_health(increase)
        elif item == "Water":
            increase = 4 * quantity
            self.chicken.update_health(increase)
        print(f"Your chicken's health increased from {original_health} to {original_health + increase}")
        self.remove_from_inventory(item, quantity)

    #ending - if coins -tve lose, coins +ve win!!
        
if __name__ == "__main__":
    game = Game()
    game.create_shop()
    game.shop()
