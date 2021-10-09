"""
AUTHOR: Fatema Vajihee
Python3 Concept: Majority Element in Python
GITHUB: https://github.com/Fatema110

A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

Examples : 

Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 

"""

def majorityElement(self, arr, n):
        arr.sort()
        count = 1
        max_ele = -1
        temp = arr[0]
        flag = 0
        
        for i in range(1,n):
            
            if(temp == arr[i]):
                count += 1
            else:
                count = 1
                temp = arr[i]
            
            if(max_ele < count):
                
                max_ele = count
                ele = arr[i]
                
                if(max_ele > (n//2)):
                    flag = 1
                    break 
                
        if(flag == 1):
            return ele
        elif(len(arr) == 1):
            return arr[0]
        else:
            return -1


import math

from sys import stdin


def main():
    
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
