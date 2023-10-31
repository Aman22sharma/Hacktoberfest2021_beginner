# AUTHOR: Aaditya Kumra
# Python3 Concept:String traversing
# GITHUB: https://github.com/AadityaKumra

#capitalize first letter of each word.
#input-nikhil jain
#output-Nikhil Jain


def Capatalize_string(a):
    a = s.split(' ')
    n = (' '.join(word.capitalize() for word in a))
    return n

s = input() 
final_string = Capatalize_string(s)
print(final_string)
