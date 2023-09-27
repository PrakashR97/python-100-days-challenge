from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

switch_on = True

c_m = CoffeeMaker()
m_i = Menu()
m_m = MoneyMachine()

while switch_on:
    options = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if options == 'report':
        c_m.report()
    elif options == 'latte' or 'espresso' or 'cappuccino':
        drink = m_i.find_drink(options)
        # money = m_m.process_coins()
        m_m.make_payment(drink.cost)
        c_m.report()
        can_make = c_m.is_resource_sufficient(drink)
        if can_make:
            c_m.make_coffee(drink)
        c_m.report()

