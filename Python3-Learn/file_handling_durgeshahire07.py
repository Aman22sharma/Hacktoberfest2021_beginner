"""""
// AUTHOR: Durgesh Ahire
// Python3 Concept: File handling in Python3
// GITHUB: https://github.com/durgeshahire07

//Add your python3 concept below
"""""

# Python program to demonstrate
# file handling


# importing module
import sys, os

# path of the current script
pathname = os.path.dirname(sys.argv[0])
print()

# Before creating
dir_list = os.listdir(pathname)
print("List of directories and files before creation:")
print(dir_list)
print()

# Creates a new file
with open('myfile.txt', 'w+') as fp:
	pass
	# To write data to new file uncomment
	# this fp.write("New file created")

# After creating
dir_list = os.listdir(pathname)
print("List of directories and files after creation:")
print(dir_list)

# Write on a file
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close() #to change file access modes

# Display the content in the file
file1 = open("myfile.txt","r+")
print("Output of Read function is ")
print(file1.read())
print()
