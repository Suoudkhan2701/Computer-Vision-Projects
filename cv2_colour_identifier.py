import cv2
import numpy as np
x=0
y=0
pnt=0
r=''
def func1(event,xPos,yPos,flags,param):
    global x
    global y
    global pnt
    global r
    if (event==cv2.EVENT_LBUTTONDOWN):
        x=xPos
        y=yPos
        pnt=[x,y]
        r=str(pnt)
cam=cv2.VideoCapture(0)
cv2.namedWindow("MyCam")
cv2.setMouseCallback("MyCam",func1)
while True:
    ignore, frame = cam.read()
    new = np.zeros([250, 250, 3], dtype=np.uint8)
    z=frame[x,y]
    new[:, :] = z
    cv2.putText(new,r,(0,50),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,0),2)
    cv2.imshow("Color", new)
    cv2.imshow("MyCam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cam.release()