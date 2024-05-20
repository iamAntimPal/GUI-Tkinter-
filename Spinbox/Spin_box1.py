from tkinter import*
win=Tk()
win.geometry('900x400+250+200')

lst=['ANURAG','ANTIM','RAGHAV']

s=Spinbox(win,values=lst,justify=CENTER,font='arial 50',width=12)
s.pack()

win.mainloop()