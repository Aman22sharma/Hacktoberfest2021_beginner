# AUTHOR: Bhoomika Gothwal
# Python3 Concept: Bit Manipulation
# GITHUB: https://github.com/OREO1210



# Function to get the bit at the ith position
def getBit( num,  i):
 
    # Return true if the ith bit is set. Otherwise return false
    return ((num & (1 << i)) != 0)
 

# Function to set the ith bit of the given number num
def setBit( num,  i):
 
    # Sets the ith bit and return the updated value.
    return num | (1 << i)
 

# Function to clear the ith bit of the given number N.
def clearBit( num,  i):
     
    # Create the mask for the ith bit unset.
    mask = ~(1 << i)
     
    # Return the update value
    return num & mask
 


# Driver Code for Given number N
n = 90
print("The bit at the 4rd position is: " , 1 if (getBit(n, 4)) else '0')
 
print("The value of the given number" , "after setting the bit at ","MSB is: " , setBit(n, 0))
 
print("The value of the given number" , "after clearing the bit at ","MSB is: " , clearBit(n, 0))
 