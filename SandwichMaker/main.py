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


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        bread_required = ingredients["bread"] # Bread Order Amount
        ham_required = ingredients["ham"] # Ham Order Amount
        cheese_required = ingredients["cheese"] # Cheese Order Amount

        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount_required in ingredients.items():
            if self.machine_resources[item] < amount_required:
                print("Sorry, there is not enough", item, ".")
                return False
        return True # Sufficient Materials

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        dollar = float(input("How many large dollars?\n"))
        half_dollar = float(input("How many half dollars?\n"))
        quarter = float(input("How many quarters?\n"))
        nickels = float(input("How many nickels?\n"))
        # Our amount of each item

        dollar_amount = dollar * 1
        half_dollar_amount = half_dollar * .5
        quarter_amount = quarter * .25
        nickels_amount = nickels * .05
        # Calculate appropriate values for quantities

        return dollar_amount + half_dollar_amount + quarter_amount + nickels_amount # Calculate the total amount.



    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins > cost:
            print("Here is $", coins - cost, "in change.\n")
            return True
        if coins == cost:
            return True
        else:
            print("Sorry that's not enough money. Money refunded.\n")
            return False
        # Coins in the interactable part will be process_coins()


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

        bread_amount = sandwich_size["bread"]
        ham_amount = sandwich_size["ham"]
        cheese_amount = sandwich_size["cheese"]
        # Variables for the amount of each dictionary entry for the sandwich size

        print("Enjoy your sandwich! Bon appetit!\n")

        order_ingredients["bread"] -= bread_amount
        order_ingredients["ham"] -= ham_amount
        order_ingredients["cheese"] -= cheese_amount
        # Deducting from ingredient amount

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwich_machine = SandwichMachine(resources) # Pulls from resource dictionary.

turn_off = False

while not turn_off:
    response = input("What would you like? (small/medium/large/off/report):\n")

    if response == "report":
        print("Bread: ", resources["bread"], "slice(s)\n")
        print("Ham: ", resources["ham"], "slice(s)\n")
        print("Cheese: ", resources["cheese"], "pound(s)\n")
        # Report of the remaining ingredients.

    if response == "off":
        turn_off = True
        break
        # Ends loop.

    if response == "small":
        if sandwich_machine.check_resources(recipes["small"]["ingredients"]): # Should return True if ingredients exist
            money = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(money, recipes["small"]["cost"]):
                # If it fits the cost, continue.
                sandwich_machine.make_sandwich(recipes["small"]["ingredients"], resources)
                # Make sandwich, deduct necessary items.
        else:
            continue # If not, get booted back to menu.

    if response == "medium":
        if sandwich_machine.check_resources(recipes["medium"]["ingredients"]):  # Should return True if ingredients exist
            money = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(money, recipes["medium"]["cost"]):
                # If it fits the cost, continue.
                sandwich_machine.make_sandwich(recipes["medium"]["ingredients"], resources)
                # Make sandwich, deduct necessary items.
        else:
            continue  # If not, get booted back to menu.


    if response == "large":
        if sandwich_machine.check_resources(recipes["large"]["ingredients"]):  # Should return True if ingredients exist
            money = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(money, recipes["large"]["cost"]):
                # If it fits the cost, continue.o
                sandwich_machine.make_sandwich(recipes["large"]["ingredients"], resources)
                # Make sandwich, deduct necessary items.
        else:
            continue  # If not, get booted back to menu.