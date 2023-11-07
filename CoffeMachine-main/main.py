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

def is_resource(order_ingredients):
    """it returns true when order cam be made, False if ingredients aren't insuffient """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there's not enough {item}.")
            is_enough = False
    return is_enough

def porcess_coins():
    '''returns the total calculated frrom coins inserted'''
    print("please insert coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transcation_sucessfull(money_recived, cost_of_the_drink):
    """Return true when the payment is accepted or return false if the money isn't enough """
    if money_recived >= cost_of_the_drink:
        change =round(money_recived - cost_of_the_drink, 2)
        print(f"There you go you can take your change {change} 😊😊😊")
        global profit
        profit += cost_of_the_drink
        return True
    else:
        print("Sorry money is not enough")
        return False

def make_coffee(drink_name, order_ingredients ):
    """Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients
    print(f"Here is your {drink_name}🍺 enjoy😋😋 ")


is_on = True
while is_on:
    choice = input("What would you like?? (espresso, latte, cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == "report":
       print( f"Water: {resources['water']} ml")
       print( f"Milk: {resources['milk']} ml")
       print( f"Coffee: {resources['coffee']}g")
       print( f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource(drink["ingredients"]):
            payment = porcess_coins()
            if is_transcation_sucessfull(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
