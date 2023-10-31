import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\cats.jpg')
cv.imshow("img", img)

# Averaging method to blur. We define a kernel window. It computes the intensity of the middle pixel intensity by avergaing out the intensity of surrounding pizels
# This window will slide to the entire screen
average = cv.blur(img, (3,3)) # if the kernel size (3,3) is higher, there will be more blur
cv.imshow("Average", average)


# Gaussian Blur, no average, each surrounding pixel get a weight and then averaged to compute the wight of center pixel
# Gaussian blur will have a lesser effect than average
gaussian = cv.GaussianBlur(img, (3,3), 0) # 0 is for standard deviation
cv.imshow("Gaussian", gaussian)

# Median blur. Instead avarage just median. This is more accurate when there is lot of noice
# This method has lesser blur than gaussian
median = cv.medianBlur(img, 3) # 3 is the kernel size, openCV will treat it as 3X3 automatically
cv.imshow('Median', median)

# Bilateral blurring. Most effective. Why? It takes care of the edges
bilateral = cv.bilateralFilter(img, 5, 35, 25) # 5 is diameter of pizel neighborhood and not kernel size
# 35 is for sigma color, no of color which will be considered.
# 25 is for sigma space, which denotes the intensity with which distant pixels will afect the center pixel
cv.imshow(("Bilateral"), bilateral)
# It did not cause much change
cv.waitKey(0)