from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# Andy's instances
person1 = SavingsAccount("Andy", 1000, 10, 0.05, 690, 123)
person100 = SavingsAccount("Smith", 100, 10, 0.05, 790, 124)

# Caiman's instance
person2 = CheckingAccount("Caimen", 4000, 10, 420, 985)
person200 = CheckingAccount("Guy", 3200, 10, 360, 986)

# Test scenario User opening checking account and withdraw
# Scenario 1: Under Limit
person2.transfer_with_limit(1000)
person2.transfer_with_limit(16)
print("----------------------------")
#Scenario 2: Over Limit
person2.transfer_with_limit(2300)
person200.transfer_with_limit(3200)
print("----------------------------")

# Testing SavingsAccount interest feature
person1.add_interest()
person100.add_interest()