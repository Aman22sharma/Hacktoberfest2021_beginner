# AUTHOR: Akash Rajak
# Python3 Concept: Matrix Transpose
# GITHUB: https://github.com/akash435

# Add your python3 concept below

def matrix_transpose():
	for i in range(len(A)):
		for j in range(len(A[0])):
			res[i][j] = A[j][i]

A=[]

print("Enter N:")
n = int(input())

print("Enter Matrix A:")
for i in range(0, n):
	temp = []
	for j in range(0, n):
		x = int(input())
		temp.append(x)
	A.append(temp)

res = []
for i in range(0, n):
	temp = []
	for j in range(0, n):
		temp.append(0)
	res.append(temp)

matrix_transpose()

for r in res:
	print(r)
