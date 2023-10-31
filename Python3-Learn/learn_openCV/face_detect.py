import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\group 1.jpg")
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier(r'C:\Users\PIYUS\Desktop\Image Processing\learning\harr_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# minNeighbours is for no of neighbours the rectangle should have to be called face
# this function will return the rectangular coordinates of the rectangle
# To reduce the noice we have to caliberate the scale factors and min neighbors

print('Number of faces found = ', len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow("detected Faces", img)



cv.waitKey(0)