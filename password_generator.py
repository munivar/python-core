# Ask user if they want to generate a password or not
# If yes, ask for password legth
# Generate Password and print password
# If initial response is no then exit the program

import string
import random

charactors = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    password_length = int(
        input("How long would you like your password to be? : "))
    random.shuffle(charactors)
    password = []

    for x in range(password_length):
        password.append(random.choice(charactors))
    random.shuffle(password)
    password = "".join(password)

    print("Your Password is : ", password)


option = input("Do you want to generate password? (Y/N) : ")

if option == "Y":
    generate_password()
elif option == "N":
    print("Program Ended")
    quit()
else:
    print("Invalid Input, Please input Yes(Y) or No(N)")
    quit()
