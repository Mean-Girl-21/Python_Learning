# A dictionary in Python is a collection of key-value pairs.
# Each key is associated with a value and we can use a key to access the value associated with it.
alien_0 = {"color" : "blue" , "points" : 5}
print(alien_0["color"])
print(alien_0["points"])

# Adding new key-value pairs
alien_0["x-position"] = 100
alien_0["y-position"] = 150
print(alien_0)

# Modifying and accessing values in a dictionary
alien_1 = {"color" : "blue"}
print(f"The alien's color is {alien_1["color"]}.")

alien_1["color"] = "green"
print(f"Now, its new color is {alien_1["color"]}.")

point_value = alien_1.get("points", "No point value assigned")
print(point_value)


# Example : Using if-elif-else chain with a dictionary

alien_2 = {"x-position" : 0, "y-position" : 25, "speed" : "medium"}
print(f"Original x-position : {alien_2["x-position"]}")

# Move alien to the right and determine how far to move based on the current speed.
if alien_2["speed"] == "slow":
    x_increment = 1
elif alien_2["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3 

alien_2["x-position"] = alien_2["x-position"] + x_increment
print(f"New position: {alien_2["x-position"]}")

# Example : A dictionary of similar objects
favorite_languages = {
    "jen" : "python",
    "sarah" : "jython",
    "edward" : "c",
    "phil" : "rust"
}
print(f"Sarah's favorite language is {favorite_languages["sarah"].title()}.")
del favorite_languages["sarah"]
print(favorite_languages)

# Usage of for loop in a dictionary
# The items() and the keys() methods return a sequence of key-value pairs and keys respectively.

favorite_languages = {
    "jen": "python", 
    "sarah": "jython", 
    "edward": "c", 
    "phil": "rust"}
for name , value in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {value.title()}.")

print("\nThe following have taken our poll:")
for name in favorite_languages.keys():
    print(name.title())

print(f"\nThe following languages have been mentioned:")
for value in set(favorite_languages.values()): # set() is used to return unique items in a collection of duplicate items 
    print(value.title()) 

friends = ["sarah", "phil"]
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")
    if name in friends:
        print(f"{name.title()}, I see you love {favorite_languages[name].title()}!")
if "erin" not in favorite_languages.keys():
    print("Eerin, please take our poll.")

# Looping through a dictionary in an order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll!")

# Nesting a dictionary in a list
# Example 1
alien_0 = {"color" : "yellow" , "points" : 5}
alien_1 = {"color" : "green" , "points" : 10}
alien_2 = {"color" : "red" , "points" : 15}
aliens = [alien_0, alien_1, alien_2]
print(aliens)

# Example 2 
aliens = []

# Make 30 green aliens 
for alien_number in range(30):
    new_alien = {"color" : "green" , "speed" : "slow" , "points" : 5}
    aliens.append(new_alien)

# Modifying the first 3 aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "fast"
        alien["points"] = 10

# Print the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Nesting a list in a dictionary
# Example 1
# Storing information about a pizza being ordered
pizza = {
    "crust" : "thick",
    "toppings" : ["mushrooms" , "extra cheese"]
}
# Summarize the order
print(f"You have ordered {pizza["crust"].title()}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"{topping.title()}")

# Example 2
favorite_languages = {
    "sarah" : ["c" , "python"],
    "jen" : ["c"],
    "david" : ["jython" , "python"]
}

for name, values in favorite_languages.items():
    if len(favorite_languages[name]) == 1:
        print(f"{name.title()}'s favorite language is {value.title()}")
    else:
        print(f"{name.title()}'s favorite languages are:")
        for value in values:
            print(f"\t{value.title()} ")

# A dictionary inside a dictionary
users = {
    "aeinstein" : {
        "first" : "albert",
        "last" : "einstein",
        "location" : "princeton"
        } ,
    "mcurie" : {
        "first" : "marie",
        "last" : "curie" ,
        "location" : "harvard"
    }
}

for username , user_info in users.items():
    print(f"Username: {username.title()}")
    print(f"Full name: {user_info["first"].title()} {user_info["last"].title()}")
    print(f"Location: {user_info["location"].title()}\n")