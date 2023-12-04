from order import Order
from coffee_bar import CoffeeBar
from person import Person
from barista import Barista

amy = Person("Amy", "Coffee", 20.21, .20)
bob = Person("Bob", "Tea", 54.23, .18)
cat = Person("Cat", "Milk", 102.8, .15)
print(cat.wallet) # 102.8

kevin = Barista("Kevin", "Hey, dude!")
best_coffee_bar = CoffeeBar(kevin)

best_coffee_bar.place_order(amy.my_order())
best_coffee_bar.place_order(bob.my_order())
best_coffee_bar.place_order(cat.my_order())
best_coffee_bar.process_orders()

print(cat.wallet) # 99.35
print(kevin.wallet) # 1.12
best_coffee_bar.cash_out() # Amount in register: 6.5