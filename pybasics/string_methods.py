# Global Variables
# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()

# Strings are Arrays
# a = "Hello, World!"
# print(a[1])

# Looping Through a String
# for x in "banana":
#   print(x)

# String Length
# a = "Hello, World!"
# print(len(a))

# Check String
# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# Check if NOT
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# Slicing
# b = "Hello, World!"
# print(b[2:5])

# Slice From the Start
# b = "Hello, World!"
# print(b[:5])

# Slice To the End
# b = "Hello, World!"
# print(b[2:])

# Negative Indexing
# b = "Hello, World!"
# print(b[-5:-2])

# Upper Case
# a = "Hello, World!"
# print(a.upper())

# Lower Case
# a = "Hello, World!"
# print(a.lower())

# Remove Whitespace
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# Replace String
# a = "Hello, World!"
# print(a.replace("H", "J"))

# Split String
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# Format - Strings
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# Escape Character
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# Converts the first character to upper case
# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

# Converts string into lower case
# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# Returns a centered string
# txt = "banana"
# x = txt.center(20)
# print(x)

# Returns the number of times a specified value occurs in a string
# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x)

# Returns an encoded version of the string
# txt = "My name is Dk"
# x = txt.encode()
# print(x)

# Returns true if the string ends with the specified value
# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

# Sets the tab size of the string
# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(2)
# print(x)

# Searches the string for a specified value and returns the position of where it was found
# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)

# Formats specified values in a string
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# Searches the string for a specified value and returns the position of where it was found
# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)

# Returns True if all characters in the string are alphanumeric
# txt = "Company12"
# x = txt.isalnum()
# print(x)

# Returns True if all characters in the string are in the alphabet
# txt = "CompanyX"
# x = txt.isalpha()
# print(x)

# Returns True if all characters in the string are ascii characters
# txt = "Company123"
# x = txt.isascii()
# print(x)

# Returns True if all characters in the string are decimals
# txt = "1234"
# x = txt.isdecimal()
# print(x)

# Returns True if all characters in the string are digits
# txt = "50800"
# x = txt.isdigit()
# print(x)

# Returns True if the string is an identifier
# txt = "Demo"
# x = txt.isidentifier()
# print(x)

# Returns True if all characters in the string are lower case
# txt = "hello world!"
# x = txt.islower()
# print(x)

# Returns True if all characters in the string are numeric
# txt = "565543"
# x = txt.isnumeric()
# print(x)

# Returns True if all characters in the string are printable
# txt = "Hello! Are you #1?"
# x = txt.isprintable()
# print(x)

# Returns True if all characters in the string are whitespaces
# txt = "   "
# x = txt.isspace()
# print(x)

# Returns True if the string follows the rules of a title
# txt = "Hello, And Welcome To My World!"
# x = txt.istitle()
# print(x)

# Returns True if all characters in the string are upper case
# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)

# Joins the elements of an iterable to the end of the string
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# Returns a left justified version of the string
# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.")

# Converts a string into lower case
# txt = "Hello my FRIENDS"
# x = txt.lower()
# print(x)

# Returns a left trim version of the string
# txt = "     banana     "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite")

# Returns a translation table to be used in translations
# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))

# Returns a tuple where the string is parted into three parts
# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x)

# Returns a string where a specified value is replaced with a specified value
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

# Searches the string for a specified value and returns the last position of where it was found
# txt = "Mi casa, su casa."
# x = txt.rfind("casa")
# print(x)

# Searches the string for a specified value and returns the last position of where it was found
# txt = "Mi casa, su casa."
# x = txt.rindex("casa")
# print(x)

# Returns a right justified version of the string
# txt = "banana"
# x = txt.rjust(20)
# print(x, "is my favorite fruit.")

# Returns a tuple where the string is parted into three parts
# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("bananas")
# print(x)

# Splits the string at the specified separator, and returns a list
# txt = "apple, banana, cherry"
# x = txt.rsplit(", ")
# print(x)

# Returns a right trim version of the string
# txt = "     banana     "
# x = txt.rstrip()
# print("of all fruits", x, "is my favorite")

# Splits the string at the specified separator, and returns a list
# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# Splits the string at line breaks and returns a list
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

# Returns true if the string starts with the specified value
# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello")
# print(x)

# Returns a trimmed version of the string
# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# Swaps cases, lower case becomes upper case and vice versa
# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

# Converts the first character of each word to upper case
# txt = "Welcome to my world"
# x = txt.title()
# print(x)

# Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# mydict = {83:  80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))

# Converts a string into upper case
# txt = "Hello my friends"
# x = txt.upper()
# print(x)

# Fills the string with a specified number of 0 values at the beginning
# txt = "50"
# x = txt.zfill(10)
# print(x)