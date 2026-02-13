from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# Andy's instances
person1 = SavingsAccount("Andy", 1000, 10, 0.05)

# Caiman's instance
person2 = CheckingAccount("Caimen", 4000, 10, 420, 985)

# Test scenario User opening checking account and withdraw
# Scenario 1: Under Limit
person2.transfer_with_limit(1000)
print("----------------------------")
#Scenario 2: Over Limit
person2.transfer_with_limit(2300)
print("----------------------------")

