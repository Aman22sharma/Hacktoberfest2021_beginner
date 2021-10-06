# say n is 5 you must get a pattern like this
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5

n=int(input())
size=2*n-1
pattern=[]
for i in range(n):
    row=[0]*size
    for x in range(i+1):
        num=n-x
        row[x:size-x]=[num for i in range(size-2*x)]
    pattern.append(row)
pattern=pattern+pattern[:-1][::-1]
for row in pattern: print(*row)
