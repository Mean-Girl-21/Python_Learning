from name_function import get_formatted_name

print("Enter q at any time to quit")

while True:
    first_name = input("What is your first name ?  ")
    if first_name == "q":
        break

    middle_name = input(
        "What is your middle name ? Type 0 if you don't have a middle name.  ")
    if middle_name == "q":
        break

    elif middle_name == "0":
        pass

    last_name = input("What is your last name ?  ")
    if last_name == "q":
        break

    if middle_name == "0":
        formatted_name = get_formatted_name(first_name, last_name)
        print(f"Neatly formatted name : {formatted_name}\n")

    elif middle_name != "0" and middle_name != "q":
        formatted_name = get_formatted_name(first_name, last_name, middle_name)
        print(f"Neatly formatted name : {formatted_name}\n")
