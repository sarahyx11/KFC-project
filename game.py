import chicken
import combat
import gamedata
import npc
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

    # def get_player_name(self):
    #     return self.player_name

    def set_chicken(self, chicken_type: str, chicken_name: str) -> None:
        self.chicken = chicken.create_chicken(chicken_type, chicken_name)

    # def get_inventory(self):
    #     return self.inventory
        
    def add_inventory(self, item: str, quantity: int) -> None:
        if self.inventory.get(item.capitalize()) == None:
            self.inventory[item] = quantity
        else:
            self.inventory[item] += quantity

    def remove_from_inventory(self, item, quantity):
        self.inventory[item] -= quantity

    def create_shop(self):
        self.shopee = Shop(gamedata.shop.copy())

    def get_shop(self) -> Shop:
        return self.shopee

    def shop(self):
        shop = self.get_shop()
        print(text.shop_message)
        print("\nRemember not to spend too much! If your coins remain negative at end of day 5, you lose :(")
        exit = False
        while not exit:
            print()
            print(f"\nYour coins: {self.inventory["Coins"]}")
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
                coins = self.inventory["Coins"]
                if coins < 0:
                    print(f"\nYou have {coins} coins left. If coins remain negative at the end of the game, you lose! Be mindful of your spending !\n")
                else:
                    print(f"\nYou have {coins} coins left\n")
                exit = True

    def go_shop(self):
        if self.chicken.is_low_health():
            print("Chicken health is low remember to buy some food to replenish its health!")
        choice = text.prompt_y_or_n("You see a shop! Would you like to enter?")
        if choice.upper() == "Y":
            self.shop()
    
    def set_day(self, day):
        self.day = day
        
    # def day_is_over(self):
    #     pass

    def intro(self):
        print(f"====== DAY {self.day} ======")

    def create_enemy_of_the_day(self):
        day_label = f"day{self.day}"
        return npc.create_enemy(day_label)

    def deduct_coins(self, coins):
        self.inventory["Coins"] -= int(coins)

    def add_coins(self, coins):
        self.inventory["Coins"] += int(coins)
    
    def fight_is_over(self, npc):
        if npc.is_dead():
            return True
        elif self.chicken.is_dead():
            return True
        return False

    def execute_attack(self, attacker: combat.Combatant, defender: combat.Combatant, move: npc.Attack) -> dict:
        """Execute an attack using the given move.
        Return an attack report in dict form.
        """
        damage_taken = defender.take_damage(move.attack)
        attacker. boost_defence(move.defence)
        defender.reset_defence()
        return {
            "attacker_name": attacker. name,
            "attacker_hp": attacker.hp,
            "defender_name": defender.name,
            "defender_hp": defender.hp,
            "move_name": move.name,
            "damage_taken": damage_taken
        }

    def fight_over_message(self, npc):
        if npc.is_dead():
            self.add_coins(50)
            print(f"You have beaten {npc.get_name()}!!")
            print("You get 50 coins for winning!\n")
        elif self.chicken.is_dead():
            self.deduct_coins(100)
            self.chicken.full_heal()
            print("You have fainted :(")
            print("100 coins will be deducted for the defeat, try harder next time!\n")

    def enemy_beaten(self, npc):
        if self.fight_is_over(npc) and npc.is_dead():
            return True
        else:
            return False

    def npc_attacks(self, npc):
        attack = npc.get_attack()
        report = self.execute_attack(npc, self.chicken, attack)
        print(
            text.attack_report(report)
        )
    
    def print_stats(self, npc):
        print(f"Your Strength: {self.chicken.strength}")
        print(f"Your Health: {self.chicken.health}")
        print(f"Enemy's Health: {npc.health}")

    def prompt_player(self) -> str:
        day_label = f"day{self.day}"
        attack_names = list(gamedata.attacks[day_label].keys())
        choice = text.prompt_valid_choice(
            options=attack_names,
            prompt="Moves available: "
        )
        return choice

    def do(self, choice: str, npc):
        day_label = f"day{self.day}"
        attackdata = gamedata.attacks[day_label][choice]
        move = combat.create_attack(attackdata)
        report = self.execute_attack(self.chicken, npc, move)
        print(
            text.attack_report(report)
        )

    ###### TO CHANGE!!!!
    def debrief(self): 
        if self.chicken.is_low_health():
            print("Your chicken is on low health. Feed it some food or it might die tomorrow.")
            print(f"Your chicken's health: {self.chicken.hp} (Try to increase till at least (50 + day * 10) hp)")
        choice = text.prompt_y_or_n("Before the day ends, would you like to use items in your inventory?")
        while choice.upper() == "Y":
            self.use_inventory()
            choice = text.prompt_y_or_n("Would you like to use anything else?")
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
        item = shop.create_item(choice)
        self.chicken.heal(item.effect * quantity)
        print(f"Your chicken's health: {self.chicken.hp} HP")
        self.remove_from_inventory(item, quantity)

    #ending - if coins -tve lose, coins +ve win!!
        
if __name__ == "__main__":
    game = Game()
    game.create_shop()
    game.shop()
