'''
create a simple class
'''

class CashRegister:
    global rate
    rate=.076

    def __init__(self):
        self.items = 0
        self.price = 0

    def update_register (self, price):
        self.items =self.items +1
        self.price =self.price+price

    def display_register(self):
        return print("the number of items ", self.items, '\n The total price without taxes', self.price, 'Rate for taxes', rate)

    def clear_register(self):
        CashRegister.final_price_tax
        self.items=0
        self.price=0

    def final_price_tax(self):
        self.price=(1+rate)*self.price
        return print('Price with taxes' , round(self.price, 2))


register1= CashRegister()
register1.update_register(100)
register1.update_register(2.65)
register1.update_register(38.89)

register1.display_register()
register1.clear_register()


# register1.display_register()
# register1.final_price_tax()
#



# register1 = CashRegister()
# register1.update_register(1.95)
# register1.update_register(.65)
# register1.update_register(25000)
# register1.display_register()
#
# register2= CashRegister()
# print('register 2')
# register2.display_register()
# register2.update_register(500)
# print(register2.price)
#
# register1.clear_register()
# register1.display_register()


def clear_register(self):
    CashRegister.final(self)