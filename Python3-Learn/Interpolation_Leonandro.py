// AUTHOR: Leonandro Gurgel
// Python3 Concept: (Numerical Analysis: interpolation)
// GITHUB: https://github.com/Leonandro


# In this code, we will make an a aproximation of the fuction x^3 - x^2 using an interpolation
# with trigonometic functions
# function used for generating the points = x^3 - x^2
# m = 8

import matplotlib.pyplot as plt
import numpy as np

M = 8
Xm = []
Ym = []

#Generating the points to be used on the interpolation
for j in range ( (2*M) ):
  Xm.append(-np.pi + (j*np.pi/M) )
  Ym.append(Xm[j]**3 - Xm[j]**2)

#Generating points to be used on the original function
Xinput = np.linspace(-np.pi, np.pi, 100)
Youtput = Xinput**3 - Xinput**2

#Ploting the original functions and the points that will be used on the interpolation
plt.plot(Xinput, Youtput, label='f(x) = x³ - x²')
plt.scatter(Xm, Ym, color='red')
plt.legend()
plt.show()

#Generating the a's coefficients
a_coeffs = []
coefficient = 0

for k in range (M + 1):
  coefficient = 0
  for j in range (2*M):
    coefficient += (Ym[j]*np.cos( k * Xm[j] ) ) 
  a_coeffs.append(coefficient/M)

#Generating the b's coefficients
b_coeffs = []

for k in range (1, M):
  coefficient = 0
  for j in range (2*M):
    coefficient += (Ym[j]*np.sin( k * Xm[j] ) ) 
  b_coeffs.append(coefficient/M)

#Interpolated function
def Sm (x):
  value = 0
  value = (a_coeffs[0] + a_coeffs[M]*np.cos(M*x))/2
  for k in range(1, M):
    value +=  a_coeffs[k]*np.cos(k*x) + b_coeffs[k-1]*np.sin(k*x)
  return value


plt.plot(Xinput, Sm(Xinput), label='Sm(x)')
plt.scatter(Xm, Ym, color='red')
plt.legend()
plt.show()