// AUTHOR: priyajames
// Python3 Concept: oops in python
// GITHUB: https://github.com/priyajames29

//Add your python3 concept below





class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


cat1 = Cat("tutu" , 13)
cat2 = Cat("aaa" , 5)
cat3 = Cat("meow", 4)

def oldest(*args):
        return max(args)

print(f"The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old. ")

