# Checking Account with Limitation - Caimen
# Savings Account with Interest - Andy

from BankAccount import BankAccount

class CheckingAccount(BankAccount):


    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        # Pulls from BankAccount when object is created.

    def transfer_with_limit(self, amount):
        limit = 2000.0
        # Limit for transactions


        print("/////////////////////////\n")
        print(f"THANK YOU FOR USING {BankAccount.bank_name}\n")
        print("/////////////////////////\n")

        if amount > limit:
            print("Transaction declined. (Transfer limit reached)")
            return
        #Do nothing.
        else:
            print(f"Transaction approved. ${amount} has been deducted from your account.")
            return