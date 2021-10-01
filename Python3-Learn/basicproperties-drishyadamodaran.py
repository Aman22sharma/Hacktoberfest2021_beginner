// AUTHOR: Drishya
// Python3 Concept: Basic python concepts
// GITHUB: https://github.com/drishyadamodaran


# Data types
#Let’s move to data types. The data structures in Python are dictionaries, tuples and lists. Sets can be found in the sets library that is available in all versions of Python from 2.5 onwards. Lists are similar to one-dimensional arrays, although you can also have lists of other lists. Dictionaries are essentially associative arrays or hash tables. Tuples are one-dimensional arrays. Now, Python arrays can be of any type, and the types are always zero. Negative numbers start from the end to the beginning, and -1 is the last item. Variables can also point to functions. Here is an example of the usage: You can use the colon to access array ranges. If you leave the start index empty, the interpreter assumes the first item, so the end index assumes the last item. Negative indexes count from the last item, so -1 is seen as the last item. Here is an example:
#Adding the third parameter will see the Python step in the N item increments instead of one in the last line. For instance, in the above sample code, the first item is returned and then the third, so items zero and two in zero-indexing.

#Strings
#Let’s move on to strings. Python strings can either use single or double quotation marks, and you can use quotation marks of one kind in a string using another kind, so the following is valid:

#**“This is a ‘valid’ string.”**

#Multi-strings are enclosed in single or triple double-quotes. Python can support Unicode right from the start, using the following syntax:

#**u”This is Unicode.”**

#To fill strings with values, you can use the modulo (%) operator and then a tuple. Each % gets replaced with a tuple item from left to right, and you can use dictionary substitutions as well.


print "Name: %s\
Number: %s\
String: %s" % (myclass.name, 3, 3 * "-")
Name: Poromenos
Number: 3
String: ---

strString = """This is a multiline string."""
>>> print "This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"}
#This is a test.

# Flow control statements
#Python’s flow control statements are ‘while’, ‘for’ and ‘if’. For a switch, you need to use ‘if’. For enumerating through list members, use ‘for’. For obtaining a number list, use range (number). Here is the statement syntax:

rangelist = range(10)
print rangelist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for number in rangelist:
if number in (3, 4, 7, 9):
break
else:
continue
else:
pass
if rangelist[1] == 2:
print "The second item (lists are 0-based) is 2"
elif rangelist[1] == 3:
print "The second item (lists are 0-based) is 3"
else:
print "Dunno"
while rangelist[1] == 1:
pass

### Functions
#The ‘def’ keyword is used to declare functions. Optional arguments can be set in the function declaration after mandatory arguments by assigning them default values. In the case of named arguments, the argument name is assigned a value. Functions can return a tuple, and you can effectively return several values using tuple unpacking. Parameters are passed through reference, but tuples, ints, strings, and other immutable types are unchangeable because only the item’s memory location is passed. Binding another object to the variable removed the older one and replaced immutable types. Here is an example:

funcvar = lambda x: x + 1
print funcvar(1)
2
def passing_example(a_list, an_int=2, a_string="A default string"):
a_list.append("A new item")
an_int = 4
return a_list, an_int, a_string

my_list = [1, 2, 3] my_int = 10
print passing_example(my_list, my_int)
([1, 2, 3, 'A new item'], 4, "A default string")
my_list
[1, 2, 3, 'A new item'] my_int
10

### Classes
#Python supports a very limited multiple class inheritance. Private methods and variables can be declared with the addition of two or more underscores and at most one trailing one. You can also bind names to class instances, like so.

class MyClass(object):
common = 10
def __init__(self):
self.myvariable = 3
def myfunction(self, arg1, arg2):
return self.myvariable
>>> classinstance = MyClass()
>>> classinstance.myfunction(1, 2)
3
>>> classinstance2 = MyClass()
>>> classinstance.common
10
>>> classinstance2.common
10
>>> MyClass.common = 30
>>> classinstance.common
30
>>> classinstance2.common
30
>>> classinstance.common = 10
>>> classinstance.common
10
>>> classinstance2.common
30
>>> MyClass.common = 50
>>> classinstance.common
10
>>> classinstance2.common
50
def __init__(self, arg1):
self.myvariable = 3
print arg1
>>> classinstance = OtherClass("hello")
hello
>>> classinstance.myfunction(1, 2)
3
>>> classinstance.test = 10
>>> classinstance.test
10

# Exceptions
#In Python, Exceptions are handled via try-except blocks [exceptionname]. Here is an example syntax:

def some_function():
try:
10 / 0
except ZeroDivisionError:
print "Oops, invalid."
else:
pass
finally:
print "We're done with that."
>>> some_function()
Oops, invalid.
#We're done with that.
### Importing

#In Python, external libraries can be used using the keyword import[library]. For individual functions, you can use from [funcname] or [libname] import. Take a look at the following sample syntax:

import random
from time import clock
randomint = random.randint(1, 100)
>>> print randomint
64

# File I/O
#The Python programing language comes with a lot of libraries, to begin with. For instance, here is a look at how we convert data structures to strings with the use of the pickle library using file I/O:

import pickle
mylist = ["This", "is", 4, 13327] # Open the file C: 
#binary.dat for writing. The letter r before the filename string is used to prevent backslash escaping.
myfile = open(r"C:\\binary.dat", "w")
pickle.dump(mylist, myfile)
myfile.close()
myfile = open(r"C:\\text.txt", "w")
myfile.write("This is a sample string")
myfile.close()
myfile = open(r"C:\\text.txt")
>>> print myfile.read()
#'This is a sample string'
myfile.close()
#Open the file for reading.
myfile = open(r"C:\\binary.dat")
loadedlist = pickle.load(myfile)
myfile.close()
>>> print loadedlist
['This', 'is', 4, 13327]

#Conditions and variables
#Conditions in Python can be changed. For instance, take a look at this condition:

1 < a < 3

#This condition checks that a is greater than one and also less than three. You can also use ‘del’ to delete items or variables in arrays. A great way to manipulate and create lists is through list comprehensions, which have an expression and then a ‘for’ clause, followed by a zero or more ‘for’ or ‘if’ clauses. Here is an example:

>>> lst1 = [1, 2, 3] >>> lst2 = [3, 4, 5] 
>>> print [x * y for x in lst1 for y in lst2] [3, 4, 5, 6, 8, 10, 9, 12, 15] 
>>> print [x for x in lst1 if 4 > x > 1] [2, 3]
#Check if a condition is true for any items.
#"any" returns true if any item in the list is true.
>>> any([i % 3 for i in [3, 3, 4, 4, 3]])
True
#This is because 4 % 3 = 1, and 1 is true, so any() returns True.
#Check for how many items a condition is true.
>>> sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
2
>>> del lst1[0] >>> print lst1
[2, 3] >>> del lst1

#Global variables are called so because they are declared outside functions and are readable without special declarations. However, if you want to write them, you need to declare them at the start of the function with the ‘global’ keyword. Otherwise, Python will bind the object to a new local variable. Take a look at the sample syntax below:

number = 5
def myfunc():
#This will print 5.
print number
def anotherfunc():
#This raises an exception because the variable has not been bound before printing. Python knows that it an object will be bound to it later and creates a new, local object instead of accessing the global one.
print number
number = 3
def yetanotherfunc():
global number
#This will correctly change the global.
number = 3
