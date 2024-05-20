from tkinter import*
win=Tk()
win.geometry('900x400+250+200')

def value_get():
    h=ab.get()
    print(h)
    print(type(h))


# Hold data
ab=StringVar()

lbl=Label(win,text='Enter 1st Number ',font="arial 20")
lbl.place(x=40,y=40)
e1=Entry(win,bg='teal',font="arial 20",fg='white',selectbackground="yellow",selectforeground='grey',show='*',textvariable=ab)
e1.place(x=300,y=40)

b=Button(win,text='Get Value',font="arial 20",command=value_get).place(x=100,y=150)
win.mainloop()