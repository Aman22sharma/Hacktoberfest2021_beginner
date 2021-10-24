// AUTHOR: Ashutosh kumar choudhary
// Python3 Concept: TOWER OF HANAOI PUZZLE
// GITHUB: https://github.com/Ash-KODES
    
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

--Only one disk can be moved at a time.
--Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
--No disk may be placed on top of a smaller disk.

PYTHON CODE
# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
	if n == 1:
		print("Move disk 1 from rod",from_rod,"to rod",to_rod)
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
		
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods

