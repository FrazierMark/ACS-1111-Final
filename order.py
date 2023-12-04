

class Order(object):
    def __init__(self, drink_type, person):
        self.drink_type = drink_type
        self.person = person
        
    def to_string (self):
        return f"{self.person.name} orders: {self.drink_type}"
    