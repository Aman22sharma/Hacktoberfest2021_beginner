#!/usr/bin/env python
# coding: utf-8

# In[1]:


def split_and_join(line):                    #Creating a function named split and join
    a=line.split(" ")                        #Splitting the string and making a list and storing the refference in variable a
    a='-'.join(a)                            #Joining the element of list by ""-"" you can join it with anything
    return a                                 #Returning a

if __name__ == '__main__':
    line = input()                           #Taking input
    result = split_and_join(line)            #Calling the function we created and putting the argument i.e string
    print(result)                            #Printing Result

