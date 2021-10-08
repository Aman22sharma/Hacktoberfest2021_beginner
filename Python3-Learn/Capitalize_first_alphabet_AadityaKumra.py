# AUTHOR: Aaditya Kumra
# Python3 Concept:String traversing
# GITHUB: https://github.com/AadityaKumra

#capitalize first letter of each word.
#input-elon musk
#output-Elon Musk
def solve(a):
    a = s.split(' ')
    n=(' '.join((word.capitalize() for word in a)))
    return n

s = input() 
result = solve(s)
print(result)
