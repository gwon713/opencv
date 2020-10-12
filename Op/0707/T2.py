import cv2, glob
import numpy as np

files = glob.glob('../alphaimg/*.jpg')
path = '../alphaimg/'
al = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','u','v','w','x','y','z']
idx = 0
csv_f = open(path+'al.csv', 'w', encoding='utf-8')
for x in files:
    img = cv2.imread(x, 0)
    cv2.resize(img, (25,25))
    fdata = img.ravel()
    img_data = list(map(lambda n: str(n), fdata))
    print(img_data)
    csv_f.write(al[idx]+',')
    csv_f.write(','.join(img_data)+'\r\n')
    if idx < 24:
        idx+=1

csv_f.close()