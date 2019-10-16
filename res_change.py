#import the assects
import numpy as np
import cv2

# To capture the video from the webcam
cap = cv2.VideoCapture(0)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

# make_480p()
make_720p()
# change_res(1920, 1080)

while(True):
    # Capture Frame By Frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame', frame) # image shown from webcam
    # press q to close
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
