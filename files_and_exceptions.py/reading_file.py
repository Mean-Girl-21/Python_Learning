# When python reads from a txt file, it interprets all text as string

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

# Checking if someone's birthday is contained in pi

bday = input("Enter your birth date : ")
if bday in pi_string:
    print("Your birthdate appears in the first 100 digits of pi !")
else:
    print("Your birthdate doesn't appear in the first 100 digits of pi.")
