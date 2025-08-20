def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {"+": add, "-": sub, "*": multiply, "/": divide}
    n1 = float(input("Num 1 : "))
    for i in operations:
        print(i)
    going = True
    while going:
        operation_symbole = input("Pick the operation u wnat to perform : ")
        n2 = float(input("Enter another number : "))
        calculation_function = operations[operation_symbole]
        answer = calculation_function(n1, n2)
        print(answer)
        decision = input(
            "Wanna continue calculating with the last answer then type 'y'\nWnat to start fresh type 'n'\nTo exit type 'e'\nYour Choice :- "
        )
        if decision == "y":
            n1 = answer
        elif decision == "n":
            calculator()
        else:
            return print("Thank You")


calculator()
