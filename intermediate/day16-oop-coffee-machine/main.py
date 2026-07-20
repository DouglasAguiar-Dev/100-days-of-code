from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of our classes 
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    # Get the menu items dynamically from the Menu object
    options = menu.get_items() 

    # Ask the user for their choice
    choice = input(f"What would you like? ({options}): ")

    # Handle the secret commands
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Call the report method on BOTH objects
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            # Check if we have enough resources
            if coffee_maker.is_resource_sufficient(drink):
                # Process the payment using the cost inside the drink object
                if money_machine.make_payment(drink.cost): 
                    # Brew the coffee by passing the whole drink object
                    coffee_maker.make_coffee(drink)
                
