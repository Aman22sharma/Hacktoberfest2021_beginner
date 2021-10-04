import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\cats.jpg')
cv.imshow("img", img)

# Thresholding is the binarization of an image
# i.e. Either white or black
# We do this by assuming a threshold. Any pixel greater than thresh is set to 0 and lower than thresh is set to 1

# There are 2 types of thresholding: Simple and adaptive

# BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# Simple threshold: Here we have to mention the threshold value ourselves
threshold, thresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
# We have to pass the gray scale image for this threshold function
# 150 is the threshold value
# Threshold is the threshold value, ie 150
# and thresh is the binarized image
# cv.imshow("Thresh_Simple", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255,cv.THRESH_BINARY_INV)
# This just does the opposite wuth the thrshold value, that is 150
# cv.imshow("Inverse_threshold_simple", thresh_inv)


# Adaptive threshold
# This method does optimal thresholding on the basis of mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 13, 9)
# 11 is the kernel size or the block size
# Last value is the c value which we subtract from the mean for fine tuning. For greater c value we will get sharper edges
# With this also we can do inverse thing
cv.imshow("Adaptive_thresh", adaptive_thresh)


cv.waitKey(0)