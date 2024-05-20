from tkinter import*
win=Tk()
win.geometry('800x400')
f=Frame(win,height=100,width=400,bg='skyblue')
f.pack(fill=X)

lbl=Label(f,text='Antim',cursor='spider')
lbl.place(x=10,y=20)

win.mainloop()