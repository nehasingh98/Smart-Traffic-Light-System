import cv2
import numpy as np
##import matplotlib.pyplot as plt

img1=cv2.imread('car11.jpg')
img2=cv2.imread('car12.png')
img3=cv2.imread('car13.jpg')
img4=cv2.imread('car14.jpg')
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0
#Numbers instead of codes

cv2.imshow('image1',img3)
cv2.imshow('image2',img1)
cv2.imshow('image3',img2)
cv2.imshow('image4',img4)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

##plt.imshow(img, cmap='cool', interpolation='bicubic')
##plt.plot([50,100],[80,100],'c',linewidth=5)
##plt.show()
