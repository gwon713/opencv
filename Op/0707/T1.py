import cv2

gray_img = cv2.imread('../img/alp.png',0)
path = '../alphaimg/'
h, w = gray_img.shape

al_w = w/26
ww = 0

imgs = []
alpha = 65
for i in range(0, 26):
    img = gray_img[0:h, int(i*al_w):int(ww+al_w)]
    ww += al_w
    imgs.append(img)
    cv2.imshow(str(i), img)
    cv2.imwrite(path+chr(alpha)+'.jpg',img=img)
    alpha+=1

cv2.waitKey(0)
cv2.destroyAllWindows()
