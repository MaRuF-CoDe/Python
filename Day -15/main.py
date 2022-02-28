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

def is_resource_sufficient(ingredients):
    for item in resources:
        if ingredients[item]>=resources[item]:
            print("Sorry there is not enough water.")
            return False
        return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters : "))*0.25
    total += int(input("How many dimess : "))*0.1
    total += int(input("How many nickels : "))*0.05
    total += int(input("How many pennies : "))*0.01
    return total

def  transaction_successful(money_rcv,drink_cost):
    if money_rcv >= drink_cost:
        change = round(money_rcv - drink_cost,2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(chose,ingredients):
    for items in ingredients:
        resources[items]-=ingredients[items]
    print(f"Here is your {chose}. Enjoy!")
 

is_on = True

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])