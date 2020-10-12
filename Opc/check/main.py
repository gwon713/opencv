import tkinter as tk
import check.main_ui as win
import check.make_widgets as mkw
import check.Student_Member as s

def main():
    root = tk.Tk()
    app = win.AppWindow(root, '300x200+100+100')
    dao = s.StudentMemberDao()
    mkw.make(app,dao)
    app.mainloop()