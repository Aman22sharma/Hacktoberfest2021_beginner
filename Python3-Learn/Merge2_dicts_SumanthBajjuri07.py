
#AUTHOR:  SumanthBajjuri07
#Python3 Concept: Merging 2 dictionaries
#GITHUB: https://github.com/SumanthBajjuri07












dict1 = { 'Alexandra' : 27,      # given the first dictionary in key-value pairs  
            'Shelina Gomez' : 22,  
            'James' : 29,  
            'Peterson' : 30  
                        }   
dict2 = {  
            'Jasmine' : 19,      # given the second dictionary in key-value pairs  
            'Maria' : 26,  
            'Helena' : 30  
}                          
print("Before merging the two dictionary ")  
print("Dictionary No. 1 is : ", dict1) # print the dict1  
print("Dictionary No. 1 is : ", dict2)  # print the dict2  
  
dict3 = dict1.copy()  # Copy the dict1 into the dict3 using copy() method  
  
for key, value in dict2.items():  # use for loop to iterate dict2 into the dict3 dictionary  
    dict3[key] = value  
  
print("After merging of the two Dictionary ")  
print(dict3)    # print the merge dictionary  
