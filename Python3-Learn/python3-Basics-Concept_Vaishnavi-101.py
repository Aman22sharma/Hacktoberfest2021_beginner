#Author:Vaishnavi Sharma
#python3 concepts - firstprogram,escape sequences,variable,data type,casting
#list,set,tuple,dictionary,conditional statement,Loop,Function,lambda Function,
#classes and object.
#Github Profile Link : https://github.com/Vaishnavi-101

#python Begginers Guide:
#first python Program
# print("Hello")
# print('Hello World!')

# facts about " " and ''

 #print("Hi i am 'Vaishnavi' ")
# print('Hi i am "Devil" ')

# Esape Sequences \ , \\ , \n , \t , \r

# print("\'Python\' Begginer Course")
# print("I\'m learning it from youtube\nand it is going cool!")
# print("Enjoying\tlearning")

#importance of indentation in python , python use it to refer a block of code
#same whitespaces should be given for same block otherwise syntax error occoured
if(6 > 3):
     print("Yes")
     print("yes 6 is greater") 

#MultiLine Comment - python ignore string literals if it is not assign to string
"""
this is multiLine 
Comment

"""
#Variable - Python has no Command for declariang a variable
# x =5
# y = "DEVIL"
# print(x)
# print(y)

# x=6
# x="Mannu"
# print(x)

#Casting - if you want to specify a data type
# a = str(7)
# b = float(5)
# print(a)
# print(b)

#type() - get the data type
# a = 7
# print(type(a))

#variable Functionality - Many to one or One to many
# x,y,z = 5,"hi",10.0
# print(x)
# print(y)
# print(z)

# x= y =0
# print(x)
# print(y)

# + combine both text and variable
# a = "Python"
# print(a +" is cool")

# b="Hello"
# c ="Everyone"
# print(b + c)

#Data Types - Built in Data Types
#Numeric Type also called Numbers
# x = 10 #int
# print(x)
# y = 20.5 #float
# print(y)
# z = 5j  #complex
# print(z)

#Text Type
# x ="Hello"  #str
# print(x)

#sequence Type - list,Tuple,Range
# z = ["Apple","Banana"]
# print(z)
# b = ("mango","orange")
# print(b)
# v = range(5)
# print(v)

#strings and string Methods
#a ="Hello"
# print(a)
# print(a[2])
# print(a[2:]) #slicing it gives index 2 to end
# print(a[:2]) #slicing it give index 0 to 2
# print(a[1:4]) #including start but excluding end
# print(a[::2]) #jump at one position

# print(len(a)) len -for length
# txt = "Hi i am learning Python"
# if "am" in txt:   Find word present in given string or not
#     print("Yes")

#UpperCase And LowerCase
# a="WORLD"
# print(a.lower())
# b="hello"
# print(b.upper())

#strip - remove whiteSpaces
# a ="  Hello  World  "
# print(a.strip())

#replace() - string with another string
# a="Devil"
# print(a.replace("D","E"))

#split - split string in to two substring
# a ="Hello,World"
# print(a.split(","))

#format - combine number with string
# a=22
# b="Devil age is {}"
# print(b.format(a))

#List - is simiilar to string (functionality)
#  it is one of built in data type in Python
# MyList =[1,7,5,3] #list also allow duplicates
# MyList1=["Devil","Evil","angstrom"]
# MyList2=["shinchan",5]
#print(MyList)
# print(MyList1)
# print(MyList2)
#List are Mutable means change the value
# MyList[1] =5
# print(MyList)

# print(MyList)
#Insert - used to insert at specified Position
# MyList.insert(3,4)
# print(MyList)

#append - add item in list to last
# MyList.append(5)
# print(MyList)

#extend - add list to another list
# MyList.extend(MyList1)
# print(MyList)

#remove or pop- it remove given item and also specified
# MyList1.remove("Devil")
# print(MyList1)
# MyList1.pop() #remove last item
# print(MyList1)
# MyList1.pop(1)
# print(MyList1)

#sort - sort in ascending order
# MyList.sort()
# print(MyList)

#sort(reverse=True) - sort in descending order
# MyList.sort(reverse=True)
# print(MyList)

#copy - listname.copy() cant copied by l1=l2
# hi=MyList.copy()
# print(hi)

