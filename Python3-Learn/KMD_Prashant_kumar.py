'''AUTHOR: Prashant kumar
Python3 Concept: Knuth-Morris-Pratt (KMP) String Matching Algorithm
GITHUB: https://github.com/Prashant0kgp

Add your python3 concept below'''

# Python program for KMP Algorithm
def KMPSearch(word, txt):
	A = len(word)
	B = len(txt)

	# create lst[] that will hold the longest prefix suffix
	# values for pattern
	lst = [0]*A
	j = 0 # index for word[]

	# Preprocess the pattern (calculate lst[] array)
	computeLSTArray(word, A, lst)

	i = 0 # index for txt[]
	while i < B:
		if word[j] == txt[i]:
			i += 1
			j += 1

		if j == A:
			print ("STARTING INDEX " + str(i-j))
			j = lst[j-1]

		# mismatch after j matches
		elif i < B and word[j] != txt[i]:
			# Do not match lst[0..lst[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lst[j-1]
			else:
				i += 1

def computeLSTArray(word, M, lst):
	len = 0 # length of the previous longest prefix suffix

	lst[0] # lst[0] is always 0
	i = 1

	# the loop calculates lst[i] for i = 1 to M-1
	while i < M:
		if word[i]== word[len]:
			len += 1
			lst[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lst[len-1]

				# Also, note that we do not increment i here
			else:
				lst[i] = 0
				i += 1
# driver code
txt = "ABDABACDABABCABAB"
word = "ABABCABAB"
KMPSearch(word, txt)