from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
print("Welcome to Coffee Mahal . We are happy to have you as our customer")
while True:

    menuu = my_menu.get_items()
    customer_demand = input("What would you like to have ? " + menuu + "?")

    my_money_machine.report()
    my_coffee_maker.report()
