rowNum = 5
space = rowNum-1
for i in range(1, rowNum+1):
  for j in range(1, space+1):
    print(end=" ")
  space = space-1
  for j in range(2*i-1):
    print(end="*")
  print()
space = 1
for i in range(1, rowNum):
  for j in range(1, space+1):
    print(end=" ")
  space = space+1
  for j in range(1, 2*(rowNum-i)):
    print(end="*")
  print()