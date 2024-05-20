#Radio Button
from tkinter import*
win=Tk()
win.title("RooT_Window")
win.geometry("1200x400")
win.minsize(1200,400)
win.maxsize(1200,400)
def sel():
    select="You Selected the Value "+str(var.get())
    label.config(text=select)
    
var=IntVar()

r1=Radiobutton(win,text='Male',variable=var,value=1,command=sel)
r1.pack(anchor=SW)

r2=Radiobutton(win,text='Female',variable=var,value=2,command=sel)
r2.pack(anchor=SW)

r3=Radiobutton(win,text='other',variable=var,value=3,command=sel)
r3.pack(anchor=SW)

label=Label(win)
label.pack()
win.mainloop()
