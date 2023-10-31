import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Faces\train'):
    people.append(i)
haar_cascade = cv.CascadeClassifier(r'C:\Users\PIYUS\Desktop\Image Processing\learning\harr_face.xml')
print(people)

DIR = r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Faces\train'

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)


            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h , x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training done______________________")

features = np.array(features, dtype='object')
labels = np.array(labels)

# This is an instance of the training algorithm
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Training this recognizer
face_recognizer.train(features, labels)


# This is saving the trained model
face_recognizer.save(r'C:\Users\PIYUS\Desktop\Image Processing\learning\face_trained.yml')
np.save('Features.npy', features)
np.save('labels.npy', labels)
