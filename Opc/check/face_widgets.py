import tkinter as tk
from functools import partial
import copy
import os
from tkinter import messagebox
import datetime
import cv2
import check.main as m
frame_kept = None

class video_service():
    #영상 window와 GUI window가 구분됨. 영상 window는 thread로 구현
    def __init__(self,master):
        self.cnt_learn = 0
        self.app=master
        print('비디오 서비스 초기화.')
        # CascadeClassifier xml 파일의 경로 #haarcascade_frontalface_alt2.xml
        cascade_file = 'classifier/haarcascade_frontalface_default.xml'
        self.cascade = cv2.CascadeClassifier(cascade_file)


    def video_show(self,id):
        global frame_kept
        print("show")
        cap = cv2.VideoCapture(0)
        mask=cv2.imread('img/mask.png')

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                # 이미지 반전,  0:상하, 1 : 좌우
                frame = cv2.flip(frame, 1)
                frame_small=cv2.add(frame,mask)

                gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

                # 얼굴 인식
                face_list = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(170, 170),maxSize=(245,245))

                color = (0, 0, 255)
                cx = 320
                cy = 240
                cw = 250
                ch = 250
                cv2.rectangle(frame, (cx - int(cw / 2), cy - int(ch / 2)), (cx + int(cw / 2), cy + int(ch / 2)), color,thickness=8)
                #roi=img1[vpos:rows+vpos, hpos:cols+hpos]
                if len(face_list) > 0:
                    if len(face_list)>1:
                        alertMsg="Alert ! : Too many people. Please only one person."
                        cv2.putText(frame, alertMsg, (25, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
                        frame_kept=None
                    else:
                        dst=frame_small.copy()#잘라내서 보여주기
                        dst=frame_small[cy - int(ch / 2):cy + int(ch / 2), cx - int(cw / 2): cx + int(cw / 2)]
                        frame_kept= copy.deepcopy(dst)
                        cv2.imshow('img', frame_kept)
                    for face in face_list:
                        x, y, w, h = face
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness=8)
                else:
                    # print("no face")
                    frame_kept = None
                    pass

                # 영상 화면 띄우기
                cv2.imshow('frame', cv2.resize(frame, (int(640 * 1.5), int(480 * 1.5))))
                if cv2.waitKey(1) & 0xFF == ord('s'):  # 추가 종료 조건. q 누르기
                    video_service.save(id)

                if cv2.waitKey(1) & 0xFF == ord('q'):  # 추가 종료 조건. q 누르기
                    break

        cap.release()
        cv2.destroyAllWindows()
        print('\nth exiting.')

    def save(self,id):
        print("mini_btn1_clicked")
        print("학습 저장")
        if self.write_frame(id)==True:
            self.cnt_learn+=1
            print(self.cnt_learn)
        if self.cnt_learn>4:#5회 이상 학습할 경우 종료하라고 안내함
            print('학습이 충분합니다 q를 눌러 종료')


    def write_frame(self,id):
        global frame_kept
        if frame_kept is None:
            messagebox.showerror("error", "not captured")
            return False
        else:
            pngDir='dataset/' + 'person_'+id
            print(pngDir)
            if not os.path.isdir(pngDir):
                os.mkdir(pngDir)
            cv2.imwrite(pngDir+'/At'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'.png', frame_kept)
            return True
