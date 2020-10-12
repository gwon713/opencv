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
        self.fname = ''
        self.create_widgets()

    def create_widgets(self):
        self.mode_c = tk.Radiobutton(self, text='촬영모드', variable=self.mode, value=1)
        self.mode_c.pack()
        self.mode_c.invoke()  # 라디오 버튼 디폴트 체크

        self.mode_p = tk.Radiobutton(self, text='보기모드', variable=self.mode, value=2)
        self.mode_p.pack()

        self.btn1 = tk.Button(self, width=20, font=40, text='칼라모드촬영')
        self.btn1.pack()

        self.btn2 = tk.Button(self, width=20, font=40, text='흑백모드촬영')
        self.btn2.pack()

        self.btn3 = tk.Button(self, width=20, font=40, text='이전사진')
        self.btn3.pack()

        self.btn4 = tk.Button(self, width=20, font=40, text='다음사진')
        self.btn4.pack()

        self.btn5 = tk.Button(self, width=20, font=40, text='삭제')
        self.btn5.pack()

        self.file_l = tk.Label(self, width=20, font=40, text='파일명:')
        self.file_l.pack()
        self.file_e = tk.Entry(self, width=30)
        self.file_e.pack()


def cam_mode(stop, c):
    print('preview start')
    cv2.namedWindow('preview', cv2.WINDOW_NORMAL)
    while stop():
        ret, img = c.read()
        cv2.imshow('preview', img)
        cv2.waitKey(1)
    print('preview stop')


class Main:
    def __init__(self):
        self.app = Application(master=tk.Tk())
        self.flag = True
        self.cam = None
        self.cnt = 0

    def write_color(self):
        fname = self.app.file_e.get()
        if fname == '':
            messagebox.showerror("error", "input file name")
            return

        self.flag = False
        ret, img = self.cam.read()
        cv2.imshow('capture', img)
        cv2.imwrite('img/' + fname, img)
        self.app.file_e.delete(0, 'end')
        self.app.fname = 'img/' + fname

    def write_gray(self):

        fname = self.app.file_e.get()
        if fname == '':
            messagebox.showerror("error", "input file name")
            return

        self.flag = False
        ret, img = self.cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('capture', gray)
        cv2.imwrite('img/' + fname, gray)
        self.app.file_e.delete(0, 'end')
        self.app.fname = 'img/' + fname

    def view_prev(self):
        img_list = os.listdir('img')
        if self.cnt == 0:
            self.cnt = len(img_list) - 1
        else:
            self.cnt -= 1

        img = cv2.imread('img/' + img_list[self.cnt])
        cv2.imshow('capture', img)
        self.app.fname = 'img/' + img_list[self.cnt]

    def view_next(self):
        img_list = os.listdir('img')
        if self.cnt == len(img_list) - 1:
            self.cnt = 0
        else:
            self.cnt += 1

        img = cv2.imread('img/' + img_list[self.cnt])
        cv2.imshow('capture', img)
        self.app.fname = 'img/' + img_list[self.cnt]

    def del_pic(self):
        os.remove(self.app.fname)

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
            print('picture mode')
            self.flag = False
            img_list = os.listdir('img')
            img = cv2.imread('img/' + img_list[0])
            cv2.imshow('capture', img)

    def run(self):
        self.cam = cv2.VideoCapture(0)
        self.app.btn1['command'] = self.write_color
        self.app.btn2['command'] = self.write_gray
        self.app.btn3['command'] = self.view_prev
        self.app.btn4['command'] = self.view_next
        self.app.btn5['command'] = self.del_pic

        self.app.mode_c['command'] = self.mode_change
        self.app.mode_p['command'] = self.mode_change

        cam_th = threading.Thread(target=cam_mode, args=(lambda: self.flag, self.cam))
        cam_th.start()
        self.app.mainloop()


def main():
    m = Main()
    m.run()


main()



