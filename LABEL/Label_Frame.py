from tkinter import*
root_window=Tk()
root_window.geometry('800x500')
root_window['bg']='pink'

lf=LabelFrame(root_window,text='Details',height=200,width=400)
lf.pack()

lbl=Label(lf,text='InfoTech SoftNet')
lbl.place(x=20,y=60)

root_window.mainloop()

