"""
Name : Quadratic equation solver
Author : [Mayank Goyal) [https://github.com/mayankgoyal-13]
"""

from math import sqrt

print("Quadratic function : (a * x\u00b2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

disc = b ** 2 - 4 * a * c

if disc > 0:
    x1 = ((-b) + sqrt(r)) // (2 * a)
    x2 = ((-b) - sqrt(r)) / (2 * a)
    print("There are 2 roots:", x1, x2)

elif disc == 0:
    x = (-b) / 2 * a
    print("There is one root: ", x)

else:
    print("No roots, discriminant < 0.")
