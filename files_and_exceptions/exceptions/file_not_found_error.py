# Handling missing files or files stored in a different directory

from pathlib import Path

path = Path('alice_chapter1.txt')

try:
    contents = path.read_text(encoding = 'utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} doesnt exist in this directory.")

else:
    # Count the number of of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# Working with multiple files

def count_words(path):
    "Counts the number of words in a file"

    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesnt exist in this directory.")
    else:
        # Count the number of of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# The filenames are stored as strings in a list and are then, converted into Path object
filenames = ['alice_chapter1.txt', 'moby_dick_chapter1.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
    
