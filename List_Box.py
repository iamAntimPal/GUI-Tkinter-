from tkinter import*
root_window=Tk()
root_window.geometry('800x300')

scr=Scrollbar(root_window)
scr.pack(side=RIGHT,fill=Y)

lsb=Listbox(root_window,width=40,yscrollcommand=scr.set)
for msg in range(1,100001):
    lsb.insert(END,msg)

lsb.pack()
scr.config(command=lsb.yview)


root_window.mainloop()


