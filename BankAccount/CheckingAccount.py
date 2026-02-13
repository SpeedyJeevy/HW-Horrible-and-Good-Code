# Checking Account with Limitation - Caimen
# Savings Account with Interest - Andy

import BankAccount

class CheckingAccount(BankAccount):
    _account_number = 4
    __routing_number = 985
    # Protected members.

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance)
        # Pulls from BankAccount when object is created.

    def transfer_with_limit(self, amount):
        limit = 2000.0
        # Limit for transactions

        print("Account Number: {account_number}\n")
        print("Routing Number: {routing_number}\n")

        print("/////////////////////////\n")
        print("THANK YOU FOR USING {BankAccount.bank_name}\n")
        print("/////////////////////////\n")

        if amount > limit:
            print("Transaction declined. (Transfer limit reached)")
            return
        #Do nothing.
        else:
            print("Transaction approved. ${amount} has been deducted from your account.")
            return



