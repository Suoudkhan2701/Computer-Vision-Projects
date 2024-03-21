import cv2
import numpy as np
faceCascade=cv2.CascadeClassifier(r'C:\Users\suoud\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalcatface.xml')
cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    frameGRAY=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGRAY,1.1,5)
    for face in faces:
        x,y,z,a=face
        cv2.rectangle(frame,(x,y),((x+z),(y+a)),(255,0,0),3)
    cv2.imshow("MyCam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cam.release()