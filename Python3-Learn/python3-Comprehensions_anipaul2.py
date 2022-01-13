h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters) #This is list using for loop to append.

# #Now, we will use list comprehension which makes the above code easy to read and in single line.

h_letters = [letter for letter in 'human']
print(h_letters)

data = [1,2,3,4,5,6,7,8]
evens = []
for num in data:
     if not num % 2:
         evens.append(num)
print(evens)

evens = [num for num in data if not num % 2]
print(evens)

 
data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
print(words)
#Both up and below code resulting the same output but using for loop up ine and comprehensionsbelow one.
words = [num for num in data if isinstance(num, str)]
print(words)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())
print(title)

title = [word.title() for word in data]
print(title)