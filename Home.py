from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from Employee import Emp
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass
from sales import SalesClass
import os
import time
import sqlite3
class Home():
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1530x800+0+0")
        self.root.config(bg="white")

        #title
        img=Image.open("images/cart.png")
        img=img.resize((300,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lb_img=Label(self.root,image=self.photoimg)
        lb_img.place(x=0,y=0,width=300,height=130)
        title=Label(self.root,text="Inventory Management System",compound=LEFT,font=("times new roman",40,"bold"),bg="red",fg="white",anchor="w",padx=20).place(x=300,y=0,relwidth=1,height=130)
        #Button
        btn_logout=Button(self.root, text="Logout",command=self.log, font=("times new roman",15, "bold"), bg="yellow",height="2",width="12").place(x=1150,y=10)
        #clock
        self.clock_lb=Label(self.root,text="Welcome To Inventory Management System\t\t Date:DD-MM-YYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.clock_lb.place(x=0,y=120,relwidth=1,height=30)
        #Left Menu
        self.img1=Image.open("images/menu_im.png")
        self.img1=self.img1.resize((200,200),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(self.img1)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=150,width=200,height=565)
        menuLogo=Label(LeftMenu,image=self.img1)
        menuLogo.pack(side=TOP,fill=X)
        self.img2=Image.open("images/side.png")
        self.img2=self.img2.resize((20,20),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(self.img2)
        lb_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_emp=Button(LeftMenu,text="Employee",command=self.Employee,image=self.img2,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",padx=20).pack(side=TOP,fill=X)
        btn_sup=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.img2,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",padx=20).pack(side=TOP,fill=X)
        btn_cat=Button(LeftMenu,text="Category",command=self.category,image=self.img2,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",padx=20).pack(side=TOP,fill=X)
        btn_prod=Button(LeftMenu,text="Product",command=self.product,image=self.img2,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",padx=20).pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.img2,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",padx=20).pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=root.quit,image=self.img2,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",padx=20).pack(side=TOP,fill=X)
        #content
        self.emp_lb=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,font=("times new roman",20,"bold"),bg="#33bbf9",fg="white")        
        self.emp_lb.place(x=300,y=160,width=300,height=150)
        self.sup_lb=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,font=("times new roman",20,"bold"),bg="#ff5722",fg="white")        
        self.sup_lb.place(x=650,y=160,width=300,height=150)
        self.cat_lb=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,font=("times new roman",20,"bold"),bg="#009688",fg="white")        
        self.cat_lb.place(x=1000,y=160,width=300,height=150)
        self.prod_lb=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,font=("times new roman",20,"bold"),bg="#607d8b",fg="white")        
        self.prod_lb.place(x=300,y=350,width=300,height=150)
        self.sales_lb=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,font=("times new roman",20,"bold"),bg="#ffc107",fg="white")        
        self.sales_lb.place(x=650,y=350,width=300,height=150)
        #footer
        self.clock_lb1=Label(self.root,text=" IMS-Inventory Management System|Developed By Shubham and Mitesh",font=("times new roman",20),bg="#4d636d",fg="white")
        self.clock_lb1.pack(side=BOTTOM,fill=X)
        self.update()
    def Employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Emp(self.new_win)
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)
    
    def log(self):
        self.root.destroy()
        os.system("python Login.py")

    def update(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             cur.execute("select*from employee")
             employee=cur.fetchall()
             self.emp_lb.config(text=f'Total Employee\n[{str(len(employee))}]')

             cur.execute("select*from supplier")
             supplier=cur.fetchall()
             self.sup_lb.config(text=f'Total Supplier\n[{str(len(supplier))}]')

             cur.execute("select*from category")
             category=cur.fetchall()
             self.cat_lb.config(text=f'Total Category\n[{str(len(category))}]')

             cur.execute("select*from product")
             product=cur.fetchall()
             self.prod_lb.config(text=f'Total Product\n[{str(len(product))}]')

             self.sales_lb.config(text=f"Total Sales\n[{str(len(os.listdir('bill')))}]")

             '''cur.execute("select*from sales")
             sales=cur.fetchall()
             self.sales_lb.config(text=f'Total Sales\n[{str(len(sales))}]')'''

             time_=time.strftime("%I:%M:%S");
             date_=time.strftime("%d-%m-%y");
             self.clock_lb.config(text=f"IMS-Inventory Management System|Developed By Shubham and Mitesh\t\t Date:{str(date_)}\t\tTime:{str(time_)}");
             self.clock_lb.after(200,self.update)


         except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")

if __name__=="__main__":
    root=Tk()
    obj=Home(root)
    root.mainloop()
    

        
        
