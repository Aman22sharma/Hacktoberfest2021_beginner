// AUTHOR: Bhairavi-shah
// Python3 Concept: Command Line Arguments
// GITHUB: github.com/Bhairavi-shah

# Add integers that have been passed as arguments in the command line
# For example, if you run: $python file-name.py 1 2 3
# The output must be 6

import sys
try:
    # We convert each argument passed to int and then add it to sum. 
    # sys.argv[0] is not taken because that returns the file name
    total = sum(int(arg) for arg in sys.argv[1:]) 
    print('Sum = ', total)

except ValueError: 
    # When no arguments are passed, ValueError occurs
    print('Please supply integer arguments')
