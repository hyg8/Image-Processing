import cv2
import numpy as np
img=cv2.imread("horse.jpg");
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',th)
cv2.waitKey(0)
cv2.destroyAllWindows()