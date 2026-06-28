# Looping allows one to take the same action or a set of actions with all the items in a list.
# Using for loop to retrieve all items in a list
magicians = ["sam", "ava", "amrin", "alice", "david"]
for magician in magicians:
    print(magician)

# for loop tells python to associate the items in the list (magicians) with the variable (magician).
# Then, we ask python to print the name of the list item that has just been assigned to magician variable.
# It repeats the process until all items have been printed.

# Further examples:

magicians = ["sam", "ava", "amrin", "alice", "david"]
for magician in magicians:
    print(f"\n{magician.title()}, That was a great trick!")
    print(f"We can't wait to see your next trick, {magician.title()}.\n")
print("The show was great. Looking forward to the next magic show.")

pizzas = ["margherita", "farmhouse", "pepperoni","veggie paradise"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.\n")
print("I really love these pizzas!\n")

# Using range() and list() function to work with a numerical list
for number in range(1,7):
    print(number)

odd_numbers = list(range(1,12,2))
print(odd_numbers)

even_numbers = [2,4,6,8,10]
for even_number in even_numbers:
    print(even_number**2)

cubes = []
for value in range(1,11): 
    cubes.append(value**3)

print(cubes)

# Other way to get the same result
cubes = [value**3 for value in range(1,11)]
print(cubes)

# Slicing a list
players = ["sam", "charles","martina","michael", "james"]
print(players[0:3]) # prints players from 0 to 2 index position 
print(players[:4])  # prints players from 0 to 3 index position
print(players[0:])  # prints all players
print(players[-2:])  # prints the last two players 

print("\nHere are the first three players on my team:")
for player in players[0:3]:
    print(player.title())

# Copying a list using a slice
new_players = ["sam", "charles", "martin", "michael", "james"]
previous_players = players[:]

new_players.append("samuel")
previous_players.append("samantha")

print("New team players are:")
print(new_players)

print("\nPrevious team players were:")
print(previous_players)

# A tuple is an ordered collection of items that cannot change, i.e. an immutable list.
rectangle_dimensions = (200, 150)
print(rectangle_dimensions[0])
print(rectangle_dimensions[1])

# We cannot modify a given tuple. But we can assign a new value to a variable that represents that tuple.
rectangle_dimensions = (200, 150)
print("Original dimensions:")
for rectangle_dimension in rectangle_dimensions:
    print(rectangle_dimension)

new_rectangle_dimensions = (90,100)
print("\nNew dimensions:")
for new_rectangle_dimension in new_rectangle_dimensions:
    print(new_rectangle_dimension)
