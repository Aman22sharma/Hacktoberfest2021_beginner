import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype='uint8')
# cv.imshow("Blank", blank)

rectangle = cv.rectangle(blank, (20,20), (400,400), 255, 1)
cv.imshow("rectangle", rectangle)

cv.waitKey(0)
# img = cv.imread(r"C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\lady.jpg")
# cv.imshow("img", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# haar_cascade = cv.CascadeClassifier(r'C:\Users\PIYUS\Desktop\Image Processing\learning\harr_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# print(faces_rect)

# # # minNeighbours is for no of neighbours the rectangle should have to be called face
# # # this function will return the rectangular coordinates of the rectangle
# # # To reduce the noice we have to caliberate the scale factors and min neighbors

# print('Number of faces found = ', len(faces_rect))

# for (x,y,w,h) in faces_rect:
#     # print(x," ",y," ",w," ",h)
#     # print( (x,y,w,h) )
#     # cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
#     cv.rectangle(img, (175,136), (175 + 266,136+266), 255, 2)

    
# cv.imshow("detected Faces", img)



# cv.waitKey(0)