'''
AUTHOR: Jishnu S G
Python3 Concept: Sum of n numbers
GITHUB: https://github.com/jishnukoliyadan

Using recursion to find the sum of n natural numbers
'''

def sum_n_numbers(n):

    if n == 0 :
        return 0
    
    recursive_out = sum_n_numbers(n - 1)
    final_output = recursive_out + n
    
    return final_output

print(sum_n_numbers(6))