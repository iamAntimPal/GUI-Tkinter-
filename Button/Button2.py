from tkinter import*
root_window=Tk()
root_window.geometry('800x500')
root_window['bg']='teal'

def color_change():
    root_window.destroy()
    import Frame
    
    
b=Button(root_window,text='New Window',font="algerian 20",padx=30,command=color_change)
b.place(x=250,y=200)

root_window.mainloop()
