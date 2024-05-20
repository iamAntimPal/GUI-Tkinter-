from tkinter import*
win=Tk()
win.geometry('900x400+250+200')

def show():
    print(r.get())

r=StringVar()

s=Spinbox(win,from_=1,to=15,font='arial 40',width=8,justify=CENTER,textvariable=r,command=show)
s.pack()

win.mainloop()