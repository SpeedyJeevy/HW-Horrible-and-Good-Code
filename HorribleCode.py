def addSub():
    function = input("Are you doing:\nA) Addition\nB) Subtraction")
    if function.lower() == "a":
        num1 = input("Enter a first number to add:\n")
        num2 = input("Enter a second number to add to your first number:\n")
        num1 = int(num1)
        num2 = int(num2)
        num3 = num2
        num3 += num1
        print("Your result is", str(num3))
    elif function.lower() == "b":
        num1 = input("Enter a first number (number being subtracted from):\n")
        num2 = input("Enter a second number (number being subtracted):\n")
        num1 = int(num1)
        num2 = int(num2)
        num3 = num1
        num3 -= num2
        print("Your answer is: " + str(num3))


while True:
    answer = input("What do you want to do?\nA) Addition/Subtraction\nB) Multiplication\nC Division\nD) Double\n")
    if answer.lower() == "a":
        addSub()

