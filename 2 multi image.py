import cv2, glob
import numpy as np
from matplotlib import pyplot as plt
import os,sys
import os.path
images=glob.glob(r'D:\python\Final Code\*jpg')
output1=r'D:\New folder\binary'
output2=r'D:\New folder\otsu'
output3=r'D:\New folder\gaussian'
                  
for image in images:
    img = cv2.imread(image)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    print (img.shape)
    r = 500.0 / img.shape[1]
    dim = (500, int(img.shape[0] * r))
    
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

##    hist = cv2.equalizeHist(resized)
    
    gaussian = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    retva12,Otsu = cv2.threshold(resized,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    retval,binary = cv2.threshold(resized, 110, 255, cv2.THRESH_BINARY)
    
    
    name = os.path.splitext(output1)[0]
    basename=os.path.basename(image)

    imgname1= os.path.join(output1,basename)
    cv2.imwrite(imgname1, binary)
    imgname2= os.path.join(output2,basename)
    cv2.imwrite(imgname2, Otsu)
    imgname3= os.path.join(output3,basename)
    cv2.imwrite(imgname3, gaussian)



##    cv2.imshow("gaussian", gaussian)
##    cv2.imshow('Otsu',Otsu)
##    cv2.imshow('binary',binary)

##    cv2.imshow('resized',resized)

##    cv2.imshow('hist',hist)
    cv2.waitKey(10)
    cv2.destroyAllWindows()


