# Faulty Calculator in Python !!
def faultyCalculator():
    while True:
        try:
            x = int(input("Enter your First Number: "))
            break
        except:
            print("That's not a valid option!")

    while True:
        try:
            y = int(input("Enter your Second Number: "))
            break
        except:
            print("That's not a valid option!")

    while True:
        try:
            z = input(
                "Enter (+) for add, (-) for minus, (*) for multiply, (/) for divide, (e) for exit: ")
            break
        except:
            print("That's not a valid option!")

    if x == 45 and y == 3 and z == "*":
        print("Total is 555")
    elif x == 56 and y == 9 and z == "+":
        print("Total is 77")
    elif x == 56 and y == 6 and z == "/":
        print("Total is 4")
    else:
        if z == "+":
            total = x + y
            print("Total is " + str(total))
        elif z == "-":
            total = x - y
            print("Total is " + str(total))
        elif z == "*":
            total = x * y
            print("Total is " + str(total))
        elif z == "/":
            total = x / y
            print("Total is " + str(total))
        elif z == "e":
            print("Exited")
            exit()
        else:
            print("Invalid Operator")


# call function
faultyCalculator()
