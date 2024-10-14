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
