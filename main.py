# menu of the coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "americano": {
        "ingredients": {
            "water": 100,
            "coffee": 18,
        },
        "cost": 1.85,
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


def show_menu_and_order():
    """ Shows machine menu including prices and lets the user order drink; returns order"""
    print("\n-- Drinks available --")
    i = 1
    menu = []
    for drink in MENU:
        print(f"{i}: {drink:<15} ${MENU[drink]['cost']:>5.2f}")
        i += 1
        menu.append(drink)
    valid_choice = False
    while not valid_choice:
        order_number_str = input("What drink would you like?\nPlease enter the corresponding number: ")
        if order_number_str.isnumeric():
            order_number = int(order_number_str)
            if order_number <= len(menu):
                return menu[order_number - 1]
            elif order_number in service_codes:
                return order_number
            else:
                print("Sorry, your choice is not valid.")
        else:
            print("Sorry, your choice is not valid.")


def turn_machine_off():
    """ Prints report - actual resources and earned money; returns False - turns machine off """
    print_report()
    print("-- The machine is now off --")
    return False


def check_resources(order):
    """ Checks if there are enough resources for the selected drink; returns True / False """
    for ingredient in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}..")
            return False
    print(f"Your choice is {order}, the price is ${MENU[order]['cost']:.2f}")
    return True


def final_resources_check(resources):
    """ Checks resources after the drink is made; if some ingredient is depleted, turns machine off (returns False) """
    if resources['water'] == 0 or resources['milk'] == 0 or resources['coffee'] == 0:
        print("Sorry, some resources are now completely depleted.\nThe machine will turn off now.")
        return turn_machine_off()
    else:
        return True


def top_up_resources():
    """ Tops up all the resources """
    global resources
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("-- Resources are topped up --")
    print_report()


def process_coins():
    """ Successively asks for coins from the list, adds to the total; returns total money inserted """
    money = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}
    total_money_inserted = 0
    print("-- Please insert coins --")
    for coin in money:
        number_of_coins = int(input(f"How many {coin} (${money[coin]:.2f})? "))
        total_money_inserted += number_of_coins * money[coin]
        print(f" The total is: ${total_money_inserted:.2f}")
    return total_money_inserted


def check_money(total_money_inserted, order):
    """ Checks if money inserted is sufficient; if not - refunds money and returns False, if yes - returns True """
    if MENU[order]['cost'] > total_money_inserted:
        print(f"Sorry that's not enough money. ${total_money_inserted:.2f} refunded.")
        return False
    else:
        return True


def prepare_drink(order, resources, cash_earned):
    """ Prepares drink, deducts resources, adds money to the earned cash """
    resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
    if "milk" in MENU[order]['ingredients']:
        resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
    cash_earned += MENU[order]['cost']
    return resources, cash_earned


def return_change(total_money_inserted, order):
    """ Returns change """
    change = total_money_inserted - MENU[order]['cost']
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    return change  # may be used later


def print_report():
    """ Prints report of resources and cash earned """
    print("\n-- Current state of resources --")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Cash earned: ${cash_earned}")


machine_on = True
cash_earned = 0
service_codes = [333, 666, 999]

while machine_on:
    order = show_menu_and_order()
    if order == 333:  # report
        print_report()
    elif order == 666:  # off
        print("Going to turn off.")
        machine_on = turn_machine_off()
    elif order == 999:  # top up
        top_up_resources()
    else:
        if check_resources(order):
            total_money_inserted = process_coins()
            if check_money(total_money_inserted, order):
                resources, cash_earned = prepare_drink(order, resources, cash_earned)
                print(f"\nHere is your ☕ {order}.")
                return_change(total_money_inserted, order)
        machine_on = final_resources_check(resources)
