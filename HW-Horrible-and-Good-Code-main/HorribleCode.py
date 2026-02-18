"""
This function adds and subtracts and junk.
"""

def add_sub():
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

"""
This is a function that does something.
"""

def mult_div():
    function = input("Are you doing:\nA) Multiplication\nB) Division")
    if function.lower() == "a":
        num1 = input("Enter a first number to multiply:\n")
        num2 = input("Enter a second number to multiply:\n")
        num1 = int(num1)
        num2 = int(num2)
        num3 = num2
        num3 *= num1
        print("Your result is ", str(num3))
    elif function.lower() == "b":
        num1 = input("Enter a first number to divide:\n")
        num2 = input("Enter a second number to divide:\n")
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            print("Can't divide by zero, dummy!")
        num3 = num1
        num3 /= num2
        print("Your result is ", str(num3)) # Result of the computation

    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠧⢭⡳⡘⢦⠱⡌⠦⡑⢦⡑⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠘⠟⣱⢊⠵⡘⢬⡱⢆⣍⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢠⡔⣦⣟⣿⣿⣿⣿⣗⣴⣠⡀⠀⠀⠈⢎⡱⢢⡱⢎⣌⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠀⠀⠀⢀⠤⡁⠆⣱⣻⡽⣿⣿⣿⣿⣿⣿⣯⣿⡧⣄⠀⠀⠀⢇⠧⣓⠮⡜⠀⠀⠀
⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⣭⠀⠀⠀⠠⣉⠂⠄⣴⢷⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⡽⣧⠀⠀⠀⣌⠳⣍⢾⣁⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠠⠁⠄⣜⠾⣽⣛⡾⣽⣻⢿⣿⣿⣿⣿⣿⣿⡿⣧⠀⠀⠀⠮⣝⢮⠷⣭⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠁⠀⠈⠙⠘⠣⠝⡲⢏⡟⠼⠉⠋⠉⠁⠋⠙⢻⡆⠀⠀⡟⣼⢫⣟⠂⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⡜⠀⢀⠤⠀⠀⠐⢠⣮⡆⠂⠁⠀⠀⢠⠀⠁⡠⢷⠀⠀⢻⡜⣧⠏⠀⠀⠀⠀
⠤⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠡⠀⠀⠄⠀⠀⠀⠀⢾⣽⣿⠄⠀⠁⠤⠖⠊⡕⠲⢿⠀⠒⠺⡜⢧⣿⠀⠀⠀⠀
⠀⢃⠘⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⢀⣀⢀⠀⠄⠀⠸⣿⠏⡼⣁⠐⢄⡀⠿⣹⡇⠈⠀⢠⠰⡉⡦⡜⠀⠀⠀⠀
⠂⠈⠒⠹⣿⣿⣿⣿⣿⣿⣿⠇⠀⡁⢎⢞⡹⠊⡑⢀⠈⡖⣿⡞⣥⢯⢁⡊⠙⠖⢫⣛⠞⢨⣿⢱⢏⡷⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⣀⠰⠈⠂⠀⠠⠐⠂⠌⠽⠶⡙⠊⣊⡮⡕⠢⠀⠁⢸⠈⣟⠩⢚⠼⡍⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡷⠀⢂⠄⡀⠀⠂⠄⠀⠐⢀⠤⠛⠈⢁⢀⠀⡠⠀⣄⠘⢈⡉⢝⢾⣱⠀⠀⠀⠀⠀
⠀⠀⠄⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⣇⡈⠒⠄⠀⠳⣦⣮⣰⡆⣤⣷⣵⡷⠏⣰⡑⠱⠠⣘⠦⡜⡱⢪⡗⠆⠀⠀⠀⠀
⠀⠈⡄⠀⠀⠀⢹⣿⣿⣿⣿⣿⣧⣿⣦⡈⠎⠄⡀⠈⠛⠻⠗⠿⠟⢣⣁⠐⣼⡥⠏⡰⢍⢂⠂⠉⠉⠀⠉⠀⠀⠀⠀
⠀⠡⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⢹⠟⠒⠈⠤⠐⠀⡈⠙⡒⠒⠛⠍⣂⣾⣽⡬⢐⠪⣁⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⠀⠀⠀⠀⠀⣻⣿⠿⠛⠋⠁⠀⡌⠂⠄⠀⠡⠂⡉⢖⡩⢏⡝⢯⣻⣬⡧⢁⠾⣆⢨⡟⡶⡠⣄⡀⠀⠀⠀⠀⠀
⠀⠈⠄⢀⡀⣤⠄⠉⢡⠀⠀⠂⡅⠘⠐⠠⠀⡀⠀⠡⠎⡼⣱⢧⠾⣿⡳⠃⠐⣄⠙⣯⢸⣿⣿⣿⣾⣿⣷⢤⣀⠀⠀
⡠⢔⠋⡋⠑⠀⠀⠠⠡⠀⢈⠡⡂⠈⠌⠀⠀⠄⠡⠀⠈⠲⠙⠎⠛⠃⠉⢠⢓⣸⢦⢤⣿⣻⣿⣿⣿⣿⣿⣿⣶⣷⣦
⠐⡈⠐⡀⠂⠀⠀⠀⡁⠂⡌⠰⠁⠀⠀⠂⠀⠈⠄⡁⠂⠄⡠⠀⠄⢂⡘⣬⢯⡿⣏⣯⣷⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿
"""
# Hey guys what are you doing later? I'll be in the Atkins library after the Software Engineering class.

"""
Just in case if somebody wants to multiply by two.
"""
def double():
    num1 = input("Enter a number to multiply by 2:\n")
    num1 = int(num1)
    num3 = num1
    num3 *= 2
    print("Your result is ", str(num3))


while True:
    answer = input("What do you want to do?\nA) Addition/Subtraction\nB) Multiplication/Division\nC) Double\n")
    if answer.lower() == "a":
        add_sub() # Addition or subtraction???
    elif answer.lower() == "b":
        mult_div() # Multiplication or division??
    elif answer.lower() == "c":
        double() # Multiply by two

