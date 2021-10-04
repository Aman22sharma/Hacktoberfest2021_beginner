# Histograms help us visualize the pixel dsitribution/intensity distribution
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\cats.jpg')
cv.imshow("img", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', circle)

masked = cv.bitwise_and(img,img, mask=mask)

# gray_hist = cv.calcHist([gray], [0],mask, [256], [0,256])
# This will show pixel intensity only for gray scale
# Description of arguments
#  1.) This takes a list of images
#  2.) No of channels. For gray scale this is zero
#  3.) Mask currently none
#  4.) No of bins==histSize, which will be used for creating histogram
#  5.) Range of all possible pixel values

# plt.figure()
# plt.title("Gray scale histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()



# Color histograms
plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b' , 'g', 'r') # colors tuple
for i, col in enumerate(colors):
    hist = cv.calcHist([img],   [i],    mask, [256], [0,256])
                              #channels
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()

# for i, col in enumerate(colors):
#     print("i = ", i, " & col = ", col)

cv.waitKey(0)