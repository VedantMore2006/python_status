import csv
from datetime import datetime as dt

command = input("Enter a command (add/show/exit): ").lower()

if command == "add":
    item_name = input("Enter item name: ")
    item_amount = int(input("Enter item amount: "))
    
    # here there will be function call for the expense adding
    print("Expense added")

elif command == "show":
    # this will contain the function to show the expenses