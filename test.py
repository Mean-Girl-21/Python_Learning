# fruits = ["apple", "banana", "orange", "plum","cheeku","mango"]
# # for fruit in fruits:
# #     if fruit == "orange":
# #         print(f"Orange is a fruit and a color as well!")
# #         break
# #     else:
# #         continue

# # for number in range(1,12):
# #     if number % 2 != 0:
# #         continue # skip the number and continue it
# #     else:
# # #         print(number)

# # if "orange" in fruits:
# #     print(f"Orange is a fruit and a color as well!")  #in - membership

# # # in if else  you can add more blocks of if else

# # user_1 = {"name" : "tanvi" , "address": "abc"}
# # user_1["phone"] = "6284xxx"
# # print(user_1)

# # user_2 = {}
# # # dict() function
# # del user_1["name"]
# # # pdf me check remove methods
# # scores = [45, 78, 92, 33, 67, 88, 55, 71]

# # # sum = 0
# # # for score in scores:
# # #     sum = sum + score

# # # print(sum)
# # # print(max(scores))

# # abc = [1,2,2]
# # print(sum(abc))


# # # a = 100
# # # b = "hello"
# # # c = 3.14
# # # d = True
# # # e = [1, 2,3]
# # # print(type(a))
# # # a = str(a)
# # # print(type(a))
# # # f = (1,2)
# # # print(type(f))
# # # e = tuple(e)
# # # print(type(e))
# # # print(e)
# # # name = input("Hi, what's your name ?")
# # # age = int(input("What's your age?"))
# # # print(f"Hi {name}, your age is {age}.")
# # # integer_array = [x for x in range(2,11,2)]
# # # print(integer_array)
# # # squares = [x**2 for x in range(2,21) if x % 2 == 0]
# # # print(squares)
# # # scores = [45, 78, 92, 33, 67, 88, 55, 71]
# # # sum = 0
# # # for score in scores:
# # #     sum = sum + score

# # # print(sum)
# # # print(sum(scores))

# # lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(lst[1][2])

# # student = {
# #     "name": "tanvi",
# #     "age": "23",
# #     "grade": "b minus",
# #     "subjects": ["a", "b", "c"],
# # }
# # for (
# #     key
# # ) in (
# #     student.items()
# # ):  # items returns two values so we need 2 variables.otherwise returns outer elelments
# #     print(f"{key}")

# # print(student.items())  # retruns a list of tuples

# Q
coordinates = (28.6, 77.2, 216)
#tuple unpacking : assigning each element in a tuple to a variable.
latitude, longitude, altitude =  coordinates
latitude, longitude, _ =  coordinates #_ to ignorethe variable
latitude, *rest = coordinates # the remaining elemtns will come in a list

print(latitude) 



# Q17
inventory = {"apple": 50, "banana": 30, "mango": 20, "grapes": 45}
inventory["orange"] = 60
inventory["banana"] = 55
del inventory["mango"] # del statement to delete "mango" key and its value from the dictionary
print(inventory.keys())
print(inventory.values())
print(inventory.items())

# Q18-19 doubt - below is just rough calc
# cube_numbers = {"x" : x**3 for x in range(1,11)}
# print(cube_numbers)
# cube_numbers = {}
# for x in range(1,11):
#     cube_numbers.append(x)

# Q 20
number = int(input("Give us a number "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0 :
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Q 21
marks = int(input("Tell us your marks and we'll tell you the grade. "))
if  90 <= marks <= 100 :
    print("Grade: A+")
elif 75 <= marks <= 89:
    print("Grade: A")
elif 60 <= marks <= 74:
    print("Grade: B")
elif 45 <= marks <= 59:
    print("Grade: C")
else:
    print("You have failed this examination.")

# Q 22
year = int(input("Enter a year and we'll tell whether it's a leap year. "))
if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Q 23
age = int(input("Enter your age. "))
status = 'Adult' if age >= 18 else 'Minor'
print(status)

# Q24
print("\nThe multiples of 7 from 1 to 100 are: ")
for number in range(1,100):
    if number % 7 == 0:
        print(f"{number}")
    else:
        continue

# Q 25 - 28 - doubt

# Q 29
action = True 
# tag variable that takes boolean values to signal that a program is working
# it is signal to python to enter the while loop and run the program as long as the value of tag variable is True
while action:
    prompt = int(input("Enter a number: "))
    if prompt > 5:
        print(f"{prompt} is too high. Try again!")
    elif prompt < 5:
        print(f"{prompt} is too low. Try again!")
    elif prompt == 5:
        print(f"{prompt} is the correct answer!")
        break


# Q-30
for number in range(1,21):
    if number % 3 == 0:
        continue
    elif number % 5 == 0 and number % 7 == 0:
        break
    elif number % 2 == 0:
        pass
    print(number)

# Q 31
students = {
    "david" : 55,
    "ava" : 65,
    "catherine" : 39
}
for name, marks in students.items():
    if marks < 40:
        print(f"{name.title()} : Fail")
    else:
        print(f"{name.title()} : Pass")

# Q 32
prime_numbers = []
for x in range(1,51): 
    if x > 1 and (x % y != 0 for y in range(2, int(x**0.5)+ 1)): # a number is prime if n>1 and n % i is not equal to zero for all integers between 2 and root(n).
        # This part of code not working
        prime_numbers.append(x)
    else:
        continue
print(prime_numbers)

# Q 33
lst_num = []
active = True 
while active: 
    your_num = int(input("Please enter a number: "))
    if your_num != 0:
        lst_num.append(your_num)
    else:
        lst_num.append(your_num)
        print("We will no longer take new numbers.")
        break

print(lst_num)
print(sorted(lst_num))
print(f"{lst_num[0]} is the minimum value.")
print(f"{lst_num[-1]} is the maximum value.")
if len(lst_num) == 1:
    print("Average : 0")
else:
    print(f"Average: {sum(lst_num)/len(lst_num)}")
