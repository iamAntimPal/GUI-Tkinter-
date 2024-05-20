#Horizontal ScrollBar
from tkinter import*
win=Tk()
win.title("ScrollBar")
win.geometry("800x200")

#Scroll Bar
scrollbar=Scrollbar(win,orient="horizontal")
scrollbar.pack(side=BOTTOM,fill=X)

t=Text(win,wrap=NONE,insertbackground="red",
       xscrollcommand=scrollbar.set)
t.pack(fill=BOTH)

scrollbar.config(command=t.xview)
win.mainloop()
