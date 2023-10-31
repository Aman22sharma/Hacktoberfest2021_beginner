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
