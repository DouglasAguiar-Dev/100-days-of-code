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

def is_resource_sufficient(order_ingredients):
    """check if resources are sufficient or not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """return the total calculate from coins inserted."""
    print("Please insert coins.")
    pennies = int(input("how many pennies?: "))
    nickles = int(input("how many nickles?: "))
    dimes = int(input("how many dimes?: "))
    quarters = int(input("how many quarters?: "))
    total = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received- drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
#Add this to track the money the machine makes!
profit = 0

# Add this to track if the machine is ON or OFF
turn_on = True

while turn_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    # Secret word to turn off the Coffee machine
    if choice == "off":
        turn_on = False
    # Secret word to see the report about the Coffee Machine
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])