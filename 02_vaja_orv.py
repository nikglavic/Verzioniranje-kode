import cv2 
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

imgGray = cv2.imread('lenna.png',0)

cv2.namedWindow("Slika")
cv2.imshow("Slika", imgGray)
cv2.waitKey()
cv2.destroyAllWindows()