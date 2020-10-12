import tkinter as tk
import cv2
import os
from PIL import Image
from PIL import ImageTk

class AppWindow(tk.Frame):#frame
    def __init__(self, master=None, size=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#opencv frame
        self.sub_fr = None#frame
        self.create_widgets()
        self.src = None #tk의 label에 출력할 영상
        self.frame = None #tk의 영상을 출력할 레이블

    def create_widgets(self):
        self.frame = tk.Label(self.master)
        self.frame.pack()
        self.sub_fr = tk.Frame(self.master)#frame
        self.sub_fr.pack()

    def cam_mode(self):
        pass

