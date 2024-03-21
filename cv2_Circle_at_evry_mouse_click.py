import cv2
import numpy as np
pnt=0
ev=0
def mouseclick(event,xPos,yPos,flags,params):
    global pnt
    global ev
    if (event==cv2.EVENT_LBUTTONDOWN):
        ev=event
        pnt=(xPos,yPos)
    elif (event==cv2.EVENT_LBUTTONUP):
        ev=0
        print(xPos,yPos)
width=1280
height=720
cam =cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
cv2.namedWindow("MyCam")
cv2.setMouseCallback("MyCam",mouseclick)
while True:
    ignore, frame=cam.read()
    if (ev==1):
        cv2.circle(frame,pnt,30,(255, 0, 0),1)
    cv2.imshow("MyCam",frame)
    cv2.moveWindow("MyCam",0,0)
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
cam.release()

#cv2.rectangle(frame,(540,200),(800,100),(0,0,0),-1)
#cv2.putText(frame,"Hi",(540,280),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),2)