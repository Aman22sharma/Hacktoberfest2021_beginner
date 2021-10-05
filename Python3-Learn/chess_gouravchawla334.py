#AUTHOR:  Gourav chawla
#Python3 Concept: Simple Chess using python
#GITHUB: https://github.com/gouravchawla334

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0,dx)
y = np.arange(-4.0, 4.0,dx)
X, Y = np.meshgrid(x,y)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8))%2
plt.imshow(Z1,cmap="binary_r",
           interpolation='nearest',
           extent=extent,alpha=1)

def copyassignment(x,y):
    return(1- x/ 2 + x**5 + y**6)*np.exp(-(x**2+y**2))
Z2 = copyassignment(X,Y)
plt.imshow(Z2, alpha=0.7, interpolation='bilinear',extent=extent)
plt.cool()
plt.title('matplotlib.pyplot.cool() function Example', fontweight='bold')
plt.show()