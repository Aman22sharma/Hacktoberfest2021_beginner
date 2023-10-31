import numpy as np
import cv2 as cv
import os

people = []
for i in os.listdir(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Faces\train'):
    people.append(i)

haar_cascade = cv.CascadeClassifier(r'C:\Users\PIYUS\Desktop\Image Processing\learning\harr_face.xml')

features = np.load('features.npy', allow_pickle=True)
labels = np.load("labels.npy", allow_pickle=True)

# features = np.load(r'C:\Users\PIYUS\Desktop\Image Processing\learning\features.npy')
# lables = np.load(r'C:\Users\PIYUS\Desktop\Image Processing\learning\labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Faces\val\elton_john\1.jpg')
cv.imshow("Ben", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 6)

for (x,y,a,b) in faces_rect:
    faces_roi = gray[x:x+a, y:y+b]
    label, confidence = face_recognizer.predict(faces_roi )
    print(f"label = {people[label]} with a confidence of {confidence}")

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, 255, 2)
    cv.rectangle(img, (x,y), (x+a,y+b), (0,255,0), 2 )

cv.imshow("Detected Face", img)

cv.waitKey(0)