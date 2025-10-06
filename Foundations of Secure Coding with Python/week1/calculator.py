num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
operation = input("Enter '+' for addition\n '-' for subtraction\n '*' for multiplication\n '/' for divide\n-->")
if operation == '+':
    print(f"Addition of {num1} and {num2} is {num1 + num2}")
elif operation == '-':
    print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
elif operation == '*':
    print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
else:
    print(f"The division of {num1} and {num2} is {num1 / num2}")