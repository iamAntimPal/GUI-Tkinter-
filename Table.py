from tkinter import*

root_window=Tk()

lst=[('ID','NAME','ADDRESS','CONTACT NO.'),
     (1001,'Anurag','Naraina',7827516978),
     (1002,'Aditya','Janakpuri',8512354466),
     (1003,'Antim','Uttam Nagar',9812334422),
     (1004,'Nikhil','Moti Nagar',7711223344),
     (1005,'Tanya','Subhash Nagar',7546221144)]

rows=len(lst)
cols=len(lst[0])

for i in range(rows):
    for j in range(cols):
        t=Entry(root_window,width=20,fg='blue',font="arial 16 bold",justify='center')
        t.grid(row=i,column=j)
        t.insert(END,lst[i][j])

root_window.mainloop()


