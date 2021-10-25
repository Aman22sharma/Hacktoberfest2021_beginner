''' AUTHOR: João Matheus Villarim
// Python3 Concept: given a number X, print all the numbers less than X whose adjascent digits have a difference less than or equal to 1
// GITHUB: https://github.com/joaomatheusvillarim'''

number, lista = int(input()), []
for k in range(1, number+1):
    digits, willprint = [], True
    for chr in str(k):
        digits.append(int(chr))
    for y in range(len(digits)-1):
        dif = abs(digits[y+1] - digits[y])
        if dif!=0 and dif!=1:
            willprint = False
    if willprint == True:
        string = "".join(map(str, digits))
        lista.append(int(string))
print(lista)
