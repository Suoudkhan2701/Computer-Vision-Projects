import cv2
import numpy as np
img=cv2.imread(r"C:\Users\suoud\OneDrive\Documents\flower.jpg")
cv2.imshow("Picture",img)
a=np.zeros((5,5),np.uint8)
ar=cv2.erode(img,a)
cv2.imshow("Erode",ar)
if cv2.waitKey(0) & 0xFF == ord("q"):
   cv2.destroyWindow()