import cv2
import numpy as np
img=cv2.imread(r"C:\Users\suoud\OneDrive\Documents\flower.jpg")
print(img.shape[0],img.shape[1])
cv2.imshow("Picture",img)
cv2.copyMakeBorder(img,100,100,50,50,cv2.BORDER_CONSTANT)
'''cv2.resizeWindow("Picture",1280,620)
cv2.resize(img,(1944,2592))'''
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyWindow()