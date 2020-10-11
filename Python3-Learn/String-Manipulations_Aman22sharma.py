// AUTHOR: Syed Mohammad Muneer
// Python3 Concept: String Manipulations
// GITHUB: https://github.com/muneersyed156


#consider a string as follows
s = "Harry and Hermione along with Ron went to Hogwarts to learn magic and also win battle against Lord Voldemort"

#basic slicing format is s[startindex:stopindex:stepvalue(optional)] where stop index is not inclusive
# space is also considered as a charcater
print(s[0:7])       # prints from character at index 0 to charcater at index 6
print(s[0:10:2])    # prints from charcater at index 0 to charcater at index 9 with a step value of 2
print(s[-1])        # prints last charcater of the string s
print(s[::-1])      # prints the string in a reverse order
print(s[:])         # prints the whole string

k="Welcome"
print(k*3)          #prints a string 3 times continuously

#String methods and functions

a="Hope Andrea Mikaelson"
a=a.split(" ")       #The name is splitted a part based on the delimitor used i.e " "
print(a)             #prints list of words seperated by spaces

print(a[0].upper())          #converts each character in the string to uppercase 
print(a[0].lower())          #converts each character in the string to lowercase
print(a[0].capitalize())     #converts first character in the string to uppercase
print(a[0].startswith("an")) #if string starts with "an" substring then returns true else false
print(a[1].endswith("klaus")) #if string ends with "klaus" substring then returns true else false

a=' '.join(a)                #Join function combines the words into a sentence with mentioned delimiter between the words
print(a)

print(a.find('a'))            #returns the position of mentioned charcater from left if existed else -1 will be returned

try:
    print(a.index('e'))      #if character is found then it's position is retunred
    print(a.index('c'))      #if charcater is not found then index function raises an exception
except Exception as e:
    print("Element is not found")  


m='Dark,Matter,is,found,everywhere'

m=m.replace(","," ")         #replace funtion is used to replace a charcater with other character in whole string
print(m)

k='hello1'

print(k.isalpha())          #returns true if string has only alphabets else false
print(k.isalnum())          #returns true if string has either alphabets,numbers or both else false
print(k.isdigit())          #returns true if all charcaters in string are digits

#string library

import string

print(string.ascii_letters)   #prints alphabets both lower,uppercase
print(string.ascii_lowercase) #prints lowercase alphabets
print(string.ascii_uppercase) #prints uppercase alphabets
print(string.digits)          #prints digits from [0-9]

print("\n")
#Custom printing using format method 

s=str(input("Please Enter your name: "))
print("Dear {}, \nWelcome to Hacktober fest".format(s))