from car_module import Car

my_car = Car("Audi", "a4", "2019")
my_car.read_odometer()
print(my_car.get_descriptive_name())

your_car = Car("Audi", "a5", "2020")
print(your_car.get_descriptive_name())

your_car.odometer = 50  # accessng the attribute and assigning it a new value
your_car.read_odometer()

your_car.update_odometer(1000)  # assigning a new value to the attribute using a function
your_car.read_odometer()

your_car.increment_odometer(1000) # incrementing attribute's current value 
your_car.read_odometer()
