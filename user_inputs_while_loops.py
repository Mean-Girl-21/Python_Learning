# Using the input function
# Examples:
name = input("Please enter your name: ") # First, python runs the input function and the value given by the user is associated with the variable in which input() function is stored.
print(f"\nHello, {name}") # Then, it prints the value associated with the variable which was assigned by the user.

prompt = input("If you share your name we can personalise the messages you see.\nWhat is your full name?")
print(f"\nHello, {name}!")

# Using int() to accept numerical values
height = input("How tall are you in inches?")
height = int(height) # int() function tells python that the value given by the user after running input() function is numeric and not a string. This is done because input() function ,by default, takes string values. 
if height >=48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number and we'll tell you if it's even or odd.\nYour number: ")
number = int(number)
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# While loop runs as long as , or while, a certain condition is true. Whereas, for loop executes a block of code for each item in the collection of items.
# Examples
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "Tell me something and I will repeat it back to you. "
prompt += "Enter 'quit' to end the program."
message = ""

while message != "quit":  # Condition for python to enter the loop
    message = input(
        prompt
    )  # Displays the prompt and stores the vaue given by the user in the message variable
    if message != "quit":
        print(message)

# We can use a variable 'flag' which , if true, signals python to keep the program running.
# This is done because we may have many conditions which may signal python to stop the program. Flag is used to simplify this process.

prompt = "Tell me something and I will repeat it back to you. "
prompt += "Enter 'quit' to end the program."
active = True  # Active is the name of the flag variable

while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

new_prompt = "\nPlease enter the name of the city that you have visited. "
new_prompt += "Enter 'quit' once you are finished. "
while True:
    city = input(new_prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to visit {city.title()}!")

# Rather than using break to end the loop and not execute the rest of the code, we can use continue statement to return to the begining of the loop, based on the result of the conditional test.
new_number = 0
while new_number < 10:
    new_number += 1
    if new_number % 2 == 0:
        continue
    print(new_number)

# Using a while loop with lists and dictionaries

# Example 1 : Moving items from one list to another
uncomfirmed_users = ["brian", "sarah", "david"]
confirmed_users = []

while uncomfirmed_users:
    new_user = uncomfirmed_users.pop()
    print(f"Verifying {new_user.title()}")
    confirmed_users.append(new_user)

print("Here is the list of confirmed users:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# Example 1 : Moving items from one list to another
uncomfirmed_users = ["brian", "sarah", "david"]
confirmed_users = []

# Verify each user until there's no unconfirmed user
# Move each verified user to a list of confirmed users
while uncomfirmed_users:
    new_user = uncomfirmed_users.pop()
    print(f"Verifying user : {new_user.title()}")
    confirmed_users.append(new_user)

print("Here is the list of confirmed users:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of specific values from a list
pets = ["dogs", "cats", "rabbit", "cats", "dogs", "cats"]
while "cats" in pets:
    pets.remove("cats")
    print(pets)

# Filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name ? ")
    response = input("Which mountain would you like to climb ? ")
    # Store responses in a dictionary
    responses[name] = response
    repeat = input("Would you like to let another person respond ? (yes/no) ")
    if repeat == "no":
        polling_active = False

for name, reponse in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
