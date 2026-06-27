# print() function
print("Hello World!")

# Variable references a certain value. 
# A method is used to perform an action on a piece of data. 
# The method title(), upper() and lower() appear after the variable name in print() and the dot '.' tells Python to perform an action on the variable.
message = "her name is ada lovelace"
new_message = "HER NAME IS ADA LOVELACE"
print(message)
print(message.title())
print(message.upper())
print(new_message.lower())

# format string is used when we want to insert the value of one or more than one variable in a string.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


# Python programmers use all capital letters to indicate that a variable should be treated as a constant and never be changed. 
MAXIMUM_NUMBER = 1_50_00_00_000
print(MAXIMUM_NUMBER)

# Practice : Calculations resulting in the number 8
print(5 + 3)
print(4 * 2)
print(2 ** 3) # ** denotes exponent
print(9 - 1)
print(2 + (3 * 2))
print(16 / 2)
print(16 // 2) # // is used when the result of division needs to be an integer


