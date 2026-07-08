# Functions are named blocks of code that are designed to a specific job.
# A function call tells python to execute the code defined by the function.
def greet_user():
    """Display a simple greeting.""" # This is a docstring (comment) which describes what this function does. 
    print("Hello!") # This is the task which is required to be performed by the function.

greet_user() # Function call


def greet_user(username):  # We specify the extra info that the function needs in the parentheses. This is also called a parameter (username)
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")
# Now, python will look for an argument for the parameter in order to execute this code.
# An argument is a piece of info that is passed from a function call to the function.
greet_user("tanvi") 

# Positional arguments : These type of arguments need to be in the same order as the parameters as python matches each argument with the parameters in the order they were specified.
def describe_pet(animal_type, pet_name):
    """Display information about the pet"""
    print(f"I have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet("dog","harry")
describe_pet("hamster", "willie")


# Keyword arguments : These arguments are provided in 'name : value' pairs. The order of the arguments doesn't matter as python matches each value with its name during a function call.
def describe_pet(animal_type, pet_name):
    """Display information about the pet"""
    print(f"I have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet(animal_type = "dog" , pet_name = "harry")


def describe_pet(pet_name, animal_type = "dog"): 
    # Here, we provide a default value of a parameter , which python will use if the user doesn't provide value for the parameter.
    # All parameters with default values need to be provided after those parameters have been provided that dont require default values. This is done so that python can interpret the arguments in an order.
    """Display information about the pet"""
    print(f"I have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")


describe_pet(pet_name="harry")  

# Return values : The value a function returns is called a return value.
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jimi" , "hendrix") 
# We assign a returned value to a variable is because the function is giving us back some information, and we usually want to store it, use it later, or manipulate it.
print(musician) 

# Making an argument optional
def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a neatly formatted full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name} "
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jim', 'hooker' , 'lee') #We need to give the argumnets in the same order as parameters
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
    """Returns a dictionary of information about a user."""
    user_info = {'first' : first_name , 'last' : last_name}
    return user_info 
user = build_person('jimi' , 'hendrix')
print(user)

def build_person(first_name, last_name, age = None):
    """Returns a dictionary of information about a user."""
    user = {'first' : first_name, 'last' : last_name}
    if age:
        user['age'] = age
        return user 
    else:
        return user
musician = build_person('jimi', 'hendrix', 27)
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a simple greeting with formatted names."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
     print("Please tell me your name.\nType q to stop the program.")
     f_name = input("First name : ")
     if f_name == 'q':
         break
     l_name = input("Last name : ")
     if l_name == 'q':
         break
     format_name = get_formatted_name(f_name, l_name)
     print(format_name)

# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        print(f"Hello, {name.title()}!")
usernames = ["hannah", "mikey"]
greet_users(usernames)

# Modifying list in a function (changes are permanent)
def print_models(unprinted_designs, completed_models):
    """Simulate printing design until none are left. Move each unprinted design to completed models list"""
    while unprinted_designs:
        u_design= unprinted_designs.pop()
        completed_models.append(u_design)
        print(f"Printing model : {u_design.title()}")
def show_completed_models(completed_models): 
    """Show all the models that were printed."""
    print("\nThe following designs have been printed :")
    for model in completed_models:
        print(model.title())

unprinted_designs = ['phone case', 'robot pendant']
completed_models =[]
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Passing an arbitrary number of arguments using asterisk
def make_pizza(*toppings):
    """Summarise the pizza we are going to make."""
    print(f"Here are the toppings that we'll use: ")
    for topping in toppings:
        print(f"-{topping.title()}")
make_pizza('pepperoni', 'cheese')

def make_pizza(size, *toppings):
    """Summarise the pizza we are going to make."""
    print(f"Making a {size} - inch pizza with the following toppings :")
    for topping in toppings:
        print(f"- {topping.title()}")
make_pizza(16 , 'mushrooms', 'peppers', 'cheese')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first'] = first 
    user_info['last'] = last
    return user_info
user_info = build_profile('jimi', 'hendrix', age = 27, location = 'princeton')
print(user_info)

# Storing functions in modules : We can store the functions in a file (module) and import them whenever we want to use them in another file.

# Syntax for importing all functions in a module:
# import module_name , or we can use from module_name import *
# Then we can use the function by writing : module_name.function_name()
# To import specific functions : from module_name import function_1, function_2
# Alias or an alternate name can be given to a function or a module using as:
# from module_name as module_alias import function_name as function_alias
# This is done to simplify the names of modules and functions in a file while working. 