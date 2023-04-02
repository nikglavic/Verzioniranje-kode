import cv2 
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def my_roberts(slika):
    slika_robov=np.zeros(slika.shape, dtype=np.uint8)
    jedro1=np.array([[1,0],[0,-1]])
    jedro2=np.array([[0,1],[-1,0]])

    maska1=np.zeros(slika.shape[:2])
    maska2=np.zeros(slika.shape[:2])

    for i in range(0, slika.shape[0]-1):
        for j in range(0, slika.shape[1]-1):
            del_slike=slika[i:i+2, j:j+2]
            maska1[i,j]=np.sum(del_slike*jedro1)
            maska2[i,j]=np.sum(del_slike*jedro2)
    slika_robov=np.sqrt(np.square(maska1)+np.square(maska2))
    slika_robov=np.uint8(slika_robov)

    return slika_robov

def my_prewitt(slika):
    slika_robov=np.zeros(slika.shape, dtype=np.uint8)
    jedro1=np.array([[1,0, -1],[1, 0,-1], [1,0,-1]])
    jedro2=np.array([[1,1,1],[0,0,0], [-1,-1,-1]])

    maska1=np.zeros(slika.shape[:2])
    maska2=np.zeros(slika.shape[:2])

    for i in range(0, slika.shape[0]-2):
        for j in range(0, slika.shape[1]-2):
            del_slike=slika[i:i+3, j:j+3]
            maska1[i,j]=np.sum(del_slike*jedro1)
            maska2[i,j]=np.sum(del_slike*jedro2)
    slika_robov=np.sqrt(np.square(maska1)+np.square(maska2))
    slika_robov=np.uint8(slika_robov)

    return slika_robov 

def my_sobel(slika):
    
    return slika_robov 

def canny(slika, sp_prag, zg_prag):
    
    return slika_robov 

imgGray = cv2.imread('lenna.png',0)

cv2.namedWindow("Slika")
cv2.imshow("Slika", my_prewitt(imgGray))
cv2.waitKey()
cv2.destroyAllWindows()