//  AUTHOR: RUDRANSH SRIVASTAVA
//  Python3 Concept: PALINDROME STRING OR NOT
//  GITHUB: https://github.com/RUDRANSH-hub

'''TO FIND OUT WEATHER STRING IS PALINDROME OR NOT'''

str=input("enter testing string:")
reverse_str=str[::-1]  #reverse slicing the original string
if reverse_str==str:
    print("{} is palindrome".format(str))
else:
    print("{} is not palindrome".format(str))

