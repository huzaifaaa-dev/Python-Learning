# CS50P Notes

## Week 0

### Day 1 — Functions, Variables, and Printing

`input()` is used to get information from the user. By default, `input()` returns a string.

If I want to use the input as a number, I need to convert it:

age = int(input("What is your age? "))

`int()` converts the input into an integer (a whole number).

`print()` has two useful arguments: `end` and `sep`.

`end` controls what is printed at the end of a `print()` statement. By default, `end` is `"\n"`, which moves the cursor to a new line.

print("Hello", end="")
print("World")

prints:

HelloWorld

Using:

print("Hello", end="\n")

does the same thing as the default behavior.

`sep` controls what is printed between multiple values in a `print()` statement.

print("You are", age, sep=" ")

Here, the separator is a space.

To print quotation marks inside a string, I can either escape them using `\"`:

print("Hello, \"friend\"")

or use a different type of quotation mark around the string:

print('Hello, "friend"')


### Day 2 — Strings, Numbers, Formatting, and Functions

Strings have built-in methods that can be used to modify or work with text.

`.strip()` removes whitespace from the beginning and end of a string.

`.capitalize()` makes the first character uppercase and the rest lowercase.

`.title()` capitalizes the first letter of each word.

`.lower()` converts the entire string to lowercase.

`.replace()` replaces one piece of text with another.

Example:

input_user.replace(" ", "...")

replaces every space in the string with three dots.

`.split()` splits a string into multiple pieces.

first, last = name.split(" ")

If the input is:

John Smith

then:

first = "John"
last = "Smith"

String methods can be chained together.

favourite_game = input("What is your favourite game? ").strip().title()

This gets the user's input, removes whitespace from the beginning and end, and capitalizes the first letter of each word.

`input()` returns a string by default, so I need to convert the input when I want to perform calculations.

x = int(input("What is x? "))

`int()` is used for whole numbers.

`float()` is used for numbers that can contain decimal points.

For example:

x = float(input("What is x? "))

I can also convert an existing value:

z = float(x) + float(y)

However, if `x` and `y` are already integers, I can simply use:

z = x + y

`round()` rounds a number.

round(a + b)

rounds to the nearest whole number.

round(d / e, 2)

rounds the result to 2 decimal places.

The second argument tells `round()` how many decimal places to round to.

F-strings allow me to insert variables directly into strings.

print(f"Hello, {name}")

They can also be used to format numbers.

f"{c:,}"

adds commas to large numbers.

For example:

1000000

becomes:

1,000,000

f"{f:.2f}"

displays the number with exactly 2 decimal places.

`round(d / e, 2)` rounds the actual value to 2 decimal places.

`f"{f:.2f}"` controls how the value is displayed and ensures that exactly 2 decimal places are shown.

Functions allow me to create reusable blocks of code.

def hello(to="World"):
    print("Hello,", to)

`to` is a parameter. `"World"` is the default value, meaning that if no argument is provided, the function uses `"World"`.

For example:

hello("Huzaifa")

passes `"Huzaifa"` into the `to` parameter.

A function can return a value using `return`.

def cubed(n):
    return n * n * n

The result can then be used elsewhere:

print(cubed(x))

`return` sends a value back to the code that called the function. This is different from `print()`, which only displays something on the screen.

The cube can also be calculated using:

return n ** 3

A function can be used inside another function.

def main():
    x = int(input("What is x? "))
    print("x cubed is", cubed(x))

def cubed(n):
    return n ** 3

main()

The program starts by calling `main()`. `main()` gets the input and then calls `cubed()` to calculate the result.

---

## Problem Set 1 — `indoor.py`

The program asks the user to enter some text:

user_input = input("Would you like to share something? ")

`.lower()` then converts the entire input to lowercase:

user_input = user_input.lower()

The lowercase text is printed.

This can also be written more compactly:

user_input = input("Would you like to share something? ").lower()

---

## Replacing Things Inside a String

The program asks the user to enter a thought:

input_user = input("Would you like to share a thought? ")

`.replace()` replaces one piece of text with another.

input_user.replace(" ", "...")

This replaces every space `" "` with three dots `"..."`.

For example:

Hello World

becomes:

Hello...World