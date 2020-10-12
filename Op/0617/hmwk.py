import cv2
import numpy as np

imgs = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg']
imgcnt = 0
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
cv2.imshow('image', cv2.imread(imgs[imgcnt], cv2.IMREAD_COLOR))

# callback함수
def Previous():
    global imgcnt
    if imgcnt > 0:
        imgcnt -= 1
    else:
        pass
def Next():
    global imgcnt
    if imgcnt < 3:
        imgcnt += 1
    else:
        pass
def Capture():
    global capture,ret,frame
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    cv2.imshow('b', frame)
    cv2.imwrite('test1.jpg', frame)
    cv2.waitKey(0)

def Save():
    print('save')

while (1):
    show = cv2.imread(imgs[imgcnt], cv2.IMREAD_COLOR)
    cv2.imshow('image', show)
    key = cv2.waitKey(0) & 0xFF
    if key == 112:
        Previous()
    elif key == 110:
        Next()
    elif key == 99:
        Capture()
    elif key == 115:
        Save()
    elif key == 27:
        break
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# p // 112
# n // 110
# c // 99
# s // 115
