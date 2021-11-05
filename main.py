# menu of the coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# coffee machine resources - can be modified
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# FINISHED TODO 1b: show user the price of drinks
def show_menu():
    print("\n-- Drinks available --")
    i = 1
    for drink in MENU:
        print(f"{i}: {drink:<15} ${MENU[drink]['cost']:>5.2f}")
        i += 1
    # TODO 1: prompt user to choose the drink
    order = input("What would you like? ")
    return order

# TODO 2: turn the machine off by typing 'off'

# TODO 4: check sufficient resources
def check_resources(drink):
    # water
    # milk
    # coffee
    print("Checking resources...")

# TODO 5: process coins
def process_coins():
    money = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}
    print("\n-- Please insert coins --")
    total = 0
    for coin in money:
        number_of_coins = int(input(f"How many {coin} (${money[coin]:.2f})? "))
        total += number_of_coins * money[coin]
        print(f"The total is: {total:.2f}")

# TODO 6: check if transaction is successful - enough money inserted
# TODO 7: make coffee

# FINISHED TODO 3: create function for printing a report
def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    print("\nCurrent state of resources")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

print_report()
show_menu()
process_coins()