import cv2
import numpy as np
import random
from matplotlib import pyplot as plt
from pip._vendor.msgpack.fallback import xrange
import copy

img = cv2.imread('../numimg/num.jpg')
img = cv2.resize(img, (600,420))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
canny = cv2.Canny(blur, 75, 200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

max_w = 0
max_c = None

for i in xrange(len(contours)):
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    if max_w < w:
        max_w = w
        max_c = cnt
        x1, y1, w1, h1 = x, y, w, h
img2 = copy.deepcopy(img)
img3 = copy.deepcopy(img)
img2 = cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 3)
img2 = cv2.drawContours(img2, [max_c], -1, (b, g, r), 2)

x_list = []
y_list = []

for i in range(0,len(max_c)):
    x_list.append(max_c[i][0][0])
    y_list.append(max_c[i][0][1])

p1 = max_c[x_list.index(min(x_list))][0]
p2 = max_c[x_list.index(max(x_list))][0]
p3 = max_c[y_list.index(min(y_list))][0]
p4 = max_c[y_list.index(max(y_list))][0]

cv2.circle(img2, (p1[0],p1[1]), 5, (0,0,255),-1)
cv2.circle(img2, (p2[0],p2[1]), 5, (255,0,0),-1)
cv2.circle(img2, (p3[0],p3[1]), 5, (0,255,0),-1)
cv2.circle(img2, (p4[0],p4[1]), 5, (0,0,0),-1)

cv2.imshow('res1', img2)

pts1 = np.float32([p1,p2,p3,p4])
pts2 = np.float32([[0,0],[0,300],[400,0],[400,300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img3, M, (300,400))

cv2.imshow('res2', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()