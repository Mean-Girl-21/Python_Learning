# Examples of conditional tests
# Checking for equality :
cars = ["audi", "bmw", "toyota", "subaru", "maruti","nano"]
for car in cars:
    if car == "toyota":  # This can be read as : Is the value of car equal to toyota ?
        print(car.upper())
    else:
        print(car.title())

car = "Audi"
print(car.lower() == "audi") 

# Checking for inequality :
pizza_toppings = "mushrooms"
if pizza_toppings != "anchovies":
    print("Hold the anchovies!")

# Numerical comparisons :
age_0 = 21
age_1 = 23
print((age_0 >= 17) and age_1 <=50)
print((age_0 >= 25) or (age_1 <=24))

# Checking whether a value is in or not in the list :
requested_toppings = ["mushrooms", "pepperoni", "pineapple"]
print("mushrooms" in requested_toppings)
print("onions" in requested_toppings)
print("onions" not in requested_toppings)

# If-else statements
# Python uses the values True and False (results of a conditional test) to decide whether the code in an if statement should be executed.
age_2 = 17
if age_2 >= 18 :
    print("\nYou are old enough to vote.\nHave you registered yet?")
else :
    print("\nSorry you are too young to vote.\nPlease register as soon as you turn 18.")

# If-elif-else statements (used to test two or more than two conditions at once)
age_3 = 12
if age_3 <= 4:
    print("\nYour admission cost is $0.")
elif  4 < age_3 <= 18:
    print("\nYour admission cost is $10.")
else:
    print("\nYour admission cost is $40.")

# We can also omit the else block in an if-elif chain as long as an additional elif block captures the condition of interest.
age_3 = 12
if age_3 <= 4:
    print("\nYour admission cost is $0.")
elif age_3 <= 18: 
    print("\nYour admission cost is $10.")
elif age_3 < 65:
    print("\nYour admission cost is $30.")
elif age_3 >= 65:
    print("\nYour admission cost is $40.")

# If you want only one block of code to run, use an if-elif-else chain.

requested_toppings_new = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings_new:
    print("\nAdding mushrooms.")
elif "onions" in requested_toppings_new:
    print("\nAdding onions.")
elif "extra cheese" in requested_toppings_new:
    print("\nAdding extra cheese.")

print("Your pizza is ready!")

# If more than one block of code needs to run, use a series of independent if-statements.
if "mushrooms" in requested_toppings_new:
    print("\nAdding mushrooms.")
if "extra cheese" in requested_toppings_new:
    print("Adding extra cheese.")

print("\nYour pizza is ready!")

# Using if-statements with lists :
available_toppings = ["mushrooms", "olives", "green peppers","pepperoni","onions"]
for available_topping in available_toppings:
    if available_topping == "onions":
        print("Sorry, we are out of onions")
    else:
        print(f"Adding {available_topping.title()}")

print("Your pizza is ready!")

# Checking if a list is empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping.title()}")
    print("Finished making your pizza.")
else:
    print("Are you sure you want a plain pizza ?")

# Working with multiple lists
requested_toppings = ["mushrooms", "extra cheese", "pineapple"]
available_toppings = ["mushrooms", " onions", "extra cheese", "pepperoni", "olives"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we dont have {requested_topping}.")
        print(f"Only {available_toppings} are available.")

print("Your pizza is ready!")







