import cv2
import numpy as np
xPos=0
yPos=0
var=0
def callback1(val):
    global xPos
    xPos=val
    print("xPos:",val)
def callback2(val):
    global yPos
    yPos=val
    print("yPos:",val)
def callback3(val):
    global var
    var=val
    print("Radius:",var)
width=1280
height=720
cam =cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
cv2.namedWindow("Trackbars")
cv2.createTrackbar("xPos","Trackbars",0,1280,callback1)
cv2.createTrackbar("yPos","Trackbars",0,720,callback2)
cv2.createTrackbar("radius","Trackbars",0,1280,callback3)
while True:
    ignore, frame=cam.read()
    cv2.circle(frame, (xPos, yPos), var, (255, 0, 0), 2)
    cv2.imshow("MyCam",frame)
    cv2.moveWindow("MyCam",0,0)
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
cam.release()

#cv2.rectangle(frame,(540,200),(800,100),(0,0,0),-1)
#cv2.putText(frame,"Hi",(5