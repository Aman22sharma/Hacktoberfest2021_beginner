import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\park.jpg')
cv.imshow("img", img)
# def translate(img, x, y):
#     # Translation matrix
#     transMat = np.float32([[1,0,x], [0,1,y]]) # this 2X3 matrix is necessary
#     dimension = (img.shape[1], img.shape[0])

# # -x --> left
# # -y --> up

#     return cv.warpAffine(img, transMat, dimension)

# translated = translate(img, 100, 100)
# cv.imshow("Translated", translated)

# Rotation
# def rotate(img, angle, rotPoint=None):
#     (height,width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
#     dimesnions = (width,height)
#     return cv.warpAffine(img, rotMat, dimesnions)

# rotated = rotate(img, -90, None)
# cv.imshow("Rotated",rotated)

# Flipping
flip = cv.flip(img, 1)
# 0 flips it horizontally
# 1 flips it vertically
cv.imshow("Flipped", flip)


cv.waitKey(0)

