# Python Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Store anything
# myset = {"apple", "banana", "cherry"}

# Access Items
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# Add Items
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# Add Sets
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# Remove Item
# thisset = {"apple", "banana", "cherry"}
#  1. thisset.remove("banana")
#  2. thisset.discard("banana")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Keep ONLY the Duplicates
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# Keep All, But NOT the Duplicates
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

# Diffrence
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)