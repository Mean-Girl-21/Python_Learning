# A list is an ordered collection of items.
# The square brackets [] indicate a list and the items of the list are separated by commas.

colleges = ["srcc", "lsr", "kmc", "hindu", "stephens"]
print(colleges[3].upper()) # Index positions of the items in a list start from 0, not 1. 
message = f"I completed my undergraduate degree from {colleges[1].upper()}."
print(message)

# Modifying an element in the list using index position of the list items
colleges[0] = "dse" # It replaces the ietm at 0 index with the modified item.
print(colleges)

# Appending elements to the end of the list using append() method
colleges.append("ramanujhan")
print(colleges)

# Inserting an element at a specific index position in a list using insert() method
colleges.insert(1, "jesus & mary")
print(colleges)

# Deleting an item using the del statement
del colleges[2]
print(colleges) # One can no longer access the removed item after the del statement is used.

# Removing an item using the pop() method
popped_college = colleges.pop() # The pop() method removes the last item from the list but it lets one work with that item after removing it.
print(colleges)
print(popped_college)

undergrad_college = colleges.pop(1) # Specifying the index of the list item to remove using pop() method 
print(f"{undergrad_college.title()} college is a part of University of Delhi.")
print(colleges)

# Removing an item by value using remove() method
colleges.remove("kmc")
print(colleges)

# Sorting a list permanently using sort() method
colleges.sort()

# Sorting a list temporarily using sorted() function
cars_in_delhi = ["bmw", "audi", "toyota"]
print("Here is the original list:")
print(cars_in_delhi)

print("\nHere is the sorted list:")
print(sorted(cars_in_delhi))

print("\nHere is the original list again:")
print(cars_in_delhi)

# Printing a list in reverse chronological order using reverse() method
cars_in_delhi.reverse() # reverse() method changes the order permanently
print(cars_in_delhi)

# Finding out the length of a list using len function
print(len(cars_in_delhi))

