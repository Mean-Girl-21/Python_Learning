# One of the simplest ways to save data is to write it to a file

# Writing a single line

from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming")

# Writing multiple lines

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('programming.txt')
path.write_text(contents)