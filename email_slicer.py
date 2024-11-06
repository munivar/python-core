# Slicing Email in Python !!
def main():
    print("Email Slicer in Python")

    emailInput = input("Enter Email Address: ")

    # best for spliting things ->> return a list of splitted item
    splited = emailInput.split("@")
    # showing error if input field has doble "@"
    (username, domain) = emailInput.split("@")
    # showing error if input field has double "."
    (domain, extension) = domain.split(".")

    print("username ->> ", username)
    print("domain ->> ", domain)
    print("extension ->> ", extension)
    print("splitted ->> ", splited)


main()
