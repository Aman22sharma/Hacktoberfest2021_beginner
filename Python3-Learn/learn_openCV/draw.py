import numpy as np
import cv2 as cv

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# Remarks : uint8 is the datatype of an image
# In blank, we are setting the height, width and no of color channels, which is 3

# blank[:] = 0,255,0
# cv.imshow("Green", blank)

# blank[250:750, 250:750] = 0, 0, 255
# cv.imshow("Red", blank)

#Drawing a rectange
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), 2)
# cv.imshow("Rectangle", blank)

# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness = -1)
# # The negative 1 completely fills the box
# cv.imshow("Full", blank)

# Another way to reference the width and height
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,0,255) , -1)
# cv.imshow("Reference", blank)

# Circle
# cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0,255,0), -1)
# cv.imshow("Circle", blank)

# Line
# cv.line(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (255,0,0), 1)
# cv.imshow("Line", blank)

# Text
cv.putText(blank, "Hello", (0,255), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0), 1)
cv.imshow('Text', blank)
cv.waitKey(0)