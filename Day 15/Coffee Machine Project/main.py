# Coffee Machine Menu and Resources
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100}

def check_resources(ingredients):
    """Check if enough resources are available for the selected drink."""
    for item, required_amount in ingredients.items():
        if required_amount > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def insert_coins():
    """Prompt the user to insert coins and calculate the total."""
    print("Insert coins:")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

def process_payment(received, cost):
    """Process payment and provide change if necessary."""
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Change: ${change}")
        global profit
        profit += cost
        return True
    print("Insufficient funds. Money refunded.")
    return False

def prepare_coffee(name, ingredients):
    """Prepare the coffee by deducting ingredients from resources."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here's your {name} ☕. Enjoy!")

def report_status():
    """Display current resource and profit status."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")

def coffee_machine():
    """Main loop for the coffee machine."""
    running = True
    while running:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            running = False
        elif user_choice == "report":
            report_status()
        elif user_choice in MENU:
            selected_drink = MENU[user_choice]
            if check_resources(selected_drink["ingredients"]):
                payment = insert_coins()
                if process_payment(payment, selected_drink["cost"]):
                    prepare_coffee(user_choice, selected_drink["ingredients"])
        else:
            print("Invalid selection. Please try again.")

# Start the coffee machine
coffee_machine()
