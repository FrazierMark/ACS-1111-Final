from order import Order

class Person(object):
    def __init__(self, name, favorite_drink, wallet=0, tip=0):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip = tip

    def my_order(self):
        return Order(self.favorite_drink, self)
    



