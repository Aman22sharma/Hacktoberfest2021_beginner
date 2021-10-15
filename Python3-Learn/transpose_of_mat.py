import numpy

n , m = map(int,input().split())
a = []
for i in range(n):
    my_array = input().split()
    a.append(my_array)
lis1 = numpy.array(a,int)
print('input matrix:')
print(lis1)
if n==m:
    for i in range(n):
        for j in range(m):
            if i<j:
                lis1[i][j],lis1[j][i]=lis1[j][i],lis1[i][j]
    print("transposed matrix: ")
    print(lis1)
else:
    new=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            new[i][j]=lis1[j][i]
    print("transposed matrix: ")
    print(new)



