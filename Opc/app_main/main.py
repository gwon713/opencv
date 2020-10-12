import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s
import app_main.Face_Detect_Service as fds

def main():
    img_path = 'img/1.jpg'
    root = tk.Tk()
    fd_service = fds.FaceDetectService(img_path)
    app = win.AppWindow(root, '750x750+100+100', img_path)
    mkw.make(app, fd_service)
    s.service() #ui 이벤트와 상관없이 수행해야하는 기능
    app.mainloop()
