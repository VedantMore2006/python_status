import operations as ops

class EmptyValueError(Exception):
    pass

print("## OUR PERFECT CALCULATOR ##")

while True:
    try:
        choice = input("Enter operation (+, -, *, /) to calculator or type 'exit' to exit: ")
        if choice == "":
            raise EmptyValueError("The operation can't go empty")
    
        if choice.lower() == "exit":
            print("Exiting the Program!")
            break

        x = float(input("Enter First number: "))
        y = float(input("Enter seconf number: "))
            
        if choice == "+":
            print("Result:", ops.add(x, y))
        elif choice == "-":
            print("Result:", ops.sub(x, y))
        elif choice == "*":
            print("Result:", ops.multiply(x, y))
        elif choice == "/":
            print("Result:", ops.divide(x, y))
    except ValueError:
        print("Invalid input, please enter numbes only.")
    except ZeroDivisionError as e:
        print("Error:", e)
    except KeyboardInterrupt as ki:
        print("Interrepted By the user")
    