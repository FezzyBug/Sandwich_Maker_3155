class Cashier:

    def __init__(self):
        pass

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
