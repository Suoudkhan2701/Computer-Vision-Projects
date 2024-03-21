import cv2
import numpy as np
Hue1=0
Sat1=0
Val1=0
Hue2=0
Sat2=0
Val2=0
def callback1(val):
    global Hue1
    Hue1=val
    print("Hue1:",Hue1)
def callback2(val):
    global Sat1
    Sat1=val
    print("Hue1:",Sat1)
def callback3(val):
    global Val1
    Val1=val
    print("Hue1:",Val1)
def callback4(val):
    global Hue2
    Hue2=val
    print("Hue1:",Hue2)
def callback5(val):
    global Sat2
    Sat2=val
    print("Hue1:",Sat2)
def callback6(val):
    global Val2
    Val2=val
    print("Hue1:",Val2)
width=1280
height=720
cam =cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue1","Trackbars",0,1280,callback1)
cv2.createTrackbar("Saturation1","Trackbars",0,720,callback2)
cv2.createTrackbar("Value1","Trackbars",0,1280,callback3)
cv2.createTrackbar("Hue2","Trackbars",0,1280,callback4)
cv2.createTrackbar("Saturation2","Trackbars",0,720,callback5)
cv2.createTrackbar("Value2","Trackbars",0,1280,callback6)
while True:
    ignore, frame=cam.read()
    cv2.imshow("MyCam",frame)
    cv2.resize(frame,(640,320))
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    LB = np.array([Hue1, Sat1, Val1])
    UB = np.array([Hue2, Sat2, Val2])
    Mask=cv2.inRange(frameHSV,LB,UB)
    cv2.imshow("HSV",frameHSV)
    cv2.resize(frameHSV, (640, 320))
    cv2.imshow("Mask",Mask)
    cv2.resize(Mask, (640, 320))
    img=cv2.bitwise_and(frame,frame,mask=Mask)
    cv2.imshow("Masked",img)
    cv2.moveWindow("MyCam",0,0)
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
cam.release()