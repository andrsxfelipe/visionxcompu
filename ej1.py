import cv2
import numpy as np
W = 100
H = 100
im=np.zeros((W,H,3),np.uint8)

def show_im(im):
    cv2.imshow('window',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cuadrados():
    for i in range(19,80):
        for j in range(19,80):
            im[i,j] = (0,0,255)

    for i in range(29,70):
        for j in range(29,70):
            im[i,j] = (0,255,0)

    for i in range(39,60):
        for j in range(39,60):
            im[i,j] = (255,0,0)
    for i in range(44,55):
        for j in range(44,55):
            im[i,j] = (0,0,0)

#--
for i in range(0,100,3):

    im[5,i] = (255,0,0)
for i in range(1,100,5):
    im[6,i] = (255,0,0)
for i in range(2,100,5):
   im[6,i] = (255,0,0)
for i in range(4,100,5):
    im[4,i] = (255,0,0)
for i in range(5,100,5):
   im[4,i] = (255,0,0)

#--

#cuadrados()           
show_im(im)