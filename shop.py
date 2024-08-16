class Shop:
    def __init__(self, inventory, price, item):
        self.inventory = inventory
        self.price = price
        self.item = item

    def get_inventory(self):
        return self.inventory

    def get_item(self):
        return self.item
        
    def get_price(self):
        return self.price
        
    def get_price_list(self):
        print()
        for i in range(len(self.get_inventory())):
            print(f"{self.get_item()[i]:<15}: ${self.get_price()[i]}")
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
        
        while not quantity.isdigit() or not(1 <= int(quantity) <= int(self.get_inventory()[purchase_number])):
            print(f"Quantity left: {self.get_inventory()[purchase_number - 1]}")
            quantity = input('Enter valid quantity: ')

        quantity = int(quantity)
        self.update_inventory(purchase_number, quantity)

    def update_inventory(self, purchase_number, quantity):
        self.inventory[int(purchase_number) - 1] -= int(quantity)

if __name__ == "__main__": # to run go to shell and type python shop.py
    item = ["Coke", "Water", "Food"]
    inventory = [30, 40, 20]
    price = [2, 3, 4]
    shop = Shop(inventory, price, item)  
    shop.update_inventory(1, 10)  
    shop.get_price_list()
    shop.purchase_item()
    print(shop.get_inventory())