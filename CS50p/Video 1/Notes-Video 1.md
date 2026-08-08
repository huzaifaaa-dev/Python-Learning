# Day 1 — Video 1

## If, Elif, and Else

`if`, `elif`, and `else` are used to make decisions in a program based on whether a condition is `True` or `False`.

`if` checks the first condition.

`elif` means "else if" and allows me to check another condition if the previous condition was false.

`else` runs when none of the previous conditions were true.

For example:

```
if a > b:
    print("a is bigger than b")
elif a < b:
    print("a is smaller than b")
elif a == b:
    print("a is equal to b")
```

Once Python finds a condition that is `True`, it runs that block and skips the remaining `elif` and `else` blocks.

---

## Comparison Operators

Comparison operators compare values and produce either `True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

`==` means "equal to".

`=` means assignment.

For example:

```
x = 5
```

assigns `5` to `x`.

```
x == 5
```

checks whether `x` is equal to `5`.

---

## Logical Operators

Logical operators allow me to combine conditions.

### `and`

`and` means that both conditions must be `True`.

```
if score >= 90 and score <= 100:
    print("Grade: A")
```

### `or`

`or` means that at least one condition must be `True`.

```
if c > d or c < d:
    print("c is not equal to d")
```

### `not`

`not` reverses a Boolean value.

```
not True   # False
not False  # True
```

---

## Not Equal: `!=`

Instead of checking whether one value is greater than another OR smaller than another:

```
if c > d or c < d:
    print("c is not equal to d")
else:
    print("c is equal to d")
```

I can directly use `!=`:

```
if c != d:
    print("c is not equal to d")
else:
    print("c is equal to d")
```

`!=` checks whether two values are different.

---

## Chained Comparisons

Python allows me to combine comparisons into a single expression.

Instead of:

```
if score >= 90 and score <= 100:
    print("Grade: A")
```

I can write:

```
if 90 <= score <= 100:
    print("Grade: A")
```

This means that `score` must be greater than or equal to `90` AND less than or equal to `100`.

I can also use this for other ranges:

```
elif 80 <= score < 90:
    print("Grade: B")
```

---

## Simplifying Conditions

Sometimes I don't need to explicitly check both sides of a range.

For example:

```
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
```

Python checks the conditions from top to bottom.

If Python reaches `elif score >= 80`, I already know that `score` was not `>= 90`.

Therefore, the second condition effectively covers the `80–89` range.

This allows me to write shorter and cleaner conditional statements.

---

## Modulo: `%`

The `%` operator gives me the remainder after division.

For example:

```
5 % 2
```

gives:

```
1
```

because 5 divided by 2 leaves a remainder of 1.

```
6 % 2
```

gives:

```
0
```

because 6 divides evenly by 2.

This makes `%` useful for checking whether a number is even or odd.

```
if e % 2 == 0:
    print("Even")
else:
    print("Odd")
```

If a number has a remainder of `0` when divided by `2`, it is even.

---

## Functions

Functions allow me to create reusable blocks of code.

A function is defined using `def`.

```
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

`n` is the parameter of the function.

`return` sends a value back from the function.

---

## Boolean Functions

A function can return a Boolean value such as `True` or `False`.

The `is_even()` function can be written as:

```
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

Since `n % 2 == 0` already evaluates to either `True` or `False`, this can be simplified to:

```
def is_even(n):
    return n % 2 == 0
```

The shorter version works because the comparison itself produces the Boolean value.

---

## Conditional Expressions

Python allows a simple `if`/`else` decision to be written on one line.

For example:

```
def is_odd(n):
    return False if n % 2 == 0 else True
```

This means:

> Return `False` if `n` is even; otherwise return `True`.

This is called a conditional expression or ternary expression.

A normal `if`/`else` can sometimes be easier to read, especially for more complicated logic.

---

## Functions Calling Functions

One function can call another function.

For example:

```
def main():
    f = int(input("Whats f? "))
    if is_even(f):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()
```

The program starts by calling `main()`.

`main()` gets the user's input and then calls `is_even()` to determine whether the number is even.

---

## `match` and `case`

`match` and `case` can be used to compare a value against multiple possible patterns.

For example:

```
match outworldy:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

Python checks each `case` until it finds one that matches the value.

---

## Catch-All Case: `_`

In a `match` statement:

```
case _:
```

`_` is used as a catch-all case.

It means:

> Whatever case has not already been handled.

For example:

```
match outworldy:
    case "Harry":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

If the name is not `"Harry"` or `"Draco"`, the `_` case runs.

---

## Multiple Patterns in `match`: `|`

The `|` operator can be used to match multiple values in the same case.

Instead of:

```
if outworldy == "Harry" or outworldy == "Hermione" or outworldy == "Ron":
    print("Gryffindor")
```

I can use:

```
match outworldy:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

Here, `|` acts similarly to `or`.

---

## `match` with Strings

`match` can also be used when the input needs to match several possible string representations.

For example:

```
answer = input("What is the answer to the Great Question of Life, The Universe, and Everything? ")
answer = answer.strip().title()

match answer:
    case "42" | "Forty-Two" | "Forty Two":
        print("Yes")
    case _:
        print("No")
```

`.strip()` removes whitespace from the beginning and end of the input.

`.title()` capitalizes the first letter of each word.

This allows inputs such as:

```
42
Forty-Two
Forty Two
```

to be handled by the same `case`.

---

## `.startswith()`

`.startswith()` checks whether a string begins with a specific sequence of characters.

For example:

```
greeting = input("Greeting: ")
greeting = greeting.strip().lower()

if greeting.startswith("hello"):
    print("0$")
elif greeting.startswith("h"):
    print("20$")
else:
    print("100$")
```

If the greeting starts with `"hello"`, the program prints `0$`.

If it does not start with `"hello"` but does start with `"h"`, it prints `20$`.

Otherwise, it prints `100$`.

`.startswith()` returns either `True` or `False`.

For example:

```
greeting.startswith("hello")
```

asks:

> Does `greeting` start with `"hello"`?

---

## Key Takeaways

* `if`, `elif`, and `else` are used for conditional logic.
* `==` checks equality while `=` assigns a value.
* `!=` checks whether two values are different.
* `and` requires both conditions to be true.
* `or` requires at least one condition to be true.
* `%` gives the remainder after division.
* `%` can be used to determine whether a number is even or odd.
* Python supports chained comparisons such as `90 <= score <= 100`.
* Conditions can sometimes be simplified by relying on Python's top-to-bottom evaluation.
* Functions are defined using `def`.
* `return` sends a value back from a function.
* Functions can return Boolean values.
* Conditional expressions allow simple `if`/`else` logic to be written in one expression.
* One function can call another function.
* `match` and `case` can be used to match values against different patterns.
* `case _` is the catch-all case.
* `|` allows multiple patterns to be handled by the same `case`.
* `.strip()` removes whitespace from the beginning and end of a string.
* `.title()` capitalizes the first letter of each word.
* `.startswith()` checks whether a string begins with a specific sequence of characters.
