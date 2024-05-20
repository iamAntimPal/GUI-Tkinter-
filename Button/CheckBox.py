from tkinter import*
win=Tk()
win.geometry("800x400")

F=Frame(win,highlightbackground="blue",highlightthickness=5)
F.pack(padx=20,pady=20)

C1=Checkbutton(F,text="Hindi",width=200,anchor="w")
C1.pack(padx=10,pady=10)

C2=Checkbutton(F,text="English",width=200,anchor="w")
C2.pack(padx=10,pady=10)

C3=Checkbutton(F,text="Bengali",width=200,anchor="w")
C3.pack(padx=10,pady=10)

C4=Checkbutton(F,text="Other",width=200,anchor="w")
C4.pack(padx=10,pady=10)

Button(F,text="BUTTON",font="Calibri 12 bold",
fg='#008080',padx=10,activeforeground='white',
activebackground='#9999FF').pack(padx=10,pady=10)

win.mainloop()
