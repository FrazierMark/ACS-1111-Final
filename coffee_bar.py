class CoffeeBar(object):
    def __init__(self, Barista):
        self.order_list = []
        self.Barista = Barista
        self.register = 0
        self.cost = {
            "Coffee": 2.00,
            "Tea": 1.50,
            "Milk": 3.00
        }
        self.receipts = []
        self.tip_jar = 0
        
    def place_order(self, Order):
        self.order_list.append(Order)
        order_cost = self.cost[Order.drink_type] + (self.cost[Order.drink_type] * Order.person.tip)
        Order.person.wallet -= order_cost
        self.register += self.cost[Order.drink_type]
        self.tip_jar += (self.cost[Order.drink_type] * Order.person.tip)
        
    def process_orders(self):
        for order in self.order_list:
            print(f"{self.Barista.greeting} {order.to_string()}")
            
        self.receipts = self.order_list.copy()
        self.order_list = []
        
        self.Barista.wallet += self.tip_jar
            
    def cash_out(self):
        print(f"Amount in register: ${self.register}")