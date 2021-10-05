// AUTHOR: Devendra Patel
//Python3 Concept: Palindrome
// GITHUB: https://github.com/github-dev21

print("Enter the Number ")
num = int(input())
temp = num
reverse = 0

while(num>0):
    dig = num%10
    reverse = reverse*10+dig
    num = num//10

print(reverse)
if temp==reverse:
    print("Number is in Palindrome")
else:
    print("Number is not in Palindrome")