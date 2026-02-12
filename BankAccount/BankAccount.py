class BankAccount:
    bank_name = "John Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance # Constructors


    def deposit(self, amount): # You need to add self in the parameter every time.
        self.current_balance += amount # Adds amount to current balance.

    def withdraw(self, amount):
        if amount > self.minimum_balance:
            print("You can't withdraw that much!")
        else:
            self.current_balance -= amount # Subtracts from current bank account balance.

    def print_customer_information(self):
        print("THANK YOU FOR CHOOSING ", self.bank_name, "\n")

        print("Customer Name: ", self.customer_name, "\nCurrent Balance: ", self.current_balance)

# Savings Account subclass with interest rate
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest

guy = BankAccount("Guy", 420, 420)
bro = BankAccount("Bro", 800, 800)

guy.print_customer_information()

print("\n////////////////////////////////////")

bro.print_customer_information()
print("\nTest subtracting some money:")
bro.withdraw(900) # Expected: "You can't withdraw that much!"
print("\n")
bro.print_customer_information()

print("\n////////////////////////////////////")
print("\nTesting PROPER money subtraction:")
bro.withdraw(100)
print("\n")
bro.print_customer_information() # Expected: 700
