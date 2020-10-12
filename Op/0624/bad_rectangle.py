import cv2
import numpy as np
from matplotlib import pyplot as plt
from urllib3.connectionpool import xrange

img = cv2.imread('../img/brec.jpg')
img1 = img.copy()
img2 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

# 적용하는 숫자가 커질 수록 Point의 갯수는 감소
epsilon1 = 0.01*cv2.arcLength(cnt, True)
epsilon2 = 0.1*cv2.arcLength(cnt, True)

approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

cv2.drawContours(img, [cnt],0,(0,255,0),3) # 215개의 Point
cv2.drawContours(img1, [approx1], 0,(0,255,0), 3) # 21개의 Point
cv2.drawContours(img2, [approx2], 0,(0,255,0), 3) # 4개의 Point

titles = ['Original', '1%', '10%']
images = [img, img1, img2]

for i in xrange(3):
    plt.subplot(1,3,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()