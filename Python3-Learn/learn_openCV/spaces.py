import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\park.jpg')
cv.imshow("img", img)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# plt.imshow(rgb)
# plt.show()

# # RBG to Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# We can not directly convert a gray to HSV. SO first gray has to be conveted to BGR and then BGR to HSV

# # BGR to HSV ( Hue saturation value)
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)


# # BGR to L*A*B
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("LAB", lab)

# # BGR is inverse of RBG anf python reads the image in BGR format

cv.waitKey(0)