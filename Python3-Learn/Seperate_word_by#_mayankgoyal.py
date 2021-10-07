""" Aim: Read a text file line by line and display each word separated by a #
    Name: Mayank Goayl
    Github username: mayankgoyal-13
"""
#first creat a .txt file named list in the same directory.Then, add the content in it
file_text = open("list.txt", 'r')
for l in file_text:
    words = l.split()
    for i in words:
        print(i + '#', end='')
    print()
file_text.close()
