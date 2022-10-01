import matplotlib.pyplot as plt

print("Enter the x1: ")
x1 = int(input())
print("Enter the x2: ")
x2 = int(input())
print("Enter the y1: ")
y1 = int(input())
print("Enter the y2: ")
y2 = int(input())

dx = x2-x1
dy = y2-y1

if(abs(dx) > abs(dy)):
  steps = abs(dx)
else:
  steps = abs(dy)

xincrement = dx/steps
yincrement = dy/steps

i = 0

xcordinates = []
ycordinates = []

while i < steps:
  i+=1
  x1 += xincrement
  y1 += yincrement
  print("x1 : ",x1," y1 : ",y1)
  xcordinates.append(x1)
  ycordinates.append(y1)

plt.plot(xcordinates,ycordinates)

plt.xlabel("X - axis")
plt.ylabel("Y - axis")

plt.title("DDA LINE ALGORITHM")

plt.show()
