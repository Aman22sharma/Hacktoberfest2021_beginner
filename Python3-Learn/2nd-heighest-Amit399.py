print("enter the number of elements to be entered in an array")
n=int(input())
B = []
for i in range(n):
    B.append(input())
print(B)
C=max(B)
for i in range(5):
    if C==max(B):
        B.remove(max(B))
print(max(B))
