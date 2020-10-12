import tkinter as tk
from tkinter import messagebox
import time, os, cv2, threading


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('200x400+50+300')  # 윈도우창 크기 1600*900, 위치:100,100
        self.master.resizable(True, True)
        self.pack()
        self.mode = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.mode_c = tk.Radiobutton(self, text='영상촬영모드', variable=self.mode, value=1)
        self.mode_c.pack()
        self.mode_c.invoke()  # 라디오 버튼 디폴트 체크

        self.mode_p = tk.Radiobutton(self, text='저장된파일목록보기', variable=self.mode, value=2)
        self.mode_p.pack()

    def createNewWindow(self):
        newWindow = tk.Toplevel(self)
        newWindow.geometry('200x500+300+300')
        V1 = tk.Radiobutton(newWindow, text='1',variable=newWindow,value = 1)
        V1.pack()
        V1.invoke()
        V2 = tk.Radiobutton(newWindow, text='2',variable=newWindow,value = 2)
        V2.pack()

        V3 = tk.Radiobutton(newWindow, text='3',variable=newWindow,value = 3)
        V3.pack()

        V4 = tk.Radiobutton(newWindow, text='4',variable=newWindow,value = 4)
        V4.pack()

        V5 = tk.Radiobutton(newWindow, text='5', variable=newWindow, value=5)
        V5.pack()

        V6 = tk.Radiobutton(newWindow, text='6', variable=newWindow, value=6)
        V6.pack()

        V7 = tk.Radiobutton(newWindow, text='7', variable=newWindow, value=7)
        V7.pack()

        show = tk.Button(newWindow, text='show')
        show.pack()


def cam_mode(stop, c):
    timecnt = 1
    Vname = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    width = int(c.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(c.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    writer = cv2.VideoWriter(Vname+'.avi', fourcc, 30.0, (width, height))
    print('preview start')
    cv2.namedWindow('preview', cv2.WINDOW_NORMAL)

    while stop():
        ret, img = c.read()

        cv2.imshow('preview', img)
        writer.write(img)
        #cv2.waitKey(1)
        if cv2.waitKey(1)&0xff==27:
            break
    print('preview stop')


class Main:
    def __init__(self):
        self.app = Application(master=tk.Tk())
        self.flag = True
        self.cam = None
        self.cnt = 0

    def mode_change(self):
        mode = self.app.mode.get()
        print('call', mode)
        cv2.destroyAllWindows()
        if mode == 1:
            print('preview mode')
            self.flag = True
            cam_th = threading.Thread(target=cam_mode, args=(lambda: self.flag, self.cam))
            cam_th.start()
        elif mode == 2:
            self.flag = False
            self.app.createNewWindow()




    def run(self):
        self.cam = cv2.VideoCapture(0)
        self.app.mode_c['command'] = self.mode_change
        self.app.mode_p['command'] = self.mode_change

        cam_th = threading.Thread(target=cam_mode, args=(lambda: self.flag, self.cam))
        cam_th.start()
        self.app.mainloop()


def main():
    m = Main()
    m.run()


main()



