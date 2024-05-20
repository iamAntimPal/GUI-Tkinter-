from tkinter import*
win=Tk()
win.geometry('900x400+250+200')
def show():
    print(c.get())

c=IntVar()

c1=Checkbutton(win,text='English',variable=c,command=show)
c1.place(x=0,y=0)

c2=Checkbutton(win,text='Hindi')
c2.place(x=0,y=20)

c3=Checkbutton(win,text='Mathematics')
c3.place(x=0,y=40)

c4=Checkbutton(win,text='Zology')
c4.place(x=0,y=60)

b=Button(win,text='Get Value',font="arial 20").place(x=100,y=150)
win.mainloop()