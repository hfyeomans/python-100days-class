
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO Check resources are sufficient from above resources


# TODO define money drawer
money_drawer = 0

# TODO Check transaction successful
# f not enough money refund money and go back to "what would you like" prompt


def transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change -> ${change}")
        # TODO put money in money drawer
        global money_drawer
        money_drawer += drink_cost
        return True
    else:
        print("Insufficient funds deposited")
        return False


def sufficient_resources(order_resources):
    for item in order_resources:
        if order_resources[item] > resources[item]:
            print(f"There is not enough {item}.")
            return False
    return True

# TODO Process coins
# TODO define money
# TODO count money


def coins():
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * quarter
    total += int(input("How many dimes?: ")) * dime
    total += int(input("How many nickles?: ")) * nickle
    total += int(input("How many pennies?: ")) * penny
    return total

# TODO Make Coffee


def make_coffee(drink, ingredients):
    # TODO take resources from milk/coffee
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


def coffee():
    # TODO starting money
    coffee_on = True
    while coffee_on:
        # TODO prompt user for what they'd like
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # TODO turn off coffee machine - end program
        if selection == "off":
            coffee_on = False
        # TODO Print report - resources # TODO format report
        elif selection == "report":
            print(f"Water:  {resources['water']}ml")
            print(f"Milk:   {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money:  ${money_drawer}")
        else:
            drink = MENU[selection] # makes it so I don't have to do MENU[selection]["example"]
            if sufficient_resources(drink["ingredients"]):
                payment = coins()
                if transaction_success(payment, drink["cost"]):
                    make_coffee(selection, drink["ingredients"])


coffee()










