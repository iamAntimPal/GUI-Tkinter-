from tkinter import*
import tkinter.messagebox as msg
win=Tk()
win.geometry('800x300')

def fun_1():
    msg.showinfo('Button_1','You Clicked Button_1')

def fun_2():
    v=msg.askquestion('Button_2','Do you Like GUI')
    print(v)
    if v=='yes':
        r=msg.showinfo('Msg','Great...😊')
    else:
        r=msg.showinfo('Msg','Why...😔')

def fun_3():
    a=msg.askokcancel('ok/cancel','Confirmation')
    if a==True:
        am=msg.showinfo('Message','You Press ok')
    else:
        am=msg.showinfo('Message','You Press cancel')

f=Frame(win,width=410,height=55,borderwidth=4,relief='groove').place(x=45,y=135)
b1=Button(f,text='Button_1',command=fun_1,padx='20').place(x=90,y=150)
b2=Button(f,text='Button_2',command=fun_2,padx='20').place(x=200,y=150)
b3=Button(f,text='Button_3',command=fun_3,padx='20').place(x=310,y=150)

win.mainloop()
