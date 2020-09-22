import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

#img=cv2.imread("sudoku.jpg")
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cap=cv2.VideoCapture('road_car_view.mp4')
#cap=cv2.VideoCapture('highway.mp4')
#cap=cv2.VideoCapture(0)
def nothing(x):
    pass

a_min=0
a_max=0
cv2.namedWindow('TrackBar')
cv2.createTrackbar('Area_min','TrackBar',0,200000,nothing)
cv2.createTrackbar('Area_max','TrackBar',0,200000,nothing)
#cv2.createTrackbar('Area_min','TrackBar',0,2000,nothing)
#cv2.createTrackbar('Area_max','TrackBar',0,2000,nothing)

    #cv2.fillPoly(mask, polygons, 255) 

while True:
    _,img=cap.read()
    imgg=img.copy()
    imggg=img.copy()
    img[0:450,:]=[0,0,0]
    #img[0:250,:]=[0,0,0]

   
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect edges
    edges=cv2.Canny(gray,150,300)

    #to detect lines we will use hough transfer method
    #adjust the threshold and maxlinegap according to need
    lines=cv2.HoughLinesP(edges,4,np.pi/180,1,maxLineGap=20)#edges,rho,theta,threshold(high the threshold less the lines)

    #print(lines)

    #draw these lines
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),10)
    ##############################################
    lower=np.array([0,0,0])
    upper=np.array([0,255,0])
    mask=cv2.inRange(img,lower,upper)
    mask=cv2.bitwise_not(mask)

    result = cv2.bitwise_and(img,img,mask = mask)
    a_min=cv2.getTrackbarPos('Area_min','TrackBar')
    a_max=cv2.getTrackbarPos('Area_max','TrackBar')
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)#(image,contour retrival mode,contour approximation methord)
    for i in contours:
        area = cv2.contourArea(i)
        if area>=a_min and area<a_max:
            cv2.drawContours(imgg, i, -1, (0, 0, 255),3)#(image on which to draw contour,contours,index of contour(-1 for all),color,thickness)
            cv2.fillPoly(imgg, [i], (0,0,255))
            #rotated rectangle forms rectangle around with smallest area
            #rect = cv2.minAreaRect(i)
            #box = cv2.boxPoints(rect)
            #box = np.int0(box)
            #rot_rect_draw = cv2.drawContours(imgg,[box],0,(0,0,255),2)
            lower=np.array([0,0,254])
            upper=np.array([0,0,255])
            mask=cv2.inRange(imgg,lower,upper)
            result = cv2.bitwise_and(img,img,mask = mask)
            
        
            
                
            
    cv2.imshow("road",result)    
    cv2.imshow("result",imgg)
    cv2.imshow("mask",mask)
    cv2.imshow("img",img)
    cv2.imshow("original",imggg)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
