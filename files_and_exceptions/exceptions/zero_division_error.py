# Python uses special objects called exceptions to manage errors that arise during the program's execution
# Exceptions are handled with try-except blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide a number by 0 !")

# Example 1 : Creating a simple calculator that does division

print("Give me two numbers and i'll divide them ")
print("Enter 'q' to quit")

while True:
    num_1 = input("Enter the first number :  ")
    if num_1 == 'q':
        break
    else:
        num_2 = input("Enter the second number :  ")

        if num_2 == 'q':
            break

        else: 
            try:
                answer = int(num_1) / int(num_2)
                print(f"The answer is {answer}.")

            except ZeroDivisionError:
                print("The denominator cannot be zero in division.")


                

