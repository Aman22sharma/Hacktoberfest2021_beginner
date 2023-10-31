import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\cats.jpg')
cv.imshow("Cats", img)

# Gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", gray)

# # Blur
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# # edge detection/canny
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)

# Alternative for blur + canny below
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# If intensity is below 125 then set to 0/black and above 255 will be 1/white
cv.imshow("Thresh", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours), " contours found!")


# Visualizing the contours by drawing on the blank image
blank = np.zeros(img.shape, dtype="uint8")

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours on blank", blank)


# cv.imshow("Blank", blank)

cv.waitKey(0)
