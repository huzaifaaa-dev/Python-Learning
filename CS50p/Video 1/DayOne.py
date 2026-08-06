# Day 1 — Video 1
# Learned: ...
x = int(input("Whats x? "))
y = int(input("Whats y? "))

if x < y:
    print("x is less than y")
else:  # Use elif (else if), more concise and saves space)
    if x == y:  # == means "equal to" # = means assignment
        print("x is equal to y")
    if x > y:
        print("x is greater than y")

a = int(input("Whats a? "))
b = int(input("Whats b? "))

if a > b:
    print("a is bigger than b")
elif a < b:
    print("a is smaller than b")
elif a == b:
    print("a is equal to b")

c = int(input("Whats c? "))
d = int(input("Whats d? "))

if c > d or c < d:
    print("c is not equal to d")
else:
    print("c is equal to d")

if c != d:
    print("c is not equal to d")
else:
    print("c is equal to d")

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score > 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade F")

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
# Continues like so

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
# Continues like so

e = int(input("Whats e? "))

if e % 2 == 0:
    print("Even")
else:
    print("Odd")

def main():
    f = int(input("Whats f? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    return False if n % 2 == 0 else True

def is_learning(n):
    return n % 2 == 0

main()