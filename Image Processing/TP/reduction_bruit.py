# -*- coding: Latin-1 -*-
# Programme de filtrage d'une image couleur
# Dominique Lefebvre pour TangenteX.com
# 14 janvier 2016
#

# importation des librairies
import sys
from PIL import Image

# définition de la fonction de convolution 2D
# avec une matrice masque de convolution de 3x3
# sur les trois canaux RGB du pixel Pix
def Convolution2D(Filtre,TPix,x,y):
    p0 = p1 = p2 = 0
    for i in range(-1,1):
        for j in range(-1,1):
            p0 += Filtre[i+1][j+1]*TPix[y+i,x+j][0]
            p1 += Filtre[i+1][j+1]*TPix[y+i,x+j][1]
            p2 += Filtre[i+1][j+1]*TPix[y+i,x+j][2]
    # normalisation des composantes
    p0 = int(p0/9.0) 
    p1 = int(p1/9.0)
    p2 = int(p2/9.0)       
    # retourne le pixel convolué
    return (p0,p1,p2)

# définition de la matrice de convolution - exemple initial
Filtre = [[-1,-2,-1],[-2,16,-2],[-1,-2,-1]]


# ouverture du fichier image
ImageFile = 'horse.jpg'
try:
   img = Image.open(ImageFile)
except IOError:
    print ('Erreur sur ouverture du fichier ' + ImageFile)
    exit(1)
#sauvegarde du nouveau image
img.save("Nouveau.jpg")   
# récupération de la largeur et hauteur de l'image
colonne,ligne = img.size
# image filtrée
imgF = Image.new(img.mode, img.size)


#boucle de traitement de l'image par convolution avec Filtre
TabPixel = img.load()
for x in range(1,ligne-1):
   for y in range(1,colonne-1):
        p = Convolution2D(Filtre,TabPixel,x,y)
        imgF.putpixel((y,x),p)
        
# affichage de l'image filtrée
imgF.show()

# fermeture du fichier image
#sauvegarde de l'image traiter

img.close()