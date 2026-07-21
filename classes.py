# Classes represent real world things or situations and we can create objects based on these classes
# Making an object from a class is called instantiation, and we work with instances of a class

# Creating a Dog class
# Each instance of the Dog class will store a name and age , and will have the ability to sit() and roll_over()


# Working with classes and instances

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 7)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()
my_dog.roll_over()


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        description = f"{self.make} {self.model} {self.year}"
        return description

    def read_odometer(self):
        print(f"This car's odometer reading is {self.odometer}.")

    def update_odometer(self, mileage):
        self.odometer = mileage


my_car = Car("Audi", "a4", "2019")
my_car.read_odometer()
print(my_car.get_descriptive_name())

your_car = Car("Audi", "a5", "2020")
print(your_car.get_descriptive_name())
your_car.odometer = 50
your_car.read_odometer()

your_car.update_odometer(1000)
your_car.read_odometer()


class Restaurant :

    def __init__(self, name, cuisine):
        self.name = name 
        self.cuisine = cuisine
    

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and their cuisine is {self.cuisine}.")

    def open_restaurant(self, status):

        if status :
            print(f"{self.name} is open.")

        else:
            print(f"{self.name} is currently closed.")

restaurant = Restaurant("Big Chef", "Indian")
restaurant.describe_restaurant()
restaurant.open_restaurant(True)
