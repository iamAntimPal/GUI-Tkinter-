#Radio Button
from tkinter import*
win=Tk()
win.title("RooT_Window")
win.geometry("200x200")
win.minsize(350,100)
win.maxsize(350,100)
def sel():
    r=var.get()
    if r==1:
        print("Selected Male")
    if r==2:
        print("Selected Female")
    if r==3:
        print("Selected other")
    
var=IntVar()

r1=Radiobutton(win,text='Male',variable=var,value=1,command=sel)
r1.pack(anchor=SW)

r2=Radiobutton(win,text='Female',variable=var,value=2,command=sel)
r2.pack(anchor=SW)

r3=Radiobutton(win,text='other',variable=var,value=3,command=sel)
r3.pack(anchor=SW)

win.mainloop()
