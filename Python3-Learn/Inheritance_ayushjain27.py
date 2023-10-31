AUTHOR: Ayush Jain
Python3 Concept: Inheritance
GITHUB: https://github.com/ayushjain27

# Inheritance

# Single level inheritance

class Person(object):
    def __init__(self, name):
        self.name = name
   
    def getName(self):
        return self.name

    def isEmployee(self):
        return False
      
class Employee(Person):
    def isEmployee(self):
        return True
   
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
   
emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())


Output: 

Geek1 False
Geek2 True

# Multiple inheritance

class Employee:
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

class player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f" The name is {self.name}, Game is {self.game} "

class CoolProgrammer(Employee,player):
    language = "C++"
    def printlanguage(self):
        print(self.language)

Harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",4554,"Student")
shubham = player("Shubham",["Cricket"])
karan = CoolProgrammer("Karan",8999,"CoolProgrammer")
karan.printdetails()
print(karan.printdetails())
karan.printlanguage()

Output:

Name is Karan, Salary is 8999 and role is CoolProgrammer
C++

# Multilevel inheritance
class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 6

    def isdance(self):
        return f"Jackson yeah! " \
               f"Yes I dance very aewesomely {self.dance} no of times"
darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)

Output:

Jackson yeah! Yes I dance very aewesomely 6 no of times
1