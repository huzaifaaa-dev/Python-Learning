# Day 1 — Video 1
# Learned: ...
x = int(input("Whats x? "))
y = int(input("Whats y? "))

if x < y:
    print("x is less than y")
else:  # Use elif (else if), more concise and saves space)
    if x == y: 
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

if c > d:
    print("c is greater than d")
else:
    if c < d:
        print("c is greater than d")
    if c == d:
        print("c is equal to d")
    