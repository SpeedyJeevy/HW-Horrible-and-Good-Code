operations = input("Please select one of the arithmetic operations: + , - , * , or / ")

num1 = float(input("Please enter your first number: "))

num2 = float(input("Please enter your second number: "))

if operations == "+":
    calculation = num1 + num2


elif operations == "-":
    calculation = num1 - num2


elif operations == "*":
    calculation = num1 * num2


elif operations == "/":
    calculation = num1 / num2

print(calculation)