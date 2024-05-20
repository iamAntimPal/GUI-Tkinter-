#Vertical scrollBar
from tkinter import*
win=Tk()
win.title("ScrollBar")
win.geometry("800x200")
#Scroll Bar
scrollbar=Scrollbar(win)
scrollbar.pack(side=RIGHT,fill=Y)

t=Text(win,yscrollcommand=scrollbar.set)
t.pack(fill=BOTH)

scrollbar.config(command=t.yview)
win.mainloop()
