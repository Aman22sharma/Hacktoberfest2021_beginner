# AUTHOR: Aaditya Kumra
# Python3 Concept:String traversing
# GITHUB: https://github.com/AadityaKumra

#print the number of times that the substring occurs in the given input string

def count_substring(string, sub_string):
    counter,sum = 0,0
    for _ in range(0, len(string)):
        if string[counter:(len(sub_string)+counter)]==sub_string:
            sum = sum + 1
        counter=counter + 1
    return sum

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)