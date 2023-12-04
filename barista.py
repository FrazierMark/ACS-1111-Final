from person import Person

class Barista(Person):
    def __init__(self, name, greeting):
        super().__init__(name, greeting)
        self.name = name
        self.greeting = greeting
        