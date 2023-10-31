import cv2 as cv

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\park.jpg')
cv.imshow("Image", img)

# Gray Scale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grey", gray)

# Blurring
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)


# Edge Cascading
# canny = cv.Canny(blur, 127, 128)
# cv.imshow('Edges', canny)

# Resizing
# resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
# INTER_AREA is used when we are shrinking the dimesnions
# For enlarging we use INTER_LINEAR or cubic
# cubic is slower but gives better result
# cv.imshow("Resized", resized)

cropped = img[50:200 , 200:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)