# To Apply Canvas
from tkinter import*
root_window=Tk()
root_window.geometry('800x500')
root_window['bg']='black'
c=Canvas(root_window,height=350,width=400,bg='white')
c.create_rectangle(50,50,200,200,width=6,outline='red')
c.pack(pady=100)

# Canvas(root_window,height=350,width=400,bg='white').pack(pady=100)

root_window.mainloop()
