#AUTHOR: Rohit More
#Python3 Concept: Python classes and objects
# GITHUB: your https://github.com/Rohit-More
    
# A class is a blueprint using which we can create objects and objects are instance of a class.
#To create a class, use the keyword class:
  
 class MyClass:
  x = 5
 
#Now we can use the class named MyClass to create objects:
#Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

#The __init__() Function
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

#To understand the meaning of classes we have to understand the built-in __init__() function.

#All classes have a function called __init__(), which is always executed when the class is being initiated.

#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#The __init__() function is called automatically every time the class is being used to create a new object.
#Objects can also contain methods. Methods in objects are functions that belong to the object.

#Let us create a method in the Person class:

#Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

