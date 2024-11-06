# Python Module
import funModule
import platform
import datetime
import json
import re
# rename module
import funModule as modulefun






# call another module fun
# funModule.greeting("Jonathan")

# Built-in Modules
# x = platform.system()
# print(x)






# Python Datetime
# x = datetime.datetime.now()
# print(x)

# https://www.w3schools.com/python/python_datetime.asp
# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))








# Python Math
# https://www.w3schools.com/python/python_math.asp

# Python JSON
# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# convert into JSON:
# y = json.dumps(x)
# the result is a JSON string:
# print(y)

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))

# Order the Result
# json.dumps(x, indent=4, sort_keys=True)





# Python RegEx

# The findall() Function
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# The search() Function
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())

# The split() Function
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# The sub() Function
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

# Match Object
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x) 