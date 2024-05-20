from tkinter import*
win=Tk()
win.title("Menu_Widget")
win.maxsize(1100,600)
win.minsize(900,400)

# m=Menu(win)
# m.add_command(label="File")
# m.add_command(label="Exit",command=quit)
# win.config(menu=m)
def close():
    win.destroy()

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
m1.add_command(label="Exit",command=close)
win.config(menu=menubar)
menubar.add_cascade(label="File",menu=m1)

win.mainloop()






