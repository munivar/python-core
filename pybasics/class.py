# Python Classes

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("Dk",23)
# p1.myfunc()

# # Modify Object Properties
# p1.age = 40

# # Delete Object Properties
# del p1.age

# # Delete Objects
# del p1

# # The pass Statement
# class Person:
#   pass


# Python Iterators

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Class Polymorphism

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Drive!")
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Sail!")
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Fly!")
# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class
# for x in (car1, boat1, plane1):
#   x.move()