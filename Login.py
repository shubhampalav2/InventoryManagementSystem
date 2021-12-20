from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
import os
import email_pass
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        #====Images====
        self.phone=Image.open("images/phone.png")
        self.phone=self.phone.resize((328,480),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(self.phone)
        self.lb_phone=Label(self.root,image=self.photoimg,bd=0).place(x=200,y=90)
        #==All Variables==
        '''self.employee_id=StringVar()
        self.password=StringVar()'''
        #====Login Frame====
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=390,height=460)
        title=Label(login_frame,text="Login Page",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lb1_user=Label(login_frame, text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50, y=100)
        self.employee_id=Entry(login_frame,font=("times new roman",15),bg="#ECECEC")
        self.employee_id.place(x=50, y=140,width=250)

        lb2_pass=Label(login_frame, text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50, y=200)
        self.password=Entry(login_frame,show="*",textvariable="self.password",font=("times new roman",15),bg="#ECECEC")
        self.password.place(x=50, y=240,width=250)
        #button
        B1= Button(login_frame, text="Login",command=self.Login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",cursor="hand2",height=3,width=13)
        B1.place(x=50,y=300,width=250,height=35)

        h1=Label(login_frame,bg="lightgray").place(x=50,y=380,width=280,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=365)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget,font=("times new roman",15,"bold"),bg="white",fg="blue",bd=0).place(x=100,y=390)
        '''#===Sign Up Frame===
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=390,height=60)

        lb_reg=Label(register_frame,text="Don't have an account?",font=("times new roman",15),bg="white").place(x=24,y=20)
        btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",15,"bold"),bg="white",fg="blue",bd=0).place(x=200,y=17)'''
        #Animation Images
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lb1_change_image=Label(self.root,bg="white")
        self.lb1_change_image.place(x=320,y=164,width=180,height=350)
        self.Animate()


        
    def Animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lb1_change_image.config(image=self.im)
        self.lb1_change_image.after(2000,self.Animate)

    def Login(self):
         conn1=sqlite3.connect('ims.db')
         c1=conn1.cursor()
         try:
             if self.employee_id.get()=='' or self.password.get()=='':
                 messagebox.showerror('Error',"All fields are required",parent=self.root)
             else:
                 sql="SELECT utype FROM employee where eid=? and pass=?"
                 c1.execute(sql,(self.employee_id.get(),self.password.get()))
                 user=c1.fetchone()
                 if user==None:
                      messagebox.showerror('Error',"Invalid Employee ID|Password",parent=self.root)
                 else:
                     if user[0]=="Admin":
                      messagebox.showinfo('Success',"Logged as Admin",parent=self.root)
                      self.root.destroy()
                      os.system("python Home.py")
                     else:
                         messagebox.showinfo('Success',"Logged as Employee",parent=self.root)
                         self.root.destroy()
                         os.system("python billing.py")

         except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")

    def forget(self):
        conn1=sqlite3.connect('ims.db')
        c1=conn1.cursor()
        if self.employee_id.get()=="":
             messagebox.showerror('Error',"Employee ID must be required",parent=self.root)
        else:
            sql="SELECT email FROM employee where eid=?"
            c1.execute(sql,(self.employee_id.get(),))
            user=c1.fetchone()
            if user==None:
                messagebox.showerror('Error',"Invalid Employee ID Try Again",parent=self.root)
            else:
                self.var_otp=StringVar()
                '''self.var_pass=StringVar()
                self.var_confirm_pass=StringVar()'''
                #call send email function
                self.forget_win=Toplevel(self.root)
                self.forget_win.title('FORGET PASSWORD')
                self.forget_win.geometry('400x350+500+100')
                self.forget_win.focus_force()

                title=Label( self.forget_win,text="RESET Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                lb1_new=Label(self.forget_win, text="New Password",font=("times new roman",15)).place(x=20, y=140)
                self.var_pass=Entry(self.forget_win,show="*",font=("times new roman",15))
                self.var_pass.place(x=20,y=170)
                lb1_confirm=Label(self.forget_win, text="Confirm Password",font=("times new roman",15)).place(x=20, y=200)
                self.var_confirm_pass=Entry(self.forget_win,show="*",font=("times new roman",15))
                self.var_confirm_pass.place(x=20,y=240)
                btn_reset=Button(self.forget_win,text="Submit",command=self.update,font=("times new roman",15),bg="lightblue")
                btn_reset.place(x=20,y=280,width=250,height=30)

    def update(self):
        if(self.var_pass.get()=="" or self.var_confirm_pass.get()==""):
            messagebox.showerror('Error',"Password can't be empty")
        elif self.var_pass.get()!=self.var_confirm_pass.get():
            messagebox.showerror('Error',"New password and Confirm Password must be Same")
        else:
              conn1=sqlite3.connect('ims.db')
              c1=conn1.cursor()
              try:
                  c1.execute("Update employee set pass=? where eid=?",(self.var_pass.get(),self.employee_id.get()))
                  messagebox.showinfo('Success',"Password Updated")
                  conn1.commit()

              except Exception as e:
                   messagebox.showerror("Error",f"Error due to : {str(e)}")




if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()