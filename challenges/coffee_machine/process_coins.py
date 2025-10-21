import resources as rs
pennies = 0.01
nickels = 0.05
dimes = 0.1
quarter = 0.25
needed_amount = 2.5
total_amount= 0
no_of_pennies = int(input("How many pennies do u have : "))
for i in range(0, no_of_pennies) :
    total_amount += pennies
no_of_nickels = int(input("How many nickels do u have : "))
for i in range(0, no_of_nickels) :
    total_amount += nickels
no_of_dimes = int(input("How many demis do u have : "))
for i in range(0, no_of_dimes) :
    total_amount += dimes
no_of_quarters = int(input("How many quarters do u have : "))
for i in range(0, no_of_quarters) :
    total_amount += quarter

if total_amount > needed_amount :
    change = total_amount - needed_amount
    print(f"The actual amount needed is {needed_amount}.\nYou have {total_amount}.\nHere are your change {change}.")
    print("Thankyou for your purchase!!")
if total_amount < needed_amount:
    print(f"The needed amount is {needed_amount}, You only have {total_amount}\nYou still need {needed_amount - total_amount}\nMoney refunded")
