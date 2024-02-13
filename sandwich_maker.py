class SandwichMaker:
    resource = {}

    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for ingredient, amount_needed in ingredients.items():
            if self.machine_resources[ingredient] < amount_needed:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")