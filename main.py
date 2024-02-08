### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

units = {
    "bread": "slice(s)",
    "ham": "slice(s)",
    "cheese": "ounce(s)"
}


### Complete functions ###
class SandwichMachine:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for ingredient, amount_needed in ingredients.items():
            if self.machine_resources[ingredient] < amount_needed:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: ")) * 1
        half_dol = int(input("How many half dollars?: ")) * 0.5
        quart = int(input("How many quarters?: ")) * 0.25
        nick = int(input("How many nickels?: ")) * 0.05
        return dollars + half_dol + quart + nick

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change >= 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

# Main loop
while True:
    machine_runner = SandwichMachine(resources)
    choice = input("What would you like? (small/ medium/ large/ off/ report):").lower().strip()

    if choice == "off":
        break
    elif choice == "report":
        for ingredient, amount in machine_runner.machine_resources.items():
            print(f"{ingredient.capitalize()}: {amount} {units[ingredient]}")
    elif choice in ["small", "medium", "large"]:
        if machine_runner.check_resources(recipes[choice]["ingredients"]):
            print(f"The cost is ${recipes[choice]['cost']}.")
            coins_inserted = machine_runner.process_coins()
            if machine_runner.transaction_result(coins_inserted, recipes[choice]["cost"]):
                machine_runner.make_sandwich(choice, recipes[choice]["ingredients"])
    else:
        print("Invalid selection made.")

print("Machine is powering off.")
