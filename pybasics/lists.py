# Python Lists

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# List Legth
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# Access Items
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# Negative Indexing
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# Range of Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Change a Range of Item Values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# Insert Items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "watermelon")
# print(thislist)

# Append Items
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# Extend List
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# Remove Specified Item
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# Remove Specified Index
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# del keyword also removes the specified index

# Delete Index
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# Delete List
# thislist = ["apple", "banana", "cherry"]
# del thislist

# Clear the List
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# Loop Through a List
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Loop Through the Index Numbers
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# Using a While Loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# Looping Using List Comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# Sort List Alphanumerically
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# Sort Descending
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# Customize Sort Function
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# Case Insensitive Sort
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Copy a List
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# Join Two Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# Using Append
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)
# print(list1)

# Using Extend
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)