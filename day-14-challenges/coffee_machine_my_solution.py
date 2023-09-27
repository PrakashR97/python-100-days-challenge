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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
print(MENU["latte"]["ingredients"])


def printReport(resource):
    milk = resource["water"]
    water = resource["water"]
    coffee = resource["coffee"]
    money = resource["money"]
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}$")


def checkResource(resource, menu, drinks):
    if drinks == 'espresso':
        if resource["water"] > menu["water"] \
                and resource["coffee"] > menu["coffee"]:
            return 0
        else:
            return 1
    else:
        if resource["water"] > menu["water"] and resource["milk"] > menu["milk"] \
                and resource["coffee"] > menu["coffee"]:
            return 0
        else:
            return 1


switch_on = True


def makeCoffee(resource, menu, drinks):
    print(menu)
    if drinks == 'espresso':
        resource["water"] -= menu["water"]
        resource["coffee"] -= menu["coffee"]
    else:
        resource["water"] -= menu["water"]
        resource["milk"] -= menu["milk"]
        resource["coffee"] -= menu["coffee"]


printReport(resources)
while switch_on:
    off_or_on = input("Do you want to off the machine?").lower()
    if off_or_on == 'yes':
        switch_on = False
        print("Thanks for using coffee machine. Bye!!")
        break
    options = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if options == 'report':
        printReport(resources)
    elif options == "latte" or "espresso" or "cappuccino":
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        if checkResource(resources, MENU[options]["ingredients"], options) == 0:
            amount = (quarters * 0.25) + (dimes * 0.10) + (0.05 * nickels) + (0.01 * pennies)
            change = amount - MENU[options]["cost"]
            resources["money"] += MENU[options]["cost"]
            if change >= 0:
                makeCoffee(resources, MENU[options]["ingredients"], options)
                print(f"Here is ${round(change, 2)} in change")
                print(f"Here is your {options} enjoy!!")
            else:
                print("Sorry! you don't have not enough money")
        else:
            print("Sorry there is not enough water.")
