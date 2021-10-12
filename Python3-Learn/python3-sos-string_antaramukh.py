#!/usr/bin/env python
# coding: utf-8

# In[1]:


# AUTHOR: Antara Mukherjee
# Python3 Concept: SOS String Problem
# GITHUB: https://github.com/antaramukh

# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.

# Example: s="SOSTOT"

# The original message was SOSSOS. Two of the message's characters were changed in transit.


# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.


def marsExploration(s):
    count=0
    for i in range(0,len(s),3):
        if(s[i]=="S"):
            count+=0
        else:
            count+=1
        if(s[i+1]=="O"):
            count+=0
        else:
            count+=1
        if(s[i+2]=="S"):
            count+=0
        else:
            count+=1   
    return count

input_string="SOSSTO"
print(marsExploration(input_string))


# In[ ]:




