import cv2
import numpy as np
import mediapipe as mp
a=[]
cam = cv2.VideoCapture(0)
hands=mp.solutions.hands.Hands(False,2,1,0.5)
mpDraw=mp.solutions.drawing_utils
while True:
    ignore, frame = cam.read()
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frame1)
    if results.multi_hand_landmarks != None:
        for handlandmark in results.multi_hand_landmarks:
            for landmark in handlandmark.landmark:
                a.append([landmark.x,landmark.y])
        mpDraw.draw_landmarks(frame, handlandmark, mp.solutions.hands.HAND_CONNECTIONS)
        if a[0][0]>a[0][1]:
            cv2.putText(frame,"Left",(255,255),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,0),3)
        elif a[0][0]<a[0][1]:
            cv2.putText(frame, "Right", (255, 255), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)
    print(a)
    cv2.imshow("MyCam",frame)
    a=[]
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cam.release()