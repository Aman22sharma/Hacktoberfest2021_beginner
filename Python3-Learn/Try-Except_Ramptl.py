// AUTHOR: Ram Patel
// Python3 Concept: Try-Except in Python
// GITHUB: https://github.com/Ramptl

//# working of try() 

def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
  
# Look at parameters and note the working of Program 
divide(3, 2) 
