from tkinter import *
win= Tk()
win.geometry("400x220")
#Set the Menu initially
menu=StringVar()

menu.set("Select Any Language")

#Create a ddown Menu
OptionMenu(win, menu,"C","C++", "JAVA","PYTHON","DATA SCIENCE","DJANGO",
                 "HTML","CSS","JAVASCRIPT").pack()
win.mainloop()
