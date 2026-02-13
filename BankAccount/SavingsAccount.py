# Savings Account with interest - Andy Choo
from BankAccount import BankAccount

# Savings Account subclass with interest rate
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print("New Balance after interest is: $" + str(self.current_balance))