import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\cats 2.jpg')
cv.imshow("img", img)

######   the dimesnion of this blank must be same as the read image
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank, (30,30), (370,370), 255, -1)
# cv.imshow("mask", circle)

weird_shape = cv.bitwise_and(circle, rectangle)

masked_img = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("masked_image", masked_img)

cv.waitKey(0)