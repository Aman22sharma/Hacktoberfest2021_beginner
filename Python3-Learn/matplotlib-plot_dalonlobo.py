# AUTHOR: Dalon Lobo
# Python3 Concept: Plotting line plot using matplotlib
# GITHUB: https://github.com/dalonlobo

import numpy as np
import matplotlib.pyplot as plt

# Create dummy x and y values. In this case I create values using numpy.
# This graph will show sine wave
x = np.arange(0, 10, 0.1)  # Values for x coordinate
y = np.sin(x)  # Values for y coordinate using numpy sin function
plt.plot(x, y)  # Plots the x and y coordinates
plt.xlabel("x - values")  # show x label
plt.ylabel("y = sin(x)")  # show y label
plt.show()  # Displays the plot
