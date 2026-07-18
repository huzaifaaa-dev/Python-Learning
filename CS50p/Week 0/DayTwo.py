# How to make use of strings functions
name = input("What is your name? ")
# Name is our variable and we are using the strip() function to remove any whitespace from the input. 
# The Python documentation has a list of all the string functions, like "strip()" available in Python.

# Remove any whitespace from the user's input.
name = name.strip()
# Capitalize user's input/name
name = name.capitalize()
print(f"Hello, {name}")
# Convert user's input/name's first letter of each word to uppercase.
name = name.title()
print(f"Hello, {name}")
# Split user's name into first name and last name.
first, last = name.split(" ")
print(f"Hello, {first}")

# Convert user's input to remove any and all Whitespace as well as to Caaapitalize the first letter of each word in the given input.
favourite_game = input("What is your favourite game? ").strip().title()
print(f"Your favourite game is {favourite_game}")

# Basic Calculator
x = int(input("What is x? "))  # These are strings, David Malan forgot to make the variables integers with the int() function.
y = int(input("What is y? "))  # To fix these, do int(x) or int(input("")) 

z = x + y

print(z)