class Shop:
    def __init__(self, inventory, price, item, item_desc):
        self.inventory = inventory
        self.price = price
        self.item = item
        self.item_desc = item_desc

    def get_inventory(self):
        return self.inventory

    def get_item(self):
        return self.item
        
    def get_price(self):
        return self.price

    def get_item_desc(self):
        return self.item_desc
        
    def get_price_list(self):
        print()
        for i in range(len(self.get_inventory())):
            print(f"{self.get_item()[i] +" (" + self.get_item_desc()[i]+")":<40}: ${self.get_price()[i]}")
        print()
        
    def purchase_item(self):
        print()
        for i in range(len(self.get_item())):
            print(f"{i+1}. {self.get_item()[i]}")
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

    def update_inventory(self, purchase_number, quantity):
        self.inventory[int(purchase_number) - 1] -= int(quantity)


