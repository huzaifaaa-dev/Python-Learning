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
x = int((input("What is x? ")))  # input() returns a string, so we convert the input to an integer using int().
y = int((input("What is y? ")))  # To fix these, do int(x) or int(input("")) 

z = float(x) + float(y) # Using Float to get Numbers with their respective Decimal Points
# The above could also be int(x) + int(y) or x = int(input("What is x? "))
print(z)

# Try out rounding and use of f strings to add commas into larger, longer numbers.
a = float(input("What is a? "))
b = float(input("What is b? "))

c = round(a + b) # Rounded to the nearest WHOLE number.

print(f"{c:,}") # The Method to add a comma per 3 letters in bigger numbers, for a cleaner look.

d = float(input("What is d? "))
e = float(input("What is e? "))

f = round(d / e, 2)    # Method one to round to Specific number of Decimal numbers.

print(f"{f:.2f}") # Method two to round to Specific Number of Decimal numbers. 
# .2f represents the number of decimal spaces, either you do method one, OR method two, NOT both.

# Every function is basically nameoffunction() , MEMORIZE.
def hello(to="World"):
    print("Hello, ", to)

naaamee = input("Whats your name? ")
hello(naaamee)

def main():
    x = int(input("What is x? "))
    print("x cubed is", cubed(x))

def cubed(n):
    return n * n * n

main()