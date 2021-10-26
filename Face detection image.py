# face detection using "Haar feature based cascade classifier".
# Object detection approach.
# this is a machine learning based approach...
# where a cascade fn is trained for a lot of +ve and -ve images...
# a classifier is trained with few hundred images of a particular object(face) that is +ve example.

# we want to train the classifier with the negative images...
# the object(face) is absent in this case.

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('my image.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# scale factor i.e. 2nd argument is...
# "how much the image size is reduced at each scale".
# 3rd is minNeighbours...
# how many neighbours each candidate rectangle should have to retain it.
faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow('Original',img)
cv2.waitKey()
