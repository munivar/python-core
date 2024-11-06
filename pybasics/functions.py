# Python Functions
# def my_function():
#   print("Hello from a function")

# my_function()

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments, **kwargs
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(x):
#   return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def myfunction():
#   pass

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(7)