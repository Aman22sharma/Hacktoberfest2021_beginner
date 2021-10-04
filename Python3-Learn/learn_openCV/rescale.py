# We resize and rescale images to prevent computational strain

import cv2 as cv

capture = cv.VideoCapture(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Videos\dog.mp4')

# Function to resize/rescale..
#***For images, video and live videos
def rescaleFrame(frame, scale=0.75):
# Scale has been set default to  0.75
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimension = (width,height)

# Resize function resizes the image to a particular dimension
    return cv.resize(frame,      dimension,            interpolation=cv.INTER_AREA)
            #        the frame   to what dimesnion       ????

while True:

    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# Another way to change resolution
# ******This works ONLY for live video**********
def changeRes(width,height):
# 3 and 4 are for referencing. 10 is for brightness and so on
    capture.set(3,width)
    capture.set(4,height)
