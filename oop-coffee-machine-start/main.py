from random import choice
from tkinter.tix import Meter

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
current_resources = CoffeeMaker()
profit = MoneyMachine()
# drink_choice = input(f"What would you like? ({my_coffee.get_items()}): ")
is_on = True

while is_on:
    drink_choice = input(f"What would you like? ({menu.get_items()}): ")
    if drink_choice == "off":
        print("Powering off..")
        is_on = False
    elif drink_choice == "report":
        current_resources.report()
        profit.report()
        # is_on = False
    else:
        drink = menu.find_drink(drink_choice) #drink is MenuItem
        # print(drink)
        if current_resources.is_resource_sufficient(drink):
            if profit.make_payment(drink.cost):
                current_resources.make_coffee(drink)

