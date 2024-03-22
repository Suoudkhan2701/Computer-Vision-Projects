import cv2
import numpy as np
img=cv2.imread(r"C:\Users\suoud\OneDrive\Documents\flower.jpg")
cv2.resize(img,(5,5))
cv2.imshow("Picture",img)
img1=cv2.GaussianBlur(img,(3,3),0)
img2=cv2.medianBlur(img,5,3)
img3=cv2.bilateralFilter(img,3,4,5,6)
cv2.resize(img,(5,5))
cv2.imshow("Gaussian Blur",img1)
cv2.imshow("Median Blur",img2)
cv2.imshow("Bilateral Filter",img3)
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyWindow()