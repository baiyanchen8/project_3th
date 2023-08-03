import cv2
import numpy as np
Baboon=cv2.imread('picture/Baboon.tif')
Baboon = cv2.cvtColor(Baboon, cv2.COLOR_BGR2GRAY)
Lena=cv2.imread('picture/Lena.png')
Lena = cv2.cvtColor(Lena, cv2.COLOR_BGR2GRAY)
cv2.imshow('Baboon', Baboon)
cv2.waitKey(0)
cv2.destroyAllWindows()
# a
mat_Baboon= np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        k=bin(Baboon[i][j])
        mat_Baboon[i][j]=Baboon[i][j]>=128 if 1 else 0
# b
cv2.imshow('Baboon',mat_Baboon)
cv2.waitKey(0)
cv2.destroyAllWindows()
# c
Stego = np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        if mat_Baboon[i][j]==0:
            Stego[i][j]=Lena[i][j]  &~1 
        else :    
            Stego[i][j]=Lena[i][j]  | 1
cv2.imshow('Lena',Stego)
cv2.waitKey(0)
cv2.destroyAllWindows()
# d
mat_Stego= np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        k=bin(Stego[i][j])
        mat_Stego[i][j]=Stego[i][j]>=128 if 1 else 0
# E
for i in range(512):
    for j in range(512):
        if mat_Stego[i][j]==0:
            Lena[i][j]=Lena[i][j]  &~1 
        else :    
            Lena[i][j]=Lena[i][j]  | 1
cv2.imshow('Lena',Lena)
cv2.waitKey(0)
cv2.destroyAllWindows()