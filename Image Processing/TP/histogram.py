# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

img = cv2.imread('horse.jpg',cv2.IMREAD_GRAYSCALE)
#-----------------------------
# Affichage des valeurs min et max des pixels de l'image
print ('Valeurs min et max de l image en niveau de gris')
print(' np.min(img)')
print(' np.max(img)')

#-----------------------------
# Histogramme de l'image
plt.subplot(421),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(422),plt.hist(img.ravel(), bins=256);
plt.title('Histogram'), plt.xticks([]), plt.yticks([])

#-----------------------------
# Histogramme de l'image rÃ©elle (non modifiÃ©e par matplotlib Ã  l'affichage)
img2 = deepcopy(img); #.copy();
img2[0,0]=0 # premier pixel noir
img2[0,1]=255 # second pixel blanc
plt.subplot(423),plt.imshow(img2, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(424),plt.hist(img2.ravel(),256);
plt.title('Histogram'), plt.xticks([]), plt.yticks([])

#-----------------------------
# Min-Max
img_minmax = deepcopy(img);
val_min = np.min(img)
val_max = np.max(img)
coef = 1.0*255/(val_max-val_min);
img_minmax = (img_minmax-val_min)*coef;
img_minmax[0,0]=0
img_minmax[0,1]=255
plt.subplot(425),plt.imshow(img_minmax, cmap = 'gray')
plt.title('Min-Max'), plt.xticks([]), plt.yticks([])
plt.subplot(426),plt.hist(img_minmax.ravel(),256);
plt.title('Histogram'), plt.xticks([]), plt.yticks([])

#-----------------------------
# Egalisation d'histogramme
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum() # calcul de l'histogramme cumulÃ©
cdf = (cdf)*255/(cdf.max()) # normalisation entre 0 et 255
img_egalisee = cdf[img] # remplacement des valeurs de l'image

print ('Valeurs min et max de l image egalisee en niveau de gris')
print ('np.min(img_egalisee)')
print(' np.max(img_egalisee)')
img_egalisee[0,0]=0
img_egalisee[0,1]=255

plt.subplot(427),plt.imshow(img_egalisee, cmap = 'gray')
plt.title('Egalisation d histogramme'), plt.xticks([]), plt.yticks([])
plt.subplot(428),plt.hist(img_egalisee.ravel(),256,[0,256]);
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('..\Data\Meduse_egalisee.jpg', img_egalisee)
cv2.destroyAllWindows()
