# Program that prompts the user for an arithmetic expression, calculates the outputs the result as a float value.
expression = input("Expression: ")
x,y,z = expression.split(" ")
match y:
    case "/":
        print(float(x) / float(z))
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(float(x) * float(z))
    case _:
        print("Please enter a valid expression.")