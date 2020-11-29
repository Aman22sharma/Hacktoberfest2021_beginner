# AUTHOR: Sushmita
# Python3 Concept: function in RegEx
# GITHUB: https://github.com/Sushmita10062002

import re        # re is built in package in python for RegEx
text = "Your only limit is your mind"

x = re.findall("our",text)   #return a list containing "our" in text
print(x)

y = re.search("li",text)   #return a Match object if there is a match anywhere in text
print(y)

z = re.split("\s",text)    #return a list where the text has been split at whitespace
print(z)

p = re.sub("o" , "2" , text)   #replace "o" with "2" in text
print(p)

