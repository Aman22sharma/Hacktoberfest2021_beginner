import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\park.jpg')
cv.imshow("Img", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
b , g , r = cv.split(img)

# even after splitting how to get the actual color in place?
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("Blue", blue) # for blue, there is high concentration of blue in sky but very low of it in trees
cv.imshow("Green", green)
cv.imshow("Red", red)


# print(img.shape)# (427, 640, 3) The 3 is for 3 color channels
# print(b.shape)
# print(g.shape)
# print(r.shape)
# (427, 640)
# (427, 640)
# (427, 640)

merged = cv.merge([b,g,r])
cv.imshow("merged", merged)


cv.waitKey(0)