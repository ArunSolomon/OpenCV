#import the assects
import numpy as np
import cv2

# To capture the video from the webcam
cap = cv2.VideoCapture(0)

while(True):
    # Capture Frame By Frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    # Convert BGR to GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Display the resulting frame
    cv2.imshow('frame', frame) # image shown from webcam
    cv2.imshow('gray', gray) # image shown from webcam in gray
    cv2.imshow('hsv', hsv) # image shown from webcam in hsv
    # press q to close
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
