// AUTHOR: Syed Mohammad Muneer
// Python3 Concept: Set-Operations
// GITHUB: https://github.com/muneersyed156

a=set()             #a will be assigned to Object set()
print(a)            #prints empty set i.e Φ
print(type(a))      #returns the datatype as set

b={}                #Don't get confused here ,it is a dict
print(type(b))      #returns the datatype as dict
print(b)            #prints an empty dict 

m={1,(2,3,5),"Happy Hacking.... :D"}
print(m)            #set can have heterogeneous data that are immutable 

try:
    m={1,[2,3,5],"Happy Hacking.... :D"} #Exception will be raised as it has mutable datatype i.e [2,3,5]
    print(m)
except Exception as e:
    print("There could be some mutable data in m")


#Convertion of a datatype to Set
z=["Hai","Welcome to",2020,"Hacktober-fest"]
k=("Dark-Matter",1,4.0,45,3,3)
print(set(z))                   #Converting a list to set
print(set(k))                   #Converting a tuple to set

#adding elements in to a set 

m={1,2,3,4}
m.add(7)     #adding an element into a set
m.update([12, 3, 14])  #adding multiple elements to a set using update method

#deleting an element from a set

m.discard(7)     #discard method is used to delete an element from a set
print(m)         
m.remove(12)     #remove method is also used to delete an element from a set 
print(m)
m.discard(17)    #If the element to be deleted is not present in the set then discard method will return None
try:
    m.remove(17) #If the element to be deleted is not present in the set then remove methods raises an Exception
except Exception as e:
    print("Deleting an element which is not present in set using remove method")

m.pop()          #Randomly delets an element from the set
m.clear()        #Deletes every element from the set and finally makes the set empty


#Set Operations
a={13,12,3,2,5,7,19,10}
b={17,13,2,4,8,9,11,23}

print(a-b)          #prints all the elements that are present only in a
print(b.difference(a))  #Instead of using - we can use difference operator

print(a|b)          #prints union of both a,b
print(b.union(a))   #union method can be used instead of using | operator

print(a&b)          #prints common elements in both set a,b
print(a.intersection(b)) #Instead of using & operation we can use intersection method

print(a^b)          #prints elements of a,b which are not in both sets called as Symmetric difference
print(a.symmetric_difference(b))  #Instead of using ^ operator for we can use symmetric difference method here

#frozen sets

a=frozenset(a)
print(a)
try:
    a.add(800)
except Exception as e:
    print("Frozen set means ...... Manipulations on set cannot be done!")


