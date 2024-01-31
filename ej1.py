import cv2
import numpy as np
W = 100
H = 100
im=np.zeros((W,H,3),np.uint8)

def show_im(im):
    cv2.imshow('window',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
          
show_im(im)