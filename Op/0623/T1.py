import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/name.jpg')
# [x,y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상->좌하->우상->우하
pts1 = np.float32([[1450,1050],[790,1700],[2400,2250],[1670,2750]])

# 좌표의 이동점
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (1450,1050), 20, (255,0,0),-1)
cv2.circle(img, (790,1700), 20, (0,255,0),-1)
cv2.circle(img, (2400,2250), 20, (0,0,255),-1)
cv2.circle(img, (1670,2750), 20, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1000,1000))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
plt.show()
