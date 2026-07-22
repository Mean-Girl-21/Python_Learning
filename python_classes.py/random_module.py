"""Using random module from python's standard library"""

from random import randint, choice, sample

# Example 1 : Using randint and choice functions

print(randint(1, 7))
players = ["charles", "martina", "michael", "florence"]
first_up = choice(players)
print(first_up)

# Example 2 : Creating a class Die

class Die:
    """Creating a die that returns a random number upon rolling"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        dice_number = randint(1, self.sides)
        return dice_number


six_die = Die(6)

print("Rolling a die 10 times")
for i in range(10):
    print(f"Roll : {i+1}, Number Obtained : {six_die.roll_die()}")

# Example 3 : Lottery

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c"]
winning_ticket = sample(lottery, 4)  # Gives a list

print("Any ticket matching these 4 numbers or letters wins a prize")
print(winning_ticket)

## Lottery Analysis (using While Loop)

my_ticket = [3, 4, 6, "a"]

trials = 0

while True:
    trials += 1
    winning_ticket = sample(lottery, 4)

    if (winning_ticket == my_ticket) and (trials > 1):  # we can convert the tickets into sets and then test the condition if the order of the items doesn't matter
        print(f"You have won the lottery ! I took {trials} trials")
        break

    elif (winning_ticket == my_ticket) and (trials == 1):
        print(f"You have won the lottery ! I took {trials} trial only :)")
        break

    else:
        continue
    
