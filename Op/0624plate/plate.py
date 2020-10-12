import cv2
import numpy as np
from PIL import Image
from pytesseract import *
from pip._vendor.msgpack.fallback import xrange

img = cv2.imread('../numimg/num3.jpg')
img = cv2.resize(img,(640,420))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 흑백:첫단계 - 단순화
blur = cv2.GaussianBlur(gray,(3,3),0)#블러:잡음(노이즈) 제거
#threshold(임계값 지정해서 그 값보다 높으면 흰색, 아니면 검은색
canny = cv2.Canny(blur, 75, 200)#윤곽 도출
#contour 관련있는 영역끼리 분리 -> 많은 영역 만들어짐 -> 번호판만 추출
#번호판만 추출 로직
#h/w은 1/5~1/7 이고 넓이가 500이상
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in xrange(len(contours)):
    cnt = contours[i]

    area = cv2.contourArea(cnt)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    h = box[0][1]-box[1][1]
    w = box[2][0]-box[1][0]
    if w==0:
        continue
    if 1/6 <= h/w <= 1/4 and area>=500:
        img = cv2.drawContours(img, [box], 0, (0,0,255), 2)
        roi = img[box[1][1]:box[0][1], box[1][0]:box[2][0]]

res = Image.fromarray(roi)
text = pytesseract.image_to_string(res,lang='eng')
print(text)

cv2.imshow('res1', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()