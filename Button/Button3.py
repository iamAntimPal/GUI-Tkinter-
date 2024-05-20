from tkinter import*
root_window=Tk()
root_window.geometry('800x500')
root_window['bg']='teal'

def color_change():
    import File_3
    
        
b=Button(root_window,text='New Window',font="algerian 20",padx=30,command=color_change)
b.place(x=250,y=150)

b1=Button(root_window,text='Exit Window',font="algerian 20",padx=30,command=exit)
b1.place(x=250,y=250)

root_window.mainloop()
