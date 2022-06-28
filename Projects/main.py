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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
def finally_make_coffee(drink_name,order_ingredients):
    """ Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")


def process_money(item):
    """ Returns the total from the coin inserted"""
    print("Please insert coins.")
    total = int(input("Enter the no of quarters")) * 0.25
    total += int(input("Enter the no of dimes")) * 0.1
    total += int(input("Enter the no of nickels")) * 0.05
    total += int(input("Enter the no of quarters")) * 0.01
    return total
def make_coffee(order):

    for item in MENU[order]["ingredients"]:
        if resources[item] <= MENU[order]["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved >=  drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is your {change}")
        global profit
        profit += drink_cost
        return True
    else:
        return False
        print("Sorry that's not enough money. Money refunded")
def continue_coffee():
    continue_having = True
    while(continue_having):

        user_demand = input("What would you like? (espresso/latte/cappuccino): ")
        if(user_demand == "report"):
            print(f"water: {resources['water']}")
            print(f"milk : {resources['milk']}")
            print(f"coffee : {resources['coffee']}")
            print(f"money : {profit}")
        elif(user_demand == "off"):
            continue_having = False
            return
        else:
            drink = user_demand
            if make_coffee(drink):
                payment = process_money(drink)
                if is_transaction_successful(payment, MENU[drink]["cost"]):
                    finally_make_coffee(drink,MENU[drink]["ingredients"])




continue_coffee()