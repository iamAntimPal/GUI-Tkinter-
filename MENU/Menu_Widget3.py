from tkinter import*
import tkinter.messagebox as msg 
win=Tk()
win.title("Menu_Widget")
win.maxsize(1100,600)
win.minsize(900,400)

# m=Menu(win)
# m.add_command(label="File")
# m.add_command(label="Exit",command=quit)
# win.config(menu=m)

menubar=Menu(win)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="New",)
m1.add_command(label="New Window",)
m1.add_command(label="Open...",)
m1.add_command(label="Save",)
m1.add_command(label="Save As...",)
m1.add_separator()
m1.add_command(label="Page Setup...",)
m1.add_command(label="Print",)
m1.add_separator()
m1.add_command(label="Exit",command=quit)
win.config(menu=menubar)
menubar.add_cascade(label="File",menu=m1)

def active():
    #msg.showinfo("Help_Menu","What type of help")
    pass

def show():
    s=msg.askquestion("Ask Question","Do you like gui or not")
    if s=='yes':
        y="Great you like gui"
    else:
        y="why do you not like gui"
    msg.showinfo("Feedback",y)
    
    
h1=Menu(menubar,tearoff=0)
h1.add_command(label="Help",command=active)
h1.add_command(label="Like",command=show)
menubar.add_cascade(label="Help",menu=h1)
win.config(menu=menubar)

win.mainloop()
