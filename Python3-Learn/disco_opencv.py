import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)
i=0

while True:
    ret, frame = cap.read()
    blank = np.zeros(frame.shape[:2], dtype='uint8')
    b,g,r = cv.split(frame)
    
    i = i+ (1/3)
    if 0<i<=1:
        blue = cv.merge([b, blank, blank])
        cv.imshow('frame', blue)
    elif 1<i<=2:
        mid1 = cv.merge([b,g,blank])
        cv.imshow('frame', mid1)
    elif 2<i<=3:
        green = cv.merge([blank, g , blank])
        cv.imshow('frame', green)
    elif 3<i<=4: 
        mid2 = cv.merge([blank, g, r]) 
        cv.imshow('frame', mid2)  
    else: 
        red = cv.merge([blank, blank, r])
        cv.imshow('frame', red)
        if i>5:
            i=0
    
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
