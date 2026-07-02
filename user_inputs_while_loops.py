# Using the input function
# Examples:
name = input("Please enter your name: ")
print(f"\nHello, {name}")

prompt = "If you share your name we can personalise the messages you see."
prompt += "\nWhat is your full name?"
print(input(prompt))
print(f"\nHello, {prompt}!")

# Using int() to accept numerical values
height = input("How tall are you in inches?")
height = int(height)
if height >=48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number and we'll tell you if it's even or odd.\n Your number: ")
number = int(number)
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")