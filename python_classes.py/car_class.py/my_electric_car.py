from car_module import ElectricCar

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

my_leaf.fill_gas_tank()  # Upon calling this method, python ignores the method fill_gas_tank() in the car class and executes the method defined in the ElectricCar class

# Updating and accessing the attributes and methods

my_leaf.battery.describe_battery()
my_leaf.battery.battery_size = 40

my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
