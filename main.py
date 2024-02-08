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


    def process_coins(self):


    def transaction_result(self, coins, cost):


    def make_sandwich(self, sandwich_size, order_ingredients):


# Main loop
while True:
    machine_runner = SandwichMachine(resources)
    choice = input("What would you like? (small/ medium/ large/ off/ report):").lower().strip()

    if choice == "off":
        break
    elif choice == "report":

    elif choice in ["small", "medium", "large"]:

    else:
        print("Invalid selection made.")

print("Machine is powering off.")