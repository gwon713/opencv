import cv2

# cap 이 정상적으로 open이 되었는지 확인하기 위해서 cap.isOpen() 으로 확인가능
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3),cap.get(4)))
cap.set(3,320)
cap.set(4,240)

while(True):
    ret, frame = cap.read()

    if (ret):
        gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imshow('b', gray)
            cv2.imwrite('test1.jpg', gray)
            cv2.waitKey(0)

        elif cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()