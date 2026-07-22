"""Created a simple Restaurant class and its child class, IceCreamStand."""

class Restaurant:
    """A simple attempt to model a restaurant and keep a record of the number of customers."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and their cuisine is {self.cuisine}.")

    def open_restaurant(self, status):

        if status:
            print(f"{self.name} is open.")

        else:
            print(f"{self.name} is currently closed.")

    def customers_served(self, number_served):
        print(f"The {self.name} restaurant has served {number_served} customers.")

    def increment_customer_served(self, increment):
        self.number_served += increment
        print(f"{self.name} has served {self.number_served} customers today.")


restaurant = Restaurant("Big Chef", "Indian")
restaurant.describe_restaurant()
restaurant.open_restaurant(True)

restaurant.number_served = 100
print(f"{restaurant.name} has served {restaurant.number_served} customers.")

restaurant.increment_customer_served(1000)


class IceCreamStand(Restaurant): # Specifying the parent class in parentheses
    """Represents an ice-cream stand with available flavors."""

    def __init__(self, name, cuisine): # Here, we define __init__ for the child class
        super().__init__(name, cuisine) # Here, we specify what attributes it inherits from the parent class using super() function
        self.flavors = ["strawberry", "mango", "chocolate"]

    def print_flavors(self):
        print(f"\n{self.name.title()} has the following ice cream flavors :\n")
        for index ,flavor in enumerate(self.flavors, start=1):
            print(f"{index}. {flavor.title()}")


baskin_robbins = IceCreamStand("baskin robbins", "ice-creams")
baskin_robbins.print_flavors()

