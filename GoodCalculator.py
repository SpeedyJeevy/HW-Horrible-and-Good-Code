# Taking input for the operation, and two numbers needed for computing
operations = input("Please select one of the arithmetic operations: + , - , * , or / ")

num1 = float(input("Please enter your first number: "))

num2 = float(input("Please enter your second number: "))

# Adding num1 and num2 then saving to calculation
if operations == "+":
    calculation = num1 + num2

# Subtracting num1 and num2 then saving to calculation
elif operations == "-":
    calculation = num1 - num2

# Multiplying num1 and num2 then saving to calculation
elif operations == "*":
    calculation = num1 * num2

# Dividing num1 and num2 then saving to calculation
elif operations == "/":
    calculation = num1 / num2

# Printing the calculated result
print(calculation)