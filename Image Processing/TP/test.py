import cv2
import numpy as np
img=cv2.imread ("horse.jpg");
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v= cv2.split(hsv)
ret_h, th_h = cv2.threshold(h,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret_s, th_s = cv2.threshold(s,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#Fusion th_h et th_s
th=cv2.bitwise_or(th_h,th_s)
#Ajouts de bord à l'image
bordersize=10
th=cv2.copyMakeBorder(th, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
#Remplissage des contours
im_floodfill = th.copy()
h, w = th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
th = th | im_floodfill_inv
#Enlèvement des bord de l'image
th=th[bordersize: len(th)-bordersize,bordersize: len(th[0])-bordersize]
resultat=cv2.bitwise_and(img,img,mask=th)
cv2.imwrite("im_floodfill.png",im_floodfill)
cv2.imwrite("th.png",th)
cv2.imwrite("resultat.png",resultat)
contours, hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range (0, len(contours)) :
    mask_BB_i = np.zeros((len(th),len(th[0])), np.uint8)
    x,y,w,h = cv2.boundingRect(contours[i])
    cv2.drawContours(mask_BB_i, contours, i, (255,255,255), -1)
    BB_i=cv2.bitwise_and(img,img,mask=mask_BB_i)
    if h >15 and w>15 :
        BB_i=BB_i[y:y+h,x:x+w]
        cv2.imwrite("BB_"+str(i)+".png",BB_i)