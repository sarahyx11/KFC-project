import gamedata


class Item:
    def __init__(self, name, description, price, effect):
        self.name = name
        self.description = description
        self.price = price
        self.effect = effect


def create_item(name: str) -> Item:
    itemdata = gamedata.items[name]
    return Item(itemdata["name"], itemdata["description"], itemdata["price"], itemdata["effect"])


class Shop:
    def __init__(self, inventory: dict[str, int]):
        # inventory is a dict of item names and their quantity
        self.inventory = inventory

    def get_inventory(self) -> list[int]:
        return list[self.inventory.values()]

    def get_item(self) -> list[str]:
        return self.item
        
    def get_price(self) -> list[int]:
        return [
            gamedata.items["item"]["price"]
            for item in self.inventory
        ]

    def get_item_desc(self) -> list[str]:
        return [
            gamedata.items["item"]["description"]
            for item in self.inventory
        ]

    def purchase(self, item: str, quantity: int) -> int:
        """Remove quantity of item from inventory and return the cost of inventory"""
        if item not in self.inventory:
            raise ValueError(f"Item {item} not in inventory")
        if self.inventory[item] < quantity:
            raise ValueError(f"Not enough {item} in inventory")
        self.inventory[item] -= quantity
        return self.inventory[item] * gamedata.items[item]["price"]
        
    def display_price_list(self) -> None:
        """Display item name, description, and price"""
        print()
        for item_name in self.inventory:
            itemdata = gamedata.items[item_name]
            name, desc, price = itemdata["name"], itemdata["description"], itemdata["price"]
            print(f"{f"{name}({desc})":<40}: ${price}")
        print()
        
    def purchase_item(self) -> None:
        print()
        for i, item_name in enumerate(self.inventory, start=1):
            print(f"{i}. {item_name}")
        purchase_number = input('\nEnter item number: ')
        
        while not purchase_number.isdigit() or not (1 <= int(purchase_number) <= len(self.get_item())):
            purchase_number = input('Enter valid item number: ')
            
        purchase_number = int(purchase_number)
        quantity = input('Enter quantity: ')
        
        while not quantity.isdigit() or not(1 <= int(quantity) <= int(self.get_inventory()[purchase_number - 1])):
            print(f"Quantity left: {self.get_inventory()[purchase_number - 1]}")
            quantity = input('Enter valid quantity: ')

        quantity = int(quantity)
        self.update_inventory(purchase_number, quantity)
        
        return self.get_item()[purchase_number - 1], quantity, self.get_price()[purchase_number - 1] * quantity

    def update_inventory(self, purchase_number: str, quantity: str) -> None:
        if purchase_number == '1':
            item_name = "Water"
        elif purchase_number == '2':
            item_name = "Chicken feed"
        elif purchase_number == '3':
            item_name = "Corn"
        else:
            raise ValueError("Invalid item number")
        self.inventory[item_name] -= int(quantity)


