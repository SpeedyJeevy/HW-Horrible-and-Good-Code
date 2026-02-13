class BankAccount:
    bank_name = "John Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance # Constructors

        # Adding Protected member Account Number
        self._account_number = account_number

        # Adding private member routing number
        self.__routing_number = routing_number

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