#join - list can be join in many method like append,extend,+
# NewList=MyList+MyList1
# print(NewList)
"""
There are four collection built in data types in the Python programming language:
List ,Tuple , Set , dictionary
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

"""
#Tuple - very simillar to list but it is immutable but ordered
# MyTuple =("Hello","WOrld")
# print(MyTuple)
# MyTuple[1]="Name" // Tuple not support item assignment
# print(MyTuple)

#sets - unordered and unindexed , dont allow duplicates values
# MySets ={1,2,"banana",2}
# print(MySets)
# MySets.add(5) #to add an item 
# print(MySets)

#update() - add one set item to another set
# MySets1={5,7}
# MySets.update(MySets1)
# print(MySets) 

#remove() or discard() - both use to remove element from sets
#with one difference is that if element not present then remove show error 
#and discard() not shown any error 
#pop(),clear(),del

# MySets.remove(2)
# print(MySets)

#join() - union() or update() both of them exclude duplicates
#MySets2={4,6}
# MySets3=MySets1.union(MySets2)
# print(MySets3)

#duplicates - intersection_update
# set={5,3}
# set.intersection_update(MySets1)
# print(set)

#intersection() - return which present in both
#symmetric_difference - it conatins which is not present in both sets

# Dictionary - is a collection which is ordered and changeable. No duplicate members.
#dictionaries are python version of hash table based on mapping of key value pair.
#thisdic={"vaishu":1,"payal":420}
# print(thisdic)
# x=thisdic["payal"] // accessing value by its key
# print(x)
#get() - accessing
# x=thisdic.get("payal")
# print(x)

#keys() - return all keys of dictionaries
# x=thisdic.keys()
# print(x)

#values() - return all values of dictionaries
#update() - updates a key value pair
# thisdic.update({"vaishu":420})
# print(thisdic)

#delte a value - pop(key),popitem(),del,clear()
#copy() - one dictionary to another

#conditional statement
#if
# a=5
# b=4
# if a>b :
#      print("a is graeter than b")

#elif-
# a =41
# b=22
# if a<b:
#      print("a is lesser than b")
# elif a>b :
#      print("a is greater than b")

#else - keyword caught anything which is not done by previous conditions
# a=12
# b=25
# if a==b:
#      print("a is equal to b")
# elif a>b:
#      print("a is greater")
# else :
#      print("a is smaller than b")     

#And , or - logical operator 
# a = 5
# b = 7
# c = 10
# if a<b and a<c:
#      print("a is smaller")

#pass - if you dont put any content in if block then written it.

#loop - in Python two primitive loop commands.
#while and for
# i = 1
# while i<7:
#      print(i)
#      i+=1;

#break - used to terminate the loop.
#continue - used to terminate the current iteration.

#for - A for loop is used for iterating over a sequence
#  (that is either a list, a tuple, a dictionary, a set, or a string).
#iterate over list
# students =["vaishu","payal","Radhika","Harshita"]
# for i in students:
#      print(i)

#iterate over string
# a="Devil"
# for i in a:
#      print(i)

#break - stop the loop iteration
# list =[1,2,3,4,5]
# for i in list:
#      print(i)
#      if i==3:
#       break

#range -
# for x in range(4):
#      print(x)

#functions - use def keyword to make function.
# def fun():
#      print("Trying to Learn Python")
# fun()

#with arguments
# def add(a,b):
#      print(a+b)
# add(5,6)
# add(100,200)     

#arbitary arguement * - if you dont know how many arguments can passed use *

# def naughty(*stud):
#      print("the naughty one is " + stud[1])
# naughty("Evil","Devil")     

#Default parameter value - if no argument passed then it return default value.
# def city(town="Kanpur"):
#      print("the town is " + town)
# city("gwalior")  
# city()   

#lambda function or anonymous function or a function with no name -  can take any number
#  of arguments, but can only have one expression 
"""
if you have a single line of expression 
in function you can convert it in to lambda function

"""
# even1 = lambda a:a%2==0
# print(even1(4))

# addi = lambda a,b:a+b
# print(addi(5,4))

#OOP CONCEPT -

# class Sample():
#      pass
# x = Sample()
# print(type(x))

#__init__ = initialiization
# class Dog():
#      #class object attribute
#      species="Mammals"
#      def __init__(self,breed,name):
#          self.breed = breed
#          self.name = name
# Mydog = Dog(breed="Libra",name="Xena")
# print(Mydog.breed)
# print(Mydog.name)
# print(Mydog.species)         

