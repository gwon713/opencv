import cv2
import numpy as np
from matplotlib import pyplot as plt
from urllib3.connectionpool import xrange

img = cv2.imread('../img/rabbit.jpg')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[3] # 1이 손모양 주변의 contour
hull = cv2.convexHull(cnt)

cv2.drawContours(img1, [hull], 0,(0,255,0), 3)

titles = ['Original','Convex Hull']
images = [img, img1]

for i in xrange(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()