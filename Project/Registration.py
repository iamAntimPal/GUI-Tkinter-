from tkinter import*
from tkinter import ttk



class registrarion:
     def __init__(self,root) :
          self.root=root
          self.root.title("Registration From")
          self.root.geometry("600x300")
          self.root.resizable(False,False)
          
          lbl_Heading=Label(self.root,text="Registration From",font="arial 20 bold")
          lbl_Heading.place(x=10,y=10)
          
          
          
          #==============Sub Heading=================
          
          
          lbl_sub_Heading=Label(self.root,text="Full name",font="arial 12 ")
          lbl_sub_Heading.place(x=10,y=50)
          
          lbl_sub_Heading1=Label(self.root,text="Email",font="arial 12 ")
          lbl_sub_Heading1.place(x=10,y=90)
          
          lbl_sub_Heading2=Label(self.root,text="Gender",font="arial 12 ")
          lbl_sub_Heading2.place(x=10,y=130)
          
          lbl_sub_Heading3=Label(self.root,text="Country",font="arial 12 ")
          lbl_sub_Heading3.place(x=10,y=170)
          
          lbl_sub_Heading4=Label(self.root,text="Programming",font="arial 12 ")
          lbl_sub_Heading4.place(x=10,y=210)
          
          
          
          #=============Entry======================
          
          name_entry1=Entry(self.root,width=70)
          name_entry1.place(x=100,y=50)
          
          Email_entry2=Entry(self.root,width=70)
          Email_entry2.place(x=100,y=90)
          
          Gender1=Radiobutton(self.root,text="Male",value=1)
          Gender1.place(x=100,y=130)
          
          Gender2=Radiobutton(self.root,text="Female",value=2)
          Gender2.place(x=160,y=130)
          
          #=============Combo Box=============
          
          Country_combo=ttk.Combobox(self.root,state="readonly",width=30,justify=CENTER,values=['India','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American',])
          Country_combo.place(x=100,y=170)
          Country_combo.set("Select your country")
          
          #==============Check Box===================
          
          pro_check=Checkbutton(self.root,text="Java")
          pro_check.place(x=130,y=210)
          
          pro_check=Checkbutton(self.root,text="python")
          pro_check.place(x=190,y=210)
          
          #===============Button============
          
          sumit_button=Button(self.root,text="Submit",bg="red")
          sumit_button.place(x=20,y=240)
     

          
          
          
          
          
if __name__=="__main__":
     root=Tk()
     obj=registrarion(root)
     root.mainloop()
