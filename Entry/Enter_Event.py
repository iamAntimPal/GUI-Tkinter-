from tkinter import*
root_window=Tk()
root_window.geometry('800x400')
root_window['bg']='teal'

# ======================================================================

# Enter Even Function
def show_message1():
    s='IT IS A ENTER MOUSE EVENT'
    label.config(text=s,font='Arial 25',fg='white')

def show_message2(event):
    s='IT IS A ENTER MOUSE EVENT'
    label.config(text=s,font='Arial 25',fg='white')



# Reset Function
def reset_message1():
    s=' '
    label.config(text=s)

def reset_message2(event):
    s=' '
    label.config(text=s)

# ======================================================================

# Enter Button
event_button=Button(root_window,text='Enter',padx=60,font='Arial 20',command=show_message1)
event_button.bind('<Return>', show_message2)
event_button.place(x=150,y=200)

# Reset Button
reset_button=Button(root_window,text='Reset',padx=60,font='Arial 20',command=reset_message1)
reset_button.bind('<Return>', reset_message2)
reset_button.place(x=410,y=200)

# Label
label=Label(root_window,bg='teal')
label.place(x=150,y=80)


root_window.mainloop()
