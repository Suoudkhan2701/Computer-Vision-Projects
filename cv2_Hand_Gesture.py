import cv2
import numpy as np
import mediapipe as mp
cam = cv2.VideoCapture(0)
hands=mp.solutions.hands.Hands(False,2,1,0.5)
mpDraw=mp.solutions.drawing_utils
while True:
    ignore, frame = cam.read()
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frame1)
    if results.multi_hand_landmarks != None:
        for handlandmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,handlandmarks,mp.solutions.hands.HAND_CONNECTIONS)
    cv2.imshow("MyCam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cam.release()