'''
AUTHOR: Priyanshu
Python3 Concept: Screen recorder in python
GITHUB: https://github.com/priyanshuc4423
'''

import cv2
import numpy
import pyautogui
import time

Screen_size = (1920,1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(Screen_size))

fps = 120
prev = 0

while True:
        time_elapsed = time.time() - prev
        images = pyautogui.screenshot()
        if time_elapsed > 1.0/fps:
            prev =  time.time()
            frame = numpy.array(images)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            out.write(frame)
        cv2.waitKey(1)

cv2.destroyAllWindows()
out.release()
