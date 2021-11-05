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
    "water": 300,  # 300
    "milk": 200,
    "coffee": 100,
}

# FINISHED TODO 1b: show user the price of drinks
def show_menu_and_order():
    print("\n-- Drinks available --")
    i = 1
    for drink in MENU:
        print(f"{i}: {drink:<15} ${MENU[drink]['cost']:>5.2f}")
        i += 1
    # FINISHED TODO 1: prompt user to choose the drink
    order = input("What would you like? ")
    return order

# FINISHED TODO 2: turn the machine off by typing 'off'
def turn_machine_off():
    print_report()
    print("-- The machine is now off --")
    machine_on = False
    return machine_on

# FINISHED TODO 4: check sufficient resources
def check_resources(order):
    if resources['water'] < MENU[order]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    elif "milk" in MENU[order]['ingredients']:
        # print("Checking milk.")
        if resources['milk'] < MENU[order]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    elif resources['coffee'] < MENU[order]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    else:
        print(f"Enough ingredients to make {order}.")
        return True

def final_resources_check(resources):
    # print("Checking resources...")
    if resources['water'] == 0 or resources['milk'] == 0 or resources['coffee'] == 0:
        print("Sorry, some resources are now completely depleted.\nThe machine will turn off now.")
        return turn_machine_off()
    else:
        machine_on = True
        return machine_on

# FINISHED TODO 5: process coins
def process_coins():
    money = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}
    total_money_inserted = 0
    print("\n-- Please insert coins --")
    for coin in money:
        number_of_coins = int(input(f"How many {coin} (${money[coin]:.2f})? "))
        total_money_inserted += number_of_coins * money[coin]
        print(f"The total is: {total_money_inserted:.2f}")
    return total_money_inserted

# FINISHED TODO 6: check if transaction is successful - enough money inserted
def check_money(total_money_inserted, order):
    # print(MENU[order]['cost'])
    # print(total_money_inserted)
    if MENU[order]['cost'] > total_money_inserted:
        print(f"Sorry that's not enough money. ${total_money_inserted:.2f} refunded.")
        return False
    else:
        return True

# FINISHED TODO 7: make coffee
def prepare_drink(order, resources, cash_earned):
    # print("Dispensing water.")
    resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
    if "milk" in MENU[order]['ingredients']:
        print("Dispensing milk.")
        resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
    # print("Dispensing coffee.")
    resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
    print(f"Price of the drink: {MENU[order]['cost']}")
    cash_earned += MENU[order]['cost']
    return resources, cash_earned

# FINISHED TODO 3: create function for printing a report
def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("\nCurrent state of resources")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Cash earned: ${cash_earned}")

# FINISHED TODO 8: return spare change
def return_change(total_money_inserted, order):
    change = total_money_inserted - MENU[order]['cost']
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
        total_money_inserted = 0
    return total_money_inserted # may be used later


machine_on = True
cash_earned = 0

while machine_on == True:
    # let the person order the drink
    # print(f"Is machine on? {machine_on}")
    order = show_menu_and_order()
    if order == "report":
        print_report()
    elif order == "off":
        print("Going to turn off.")
        machine_on = turn_machine_off()
    else:
        if check_resources(order):
            # process inserted coins
            # print("Going to prepare drink...")
            total_money_inserted = process_coins()
            # print(f"Total money you inserted: {total_money_inserted}")
            # check if there are enough resources and the inserted amount is enough for the drink
            # print(f"Resources OK: {check_resources(order)}.")
            # print(f"Money OK: {check_money(total_money_inserted, order)}.")
            if check_money(total_money_inserted, order):
                # print("All is OK.")
                # prepare drink and return left resources and earned money
                resources, cash_earned = prepare_drink(order, resources, cash_earned)
                print(f"\nHere is your ☕ {order}.")
                # return any spare change
                return_change(total_money_inserted, order)
        # print(f"\nCash earned up to now: ${cash_earned:.2f}")
        # print(f"\nCurrent state of resources: \n{resources}")
        machine_on = final_resources_check(resources)




