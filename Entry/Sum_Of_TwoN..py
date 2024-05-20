#Entry widget
from tkinter import*
win=Tk()
win.geometry('250x110')
win.title('Addition')
def Add():
    r=int(Fst.get())+int(Snd.get())
    Trd.set(r)
    
Fst=StringVar()
Snd=StringVar()
Trd=StringVar()

L1=Label(win,text='Enter 1st Number: ')
L1.grid()
E1=Entry(win,justify="center",textvariable=Fst)
E1.grid(row=0,column=1)

L2=Label(win,text='Enter 2nd Number: ')
L2.grid()
E2=Entry(win,justify="center",textvariable=Snd)
E2.grid(row=1,column=1)

L3=Label(win,text='Display Output: ')
L3.grid()
E3.grid(row=2,column=1)

B=Button(win,text='ADDITION',padx=50,pady=2,command=Add)
B.grid(row=3,columnspan=2,pady=5)
win.mainloop()




