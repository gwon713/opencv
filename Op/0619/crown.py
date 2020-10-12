import cv2
import numpy as np
import sys
import time

faceCascade = cv2.CascadeClassifier('C:\\Users\\Playdata\\Desktop\\mydata\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

cap.set(3,800) # set Width
cap.set(4,800) # set Height
setx = 100
sety = 100
while True:
    ret, img = cap.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(setx,sety)
    )
    if len(faces) > 0:
        print(faces)
        color = (0, 0, 255)
        for (fx, fy, fw, fh) in faces:
            roi_gray = gray[fy:fy + fh, fx:fx + fw]
            roi_color = img[fy:fy + fh, fx:fx + fw]
        cv2.imwrite('back.jpg', img)
    else:
        print('no face')
    cv2.imshow('video',img) # video라는 이름으로 출력
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit # ESC를 누르면 종료
        break
cap.release()
print(fx,fy,fw,fh)
img1 = cv2.imread('crown.png')
img2 = cv2.imread('back.jpg')
if fh>200 :
    fh=160
iw, ih, ic = img1.shape
addy = fy-(fh-20)
addx = fx

print(addx,addy,iw,ih,ic)
roi = img2[addy:addy+ih,addx:addx+iw]

img1_g = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(img1_g, 235, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_s = cv2.bitwise_and(img1, img1, mask=mask_inv)
img_b = cv2.bitwise_and(roi, roi, mask=mask)

dst = cv2.add(img_s, img_b)
img2[addy:addy+ih,addx:addx+iw] = dst

cv2.imshow('img', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



