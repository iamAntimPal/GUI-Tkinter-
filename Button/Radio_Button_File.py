from tkinter import*
win=Tk()
win.geometry('900x400+250+200')

def show():
    print(r.get())
    
r=IntVar()

c1=Radiobutton(win,text='English',variable=r,value=1,command=show)
c1.place(x=0,y=0)

c2=Radiobutton(win,text='Hindi',variable=r,value=2,command=show)
c2.place(x=0,y=20)

c3=Radiobutton(win,text='Mathematics',variable=r,value=3,command=show)
c3.place(x=0,y=40)

c4=Radiobutton(win,text='Zology',variable=r,value=4,command=show)
c4.place(x=0,y=60)

b=Button(win,text='Get Value',font="arial 20").place(x=100,y=150)
win.mainloop()