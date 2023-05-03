# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    item = None
    quantity = None
    price = None
    item_to_remove = None
    grocery_dict={}
    '''
        {
            grocery_item : {
                quantity: int,
                price: float
            }
        }
    '''
    def driver(self):
        shopping = True
        while shopping:
#         user option for add, removing showing or quit
            res = input("Would you like to add/remove/show/quit?: ").lower()
#         handle add
            if res == 'add':
                self.item = input('What item are you adding?').lower()
                while True:
                    self.quantity = input(f"How many {self.item} would you like to add?: ")
                    if self.quantity.isdigit():
                        self.quantity = int(self.quantity)
                        break
                    else:
                        print('Please enter quantity in digits')
                while True:
                    try:
                        self.price = float(input(f'How much does {self.item} cost?: '))
                        self.add()
                        break
                    except:
                        print('Please enter price in digits')
             
            if res == 'remove':
                self.item_to_remove = input('What item would you like to remove?: ').lower()
                while True:
                    try:
                        self.quantity = int(input('How many would you like to remove?: '))
                        self.remove()
                        break
                    except:
                        print('Please enter quantity in digits!')
            if res == 'show':
                self.show()
            if res == 'total':
                self.total()
            if res == 'quit':
                shopping = False
            
    
    def add(self):
        if self.item in self.grocery_dict:
            pass
        else:
            self.grocery_dict[self.item] = {
                'quantity' : self.quantity,
                'price' : self.price
            }
        self.show()
    
    def remove(self):
        if self.item_to_remove in self.grocery_dict:
            self.grocery_dict[self.item_to_remove]['quantity'] -= self.quantity
            if self.grocery_dict[self.item_to_remove]['quantity'] < 1:
                self.grocery_dict.pop(self.item_to_remove)
        else:
            print("Item not in list")
        self.show()
    def total(self):
        total = 0
        for value in self.grocery_dict.values():
            total += value['quantity'] * value['price']
        print(f'Total: {total}')
        return total
    
    def show(self):
        print(self.grocery_dict)
        
# my = Cart()
# my.driver()