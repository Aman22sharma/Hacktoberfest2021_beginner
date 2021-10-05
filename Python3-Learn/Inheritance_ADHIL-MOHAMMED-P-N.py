#// AUTHOR: Adhil Mohammed P N
#// Python3 Concept: Inheritance in python
#// GITHUB: https://github.com/ADHIL-MOHAMMED-P-N

#//Add your python3 concept below

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

emp = Person("Geek1") 
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())
