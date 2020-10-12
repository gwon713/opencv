import tkinter as tk
from functools import partial
import threading
import check.face_widgets as f
import check.Student_Member as mem

def remove_ent(app):
    app.ent.delete(0, 'end')
    app.ent2.delete(0, 'end')
    app.ent3.delete(0, 'end')
    app.ent4.delete(0, 'end')

def make_id(g,c,n):
    if len(c) < 2:
        c = '0'+c
    if len(n) < 2:
        n = '0'+n
    eid = g+c+n
    print(type(id))
    return eid

def btn1_clicked(app, service, event):
    print(event)
    grade = app.ent.get()
    Class = app.ent2.get()
    num = app.ent3.get()
    name = app.ent4.get()
    id = make_id(grade,Class,num)
    s = mem.StudentMember(id, name)
    # h = service.select(id)
    # if h != None:
    #     print('중복된 학번!!! 다시 입력해주세요')
    # else:
    #     service.insert(s)
    #     print('입력성공')
    print(id)
    remove_ent(app)
    print('sub_btn1 clicked: video_show threading')
    v = f.video_service(app)
    Vth(app,v,id)

def Vth(app,v,id):
    threading.Thread(target=app.destroy()).start()
    threading.Thread(target=v.video_show(id)).start()


def make(app, service):
    newWindow = tk.Toplevel(app)
    newWindow.lab = tk.Label(newWindow, font=30, text='=== 학생 정보 입력 ===')
    newWindow.lab2 = tk.Label(newWindow, font=30, text='학년 : ')
    newWindow.lab3 = tk.Label(newWindow, font=30, text='반 : ')
    newWindow.lab4 = tk.Label(newWindow, font=30, text='번호 : ')
    newWindow.lab5 = tk.Label(newWindow, font=30, text='이름 : ')
    newWindow.ent = tk.Entry(newWindow, width=15)
    newWindow.ent2 = tk.Entry(newWindow, width=15)
    newWindow.ent3 = tk.Entry(newWindow, width=15)
    newWindow.ent4 = tk.Entry(newWindow, width=15)
    newWindow.btn1 = tk.Button(newWindow, width=10, font=60, text='저장')

    newWindow.lab.grid(row=0, column=0,columnspan=2)
    newWindow.lab2.grid(row=1, column=0)
    newWindow.lab3.grid(row=2, column=0)
    newWindow.lab4.grid(row=3, column=0)
    newWindow.lab5.grid(row=4, column=0)
    newWindow.ent.grid(row=1, column=1)
    newWindow.ent2.grid(row=2, column=1)
    newWindow.ent3.grid(row=3, column=1)
    newWindow.ent4.grid(row=4, column=1)
    newWindow.btn1.grid(row=5, column=1)


    newWindow.btn1.bind('<Button-1>', partial(btn1_clicked, newWindow, service))
