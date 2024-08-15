class Shop:
    def __init__(self, inventory, price):
        self.inventory = inventory
        self.price = price

    def get_inventory(self):
        return self.inventory

    def get_item_price(self):
        print('Check price')
        selected_item = input('Enter item number:')
        item_price = price[int(selected_item) - 1]
        return f' The price is {item_price} price'

    def purchase_item(self):
        purchase_number = input('Enter item number:')
        quantity = input('Enter quantity:')
        return (int(quantity) * int(purchase_number))

    def update_inventory(self, purchase_number, quantity):
        self.inventory[int(purchase_number) - 1] -= int(quantity)

if __name__ == "__main__": # to run go to shell and type python shop.py
    inventory = [40, 30, 20]  
    price = [2, 3, 4]
    item = {1:'Coke',
            2: 'Chicken food',
            3: 'Corn'}
    shop = Shop(inventory, price)  
    shop.update_inventory(1, 10)  
    print(shop.get_inventory())