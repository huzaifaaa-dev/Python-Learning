# Program to ask what the answer to the Great Question of Life, The Universe and Everything.
answer = input("What is the answer to the Great Question of Life, The Universe, and Everything? ")
answer = answer.strip().title()
match answer:
    case "42" | "Forty-Two" | "Forty Two":
        print("Yes")
    case _:
        print("No")