#Entry widget
from tkinter import*
win=Tk()
win.geometry('850x400')
win.title('Addition')

def total():
    r=int(Fst.get())+int(Snd.get())+int(trd.get())+int(frt.get())+int(fvt.get())
    sxt.set(r)

def average():
    r=int(Fst.get())+int(Snd.get())+int(trd.get())+int(frt.get())+int(fvt.get())
    snt.set(r/5)

def grade():
    a=int(Fst.get())+int(Snd.get())+int(trd.get())+int(frt.get())+int(fvt.get())
    #snt.set()
    a/=5
    if a<50:
        ett.set('F')
    if a>=50 and a<60:
        ett.set('D')
    if a>=60 and a<70:
        ett.set('C')
    if a>=70 and a<80:
        ett.set('B')
    if a>=80 and a<90:
        ett.set('A')
    if a>=90:
        ett.set('A+')

Fst=StringVar()
Snd=StringVar()
trd=StringVar()
frt=StringVar()
fvt=StringVar()
sxt=StringVar()
snt=StringVar()
ett=StringVar()

L1=Label(win,text='Enter 1st Number: ')
L1.grid()
E1=Entry(win,justify="center",textvariable=Fst)
E1.grid(row=0,column=1)

L2=Label(win,text='Enter 2nd Number: ')
L2.grid()
E2=Entry(win,justify="center",textvariable=Snd)
E2.grid(row=1,column=1)

L3=Label(win,text='Enter 3rd Number: ')
L3.grid()
E3=Entry(win,justify="center",textvariable=trd)
E3.grid(row=2,column=1)

L4=Label(win,text='Enter 4th Number: ')
L4.grid()
E4=Entry(win,justify="center",textvariable=frt)
E4.grid(row=3,column=1)

L5=Label(win,text='Enter 5th Number: ')
L5.grid()
E5=Entry(win,justify="center",textvariable=fvt)
E5.grid(row=4,column=1)

L6=Label(win,text='Total marks: ')
L6.grid()
E6=Entry(win,justify="center",textvariable=sxt,state="readonly")
E6.grid(row=5,column=1)

L7=Label(win,text='Average marks: ')
L7.grid()
E7=Entry(win,justify="center",textvariable=snt,state="readonly")
E7.grid(row=6,column=1)

L8=Label(win,text='Grades: ')
L8.grid()
E8=Entry(win,justify="center",textvariable=ett,state="readonly")
E8.grid(row=7,column=1)

B1=Button(win,text='Total',padx=50,pady=2,command=total)
B1.grid(row=8,column=1,pady=5)


B2=Button(win,text='Average',padx=10,pady=2,command=average)
B2.grid(row=8,column=2,pady=5)

B3=Button(win,text='Grade',padx=10,pady=2,command=grade)
B3.grid(row=8,column=3,pady=5)

win.mainloop()




