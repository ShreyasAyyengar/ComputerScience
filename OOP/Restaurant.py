class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def open(self):
        print(f"Our restaurant {self.name} is open!")

    def describe_restaurant(self):
        print("-----------------------")
        print(f"This resturant is called {self.name} and offers {self.cuisine} food.")

    @property
    def cuisine(self):
        return self.cuisine

    @cuisine.setter
    def cuisine(self, value):
        self.cuisine = value
