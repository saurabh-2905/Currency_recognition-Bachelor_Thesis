
import cv2
import numpy as np
import os,sys
import os.path
import cv2, glob
images=glob.glob(r'D:\python\template\cropped denomination_(FINAL)\*.jpg')
c=1

for image in images:
    img_rgb = cv2.imread(r'D:\python\Final Code\New folder\CURRENCIES DATABASE\EURO\EURO-10-F.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(image,0)
    w, h = template.shape[::-1]

##    print (img_gray.shape)
    r = 500.0 / img_gray.shape[1]
    dim = (500, int(img_gray.shape[0] * r))

    resized1 = cv2.resize(img_rgb, dim, interpolation = cv2.INTER_AREA)    
    resized2 = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)


    retval,binary = cv2.threshold(resized2, 110, 255, cv2.THRESH_BINARY)

    res = cv2.matchTemplate(binary,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where( res >= threshold)
    a,b=loc[::-1]

    for pt in zip(*loc[::-1]):
        cv2.rectangle(binary,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
        cv2.rectangle(resized1,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

##    print (a,b)
    print (c)
    

    if  a != ():
        cv2.imshow('detected',resized1)
        cv2.imshow('binary',binary)

        
        basename=os.path.basename(image) 
        name=os.path.splitext(basename)[0]
        
        if (c==2):
            print("Currency: Australian Dollar")
            print('Denomination: 10')
            
        print (name)
        
        break
    c=c+1
    
    cv2.destroyAllWindows()
    

