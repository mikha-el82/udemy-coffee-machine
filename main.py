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
# TODO 1: prompt user to choose the drink
# TODO 1b: show user the price of drinks
# TODO 2: turn the machine off by typing 'off'
# FINISHED TODO 3: create function for printing a report
# TODO 4: check sufficient resources
# TODO 5: process coins
# TODO 6: check if transaction is successful - enough money inserted
# TODO 7: make coffee

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