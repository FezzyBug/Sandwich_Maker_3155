import sandwich_maker
import data
import cashier

### Data ###
recipes = data.recipes
resources = data.resources
units = data.units

# Main loop - final changes required for commit to git
machine_runner = sandwich_maker.SandwichMaker(resources)
cashier = cashier.Cashier()

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report):").lower().strip()

    if choice == "off":
        break
    elif choice == "report":
        for ingredient, amount in machine_runner.machine_resources.items():
            print(f"{ingredient.capitalize()}: {amount} {units[ingredient]}")
    elif choice in ["small", "medium", "large"]:
        if machine_runner.check_resources(recipes[choice]["ingredients"]):
            print(f"The cost is ${recipes[choice]['cost']}.")
            coins_inserted = cashier.process_coins()
            if cashier.transaction_result(coins_inserted, recipes[choice]["cost"]):
                machine_runner.make_sandwich(choice, recipes[choice]["ingredients"])
    else:
        print("Invalid selection made.")

print("Machine is powering off.")
