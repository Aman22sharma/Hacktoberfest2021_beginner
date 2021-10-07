// AUTHOR: Avyay Jain
// Python3 Concept: (calculator)
// GITHUB: https://github.com/avyayjain

import wikipedia as wiki

n = input('Enter What You want to search : ')
wresult = wiki.search(n)
j=0

for i in wresult:
        print('Enter ',j,' for search about ',i)
        j += 1

ent = int(input('Enter Your Option : '))
print('you choose ',wresult[ent])
result = wiki.summary(wresult[ent],sentences=2)
print(result)
