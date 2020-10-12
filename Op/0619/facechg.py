import cv2
import numpy as np
import copy
#-*- coding:utf-8 -*-
cascade_file = 'C:\\Users\\Playdata\\Desktop\\mydata\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_file)

img1 = cv2.imread('face1.jpg')
img2 = cv2.imread('face2.jpg')

def nothing(x):
    pass


cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing)

f1_g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
f2_g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

f1_list= cascade.detectMultiScale(f1_g,scaleFactor=1.1,minNeighbors=1, minSize = (150,150))
f2_list= cascade.detectMultiScale(f1_g,scaleFactor=1.1,minNeighbors=1, minSize = (150,150))
if len(f1_list)>0 and len(f2_list)>0:
    x1, y1, w1, h1 = f1_list[0]
    x2, y2, w2, h2 = f2_list[0]
else:
    print("no face. program exit")
    quit()
roi1= img1[y1:y1+h1, x1:x1+w1]
roi2= img2[y2:y2+h2, x2:x2+w2]
while True:
    tmp = copy.deepcopy(img1)
    w= cv2.getTrackbarPos('W','image')

    dst= cv2.addWeighted(roi1, float(100-w)*0.01, roi2, float(w)*0.01, 0)
    tmp[y1:y1+h1, x1: x1+w1]=dst
    cv2.imshow('image',tmp)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()