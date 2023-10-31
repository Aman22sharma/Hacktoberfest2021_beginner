import cv2 as cv

#Reading Images __________________________________________________


# Reading an image
# This message takes in the path of the image and returns a matrix of pixels

# img = cv.imread(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Photos\cat_large.jpg')

# cat_large is a very big image and openCV has no method right now to resolve it and so the photo will go out of the screen

# This method references the image
# It takes in the name of the window and the matrix of pixels

# cv.imshow('Cat', img)

# Keyboard binding function
# Waits for a key to be pressed
# For 0, it will wait infinitely until the key is pressed

# cv.waitKey(0)



# Reading Videos_________________________________________________

# It can take integer arguments if you are using a webcam --> 0, 1 for other cameras and so on
capture = cv.VideoCapture(r'C:\Users\PIYUS\Desktop\Image Processing\learning\Resources\Videos\dog.mp4')

while True:

    # returns wether the frame is read successfully or not, becasue the video is read frame by frame
    isTrue, frame = capture.read()

# Passing on the above frame to show it and this will be done recursively
    cv.imshow('Video', frame)

# To stop the video from playing indefinitely
#If letter d is pressed then break out
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Releasing the capture pointer
capture.release()
cv.destroyAllWindows()

# Result : The video is played frame by frame
# (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'........This error means that the function could not find frames to play. Same error will come when we provide a wrong path.

# __________________________________________________