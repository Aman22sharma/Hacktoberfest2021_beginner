import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\park.jpg')
cv.imshow("img", img)

# What are gradients? 
# They are edge like regions butt mathematically they are different. However for programmatic thinking they are same
# Two methods ...
# 1) Laplacian
# 2) Sobel

# Laplacian method
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

lap = cv.Laplacian(gray, cv.CV_64F)
# cv.CV_64F is the data depth
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel method
# It computes gradients in two directions, X and Y directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
# 1  is x direction and 0 in y direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# 0  is x direction and 1 in y direction
# cv.imshow("Sobel_X", sobelx)
# cv.imshow("Sobel_Y", sobely)
combined_sobel = cv.bitwise_and(sobelx, sobely)
cv.imshow("Combined sobel", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)