# coffee_machine.py

# ---------------- MENU DATA ---------------- #
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

# ---------------- RESOURCES ---------------- #
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

# ---------------- FUNCTIONS ---------------- #

def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def is_resource_sufficient(order_ingredients, resources):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            return False, item
    return True, ""


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))  # $0.25
    dimes = int(input("How many dimes? "))        # $0.10
    nickels = int(input("How many nickels? "))    # $0.05
    pennies = int(input("How many pennies? "))    # $0.01
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return round(total, 2)


def handle_transaction(inserted_money, drink_cost, resources):
    if inserted_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(inserted_money - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True


def make_coffee(drink_name, order_ingredients, resources):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


# ---------------- MAIN PROGRAM ---------------- #

def coffee_machine():
    machine_on = True

    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            machine_on = False

        elif choice == "report":
            print_report(resources)

        elif choice in MENU:
            drink = MENU[choice]
            ingredients = drink["ingredients"]
            cost = drink["cost"]

            # 1. Check resources
            sufficient, lacking_item = is_resource_sufficient(ingredients, resources)
            if not sufficient:
                print(f"Sorry there is not enough {lacking_item}.")
                continue

            # 2. Process payment
            payment = process_coins()

            # 3. Verify transaction
            if handle_transaction(payment, cost, resources):
                # 4. Make the coffee
                make_coffee(choice, ingredients, resources)

        else:
            print("Invalid choice. Please select from espresso, latte, cappuccino.")

# Entry point
if __name__ == "__main__":
    coffee_machine()
