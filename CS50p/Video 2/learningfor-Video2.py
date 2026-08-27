# Here we Go!

print("meow")
print("meow")
print("meow")

i = 3
while i != 0:   # != means not equal to
    print("meow")
    i = i - 1

c = 1
while c <= 3:
    print("meow")
    c = c + 1

d = 0
while d < 3:
    print("meow")
    d += 1   # += is used for the same purpose as d = d + 1.

for e in [0, 1, 2]:  # for loop used for different ranges of values if values known.
    print("meow")

for b in range(3):  # range(3) gives the output = [0, 1, 2], identical to above, but cleaner and easier to write.
    print("meow")

for _ in range(3):    # Used to suggest this variable is required for the code to run, but we dont require the name.
    print("meow")

print("meow\n" * 3, end="")  # \n is used to say: Next line.
# end="" is used to prevent print from going to the next line.

n = int(input("Whats n? "))
if n < 0:
    n = int(input("Whats n? "))
    if n < 0:
        n = int(input("Whats n? "))

while True:    # while true means, run this code forever until break.
    n = int(input("Whats n? "))
    if n < 0:
        continue  # continue signals the loop to continue repeating from the beginning of the loop.
    else:
        break  # break ends the loop.

while True:
    n = int(input("Whats n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:   
        n = int(input("Whats n? "))
        if n > 0:
            return n  # use return to return a value.

def meow(n):
    for _ in range(n):
        print("meow")


main()

students = ["Hermione", "Harry", "Ron", "Draco"]

print(students[0])  # 0 is used since the first variable is always at 0, not 1, hence, Hermione is 0, Harry is 1, and so on.
print(students[1])
print(students[2])

for student in students:
    print(student)

# len tells you the length of a list.
for i in range(len(students)):  # This line of code means, for every number in range(len(students)), call that number i.
    print(students[i])

for i in range(len(student)):
    print(i, student[i])  # Prints the Index along with the value of whats stored in the Index.

for i in range(len(student)):
    print(i + 1, student[i]) 

# dict: Data Structure that allows you to associate one value with another.
# dict is TWO-DIMENSIONAL; unlike lists where you just have a set of values and their index number, in dict, you can assign, say, a word to its definition.
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# dict can be used to associate the student with the house.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student)

for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house" : "Slytherin", "Patronus": None}
]    # None used to literally nothing belongs in this part of the dictionary.

for student in students:
    print(student["name"], student(["house"]), student(["[patronus]"]), sep = ", ")

for _ in range(3):
    print("#")

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
    print("#\n" * height, end = "")

main()

def notmain():
    print_row(4)

def print_row(width):
    print("?" * width)

notmain()

def anothermain():
    print_square(3)

def print_square(size):

    # For each row in square.
    for i in range(size):

        # For each brick in row.
        for j in range(size):

            # Print brick.
            print("#", end="")

        print()

    for f in range(size):
        print("#" * size)

    for c in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)