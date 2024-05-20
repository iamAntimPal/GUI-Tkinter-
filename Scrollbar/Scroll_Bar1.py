#Vertical Scrollbar
from tkinter import*
win=Tk()
win.title("ScrollBar")
win.geometry("800x200")
#For connecting scrollbar to a widget
#1. widget(yscrollcommand=scrollbar.set)
#2. scrollbar.config(command=widget.yview)

scrollbar=Scrollbar(win)
scrollbar.pack(side=RIGHT,fill=Y)
lstbox=Listbox(win,width=20,justify='center',
               yscrollcommand=scrollbar.set)

for i in range(1,1001):
    lstbox.insert(END,f"Computer - {i}")

lstbox.pack()
scrollbar.config(command=lstbox.yview)
win.mainloop()
