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
        bread_required = ingredients.get("bread") # Bread Order Amount
        ham_required = ingredients.get("ham") # Ham Order Amount
        cheese_required = ingredients.get("cheese") # Cheese Order Amount

        """Returns True when order can be made, False if ingredients are insufficient."""
        if resources.get("bread") < bread_required:
            print("Sorry there is not enough bread\n")
            return False
        if resources.get("ham") < ham_required:
            print("Sorry there is not enough ham\n")
            return False
        if resources.get("cheese") < cheese_required:
            print("Sorry there is not enough cheese\n")
            return False

        else: return True # Sufficient Materials

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
        if coins >= cost:
            return True
        else:
            return False
        # Cost in the interactable part will be process_coins()


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###