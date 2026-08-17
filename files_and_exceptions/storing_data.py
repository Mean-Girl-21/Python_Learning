# Using json.dumps() and json.loads() functions for storing data in JSON-formatted strings and loading data back into memory whenever the program runs

from pathlib import Path
import json

numbers = [1,2,3,4,5]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

read_contents = path.read_text()
loaded_numbers = json.loads(contents)

print(loaded_numbers)

# Saving and reading user-generated data

username = input("What is your name ?  ")
path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username} !")

contents = path.read_text()
username = json.loads(contents)
print(f"Welcome back, {username} !")

# Other way to write this :

path = Path("username.json")

if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username} !")
else:
    username = input("What is your name ?  ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username} !")

# Refactoring : Breaking the code into a series of functions that have specific jobs

def get_stored_username(path):
    """Get stored username if available """

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username} !")
    else:
        return None

def get_new_user(path):
    """Prompt for a new username"""

    username = input("What is your name ?  ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet user by name"""

    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        print(f"Welcome back, {username} !")
    else:
        username = get_new_user(path)
        print(f"We'll remember you when you come back, {username}")

greet_user()



