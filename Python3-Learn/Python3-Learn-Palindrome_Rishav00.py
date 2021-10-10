// AUTHOR: Rishav Dutta
// Python3 Concept: Checking a string Palindrome or not
// GITHUB: https://github.com/Rishav-00

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
