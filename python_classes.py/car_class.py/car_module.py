"""A set of classes that can be used to represent a gas and electric cars."""

class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 100

    def get_descriptive_name(self):
        description = f"{self.make} {self.model} {self.year}"
        return description

    def read_odometer(self):
        print(f"This car's odometer reading is {self.odometer}.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer:
            self.odometer = mileage

        else:
            print("You cannot roll back an odometer !")

    def increment_odometer(self, value):
        self.odometer += value

    def fill_gas_tank(self):
        print(f"{self.make.title()} has a gas tank.")


# Inheritance : A class (child class) can inherit from another class (parent class) to access the attributes and methods defined in the first class.

# Defining ElectricCar class which inherits from the Car class and a Battery class, whose instance will be used as an attribute


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} kwh battery size.")

    def get_range(self):

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):

        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represents aspects of a car , specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class"""

        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):  # overriding this method from the Car class for the ElectricCar class
        print(f"{self.make.title()} doesn't have a gas tank !")

    



