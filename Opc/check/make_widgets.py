import tkinter as tk
import check.manage as m

from functools import partial

def remove_ent(app):
    app.ent.delete(0, 'end')
    app.ent2.delete(0, 'end')

def btn1_clicked(app, service, event):
    print(event)
    id = app.ent.get()
    name = app.ent2.get()
    h = service.select(id)
    if h==None:
        print('없는 학번')
    elif name==h.name:
        print('출석을 해주세요')
        service.update(id)
    else:
        print('없는 이름')
    remove_ent(app)


def btn2_clicked(app, service, event):
    print(event)
    m.make(app,service)


def make(app, service):
    app.lab = tk.Label(app.sub_fr, font=30, text='학번 : ')
    app.lab2 = tk.Label(app.sub_fr, font=30, text='이름 : ')
    app.ent = tk.Entry(app.sub_fr, width=15)
    app.ent2 = tk.Entry(app.sub_fr, width=15)
    app.btn1 = tk.Button(app.sub_fr, width=10, font=30, text='출석')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=30, text='관리')

    app.lab.grid(row=0, column=0)
    app.ent.grid(row=0, column=1, columnspan=5)
    app.lab2.grid(row=2, column=0)
    app.ent2.grid(row=2, column=1, columnspan=5)
    app.btn1.grid(row=5, column=5)
    app.btn2.grid(row=6, column=5)

    app.btn1.bind('<Button-1>', partial(btn1_clicked, app, service))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app, service))
