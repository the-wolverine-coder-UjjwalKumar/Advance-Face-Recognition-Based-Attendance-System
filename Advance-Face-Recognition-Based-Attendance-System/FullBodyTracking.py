import numpy as np
import cv2

# used for face
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# used for full body
detector= cv2.CascadeClassifier('haarcascade_fullbody.xml')

# object of videocapture 
cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()