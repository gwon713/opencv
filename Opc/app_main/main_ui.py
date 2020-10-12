import tkinter as tk
import cv2
import os
from PIL import Image
from PIL import ImageTk

class AppWindow(tk.Frame):#frame
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#opencv frame
        self.sub_fr = None#frame
        self.src = None #tk의 label에 출력할 영상
        self.frame = None #tk의 영상을 출력할 레이블
        self.create_widgets(path)
        self.imgdir = 'img/'
        self.img=None
        self.cnt=0
        self.imgdirs = os.listdir(self.imgdir)
        self.size = len(self.imgdirs)

    def make_img(self, path):
        src = cv2.imread(path)
        src = cv2.resize(src, (650,650))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)

    def create_widgets(self, path):
        self.make_img(path)
        self.frame = tk.Label(self.master, image=self.src)
        self.frame.pack()
        self.sub_fr = tk.Frame(self.master)#frame
        self.sub_fr.pack()

    def change_img(self, res):
        res = cv2.resize(res, (650,650))
        img = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)
        self.frame['image']=self.src

    def next_img(self):
        print('next')
        print('img/' + self.imgdirs[self.cnt % self.size])
        self.cnt += 1
        file = 'img/' + self.imgdirs[self.cnt % self.size]
        res = cv2.imread(filename=file)
        self.change_img(res)
        return file

    def prev_img(self):
        print('prev')
        print('img/' + self.imgdirs[self.cnt % self.size])
        self.cnt -= 1
        file = 'img/' + self.imgdirs[self.cnt % self.size]
        res = cv2.imread(filename=file)
        self.change_img(res)
        return file
