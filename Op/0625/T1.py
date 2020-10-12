import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img, (0,0),(511,511),(255,255,255),5)

img = cv2.rectangle(img, (100,100),(300,300),(0,0,255),10)

img = cv2.circle(img, (400,400), 50, (0,255,0), 5)

img = cv2.ellipse(img, (250,250),(100,50),0,0,100,(255,0,0),-1)
# pts = np.array([[100,400],[0,400],[200,500]], np.int32)
# pts = pts.reshape((-1,1,2))
img = cv2.polylines(img, [[100,400],[0,400],[200,500]],True,[100,100,100])
