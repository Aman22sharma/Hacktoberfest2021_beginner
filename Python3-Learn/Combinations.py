from itertools import combinations
S,n=input().split()
print(sorted(S))
for i in range(1,int(n)+1,1):
    for j in combinations(sorted(S),i):
        print("".join(j))