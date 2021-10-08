"""
AUTHOR: Fatema Vajihee
Python3 Concept: 4 Sum in Python
GITHUB: https://github.com/Fatema110

 A hashing based Python program to find if there are four elements with given summ.

 The function finds four elements with given summ X

 """

def findFourElements(arr, n, X):

	# Store summs of all pairs in a hash table
	mp = {}
	op = []
	for i in range(n - 1):
		for j in range(i + 1, n):
			mp[arr[i] + arr[j]] = [i, j]

	# Traverse through all pairs and search
	# for X - (current pair summ).
	for i in range(n - 1):
		for j in range(i + 1, n):
			summ = arr[i] + arr[j]

			# If X - summ is present in hash table,
			if (X - summ) in mp:

				# Making sure that all elements are
				# distinct array elements and an element
				# is not considered more than once.
				p = mp[X - summ]
				if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
					op = [arr[p[0]] , arr[p[1]] , arr[i] , arr[j]]
	print(op)


# Driver code
arr = [0,0,2,1,1]
n = len(arr)
X = 3

# Function call
findFourElements(arr, n, X)