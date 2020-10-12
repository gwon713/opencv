import cv2
import copy

c = cv2.CascadeClassifier('classifier/strawberrydetector.xml')
img = cv2.imread('img/strbryck.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
straw = c.detectMultiScale(gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40)
                           )
img2 = copy.deepcopy(img)
for (x, y, w, h) in straw:
    print(x)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    res = img2

if len(straw)==0:
    print('no strawberry')
else:
    cv2.imshow('res', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()