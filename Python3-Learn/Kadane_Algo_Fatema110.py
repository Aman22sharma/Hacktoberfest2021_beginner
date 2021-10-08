"""
AUTHOR: Fatema Vajihee
Python3 Concept: Kadane's  Algorithm in Python
GITHUB: https://github.com/Fatema110


Kadane’s algorithm is able to find the maximum sum of a contiguous subarray in an array with a runtime of O(n).

"""

def largestSum(array):
    max_ending_here = 0
    max_so_far =0
    for x in array:
        max_ending_here = max_ending_here + x
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far
print(largestSum([1,2,4,-2]))