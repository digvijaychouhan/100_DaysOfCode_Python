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


def check_resources(userinput):
    checker = MENU[userinput]["ingredients"]
    # print(checker["water"])
    for res in checker:
        if checker[res] > resources[res]:
            print(f"Sorry there is not enough {res}.")
            return False
        else:
            continue
    return True


def calculate_total_money(quarters_q, dimes_q, nickles_q, pennies_q):
    total = quarters_q * 0.25 + dimes_q * 0.10 + nickles_q * 0.05 + pennies_q * 0.01
    return total


def compare_amount(total_entry, userinput):
    checker = MENU[userinput]["cost"]
    if total_entry < checker:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["cost"] = checker
        balance = total_entry - checker
        print(f"Here is ${round(balance, 2)} dollars in change.")
        return True


def prepare_coffee(coffee_choice):
    choice = MENU[coffee_choice]["ingredients"]
    for ingredient in resources:
        if ingredient in choice:
            resources[ingredient] -= choice[ingredient]
        else:
            continue


continue_program = True
while continue_program:
    user_input = input("What would you like?(espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        continue_program = False
# TODO: 3. Print report
    elif user_input == "report":
        for item in resources:
            if item == "water" or item == "milk":
                print(f"{item.title()}: {resources[item]}ml")
            elif item == "coffee":
                print(f"{item.title()}: {resources[item]}g")
            else:
                print(f"{item.title()}: ${resources[item]}")
# TODO: 4. Check resources sufficient?
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        res_status = check_resources(user_input)
        if res_status:
            print("Please insert coins.")
            # TODO: 5. Process coins
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_entered = calculate_total_money(quarters, dimes, nickles, pennies)
            # TODO: 6. Check transaction successful?
            if compare_amount(total_entered, user_input):
                # TODO: 7. Make Coffee
                prepare_coffee(user_input)
                print(f"Here is your {user_input}. ☕ Enjoy!")
    else:
        print("Please select a valid coffee flavour.")
