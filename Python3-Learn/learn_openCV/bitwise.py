import cv2 as cv
import numpy as np

# img = cv.imread(r'')
blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise and

bitwise_and = cv.bitwise_and(rectangle, circle)
# return intersecting regions
# cv.imshow("bitwise_and", bitwise_and)


bitwise_or = cv.bitwise_or(rectangle, circle)
# returns non-intersecting and intersecting regions
# cv.imshow("bitwise_or", bitwise_or)


bitwise_xor = cv.bitwise_xor(rectangle, circle)
# returns the non intersecting regions
cv.imshow("bitwise_xor", bitwise_xor)


bitwise_not = cv.bitwise_not(circle)
# changes 0 pixels to 1 and 1s to 0s
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)