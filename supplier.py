from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
class SupplierClass():
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()
        #All Variables
        
        self.suplier_id_invoice=StringVar()
        self.name=StringVar()
        self.contact=StringVar()
       
        
      
    
        #btn_search=Button(command=self.search,text="Search",font=("times new roman",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        #title
        title=Label(self.root,text="Supplier Details",bg="#0f4d7d",font=("times new roman",25),fg="white").place(x=50,y=10,width=1000,height=40)
        #==content==
        #row1
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",bg="white",font=("times new roman",15)).place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable= self.suplier_id_invoice,bg="white",font=("times new roman",15)).place(x=180,y=80,width=180)
        #txt_gender=Entry(self.root,textvariable=self.gender,bg="white",font=("times new roman",15)).place(x=500,y=150)
        
        #row2
        name=Label(self.root,text="Name",bg="white",font=("times new roman",15)).place(x=50,y=120)
        txt_name=Entry(self.root,textvariable= self.name,bg="white",font=("times new roman",15)).place(x=180,y=120,width=180)
        
        

        #row3
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("times new roman",15)).place(x=50,y=160)
        txt_conctact=Entry(self.root,textvariable= self.contact,bg="white",font=("times new roman",15)).place(x=180,y=160,width=180)
        
        #txt_utype=Entry(self.root,textvariable=self.utype,bg="white",font=("times new roman",15)).place(x=850,y=230,width=180)
        
        #row4
        lbl_desc=Label(self.root,text="Description",bg="white",font=("times new roman",15)).place(x=50,y=200)
        self.txt_desc=Text(self.root,bg="white",font=("times new roman",15))
        self.txt_desc.place(x=180,y=200,width=470,height=90)
        
        #Buttons
        B1= Button(self.root,command=self.add, text="Insert",bg="#2196f3",height=3,width=13)
        B1.place(x=180,y=320,width=110,height=35)
        B2= Button(self.root,command=self.update, text="Update",bg="#4caf50",height=3,width=13)
        B2.place(x=300,y=320,width=110,height=35)
        B3= Button(self.root,command=self.delete, text="Delete",bg="#f44336",height=3,width=13)
        B3.place(x=420,y=320,width=110,height=35)
        B4= Button(self.root,command=self.clear,text="Clear",bg="#607d8b",height=3,width=13)
        B4.place(x=540,y=320,width=110,height=35)
        # btn_search=Button(self.root,command=self.search,text="Search",font=("times new roman",15),bg="#4caf50",fg="white").place(x=980,y=305,width=110,height=28)
        
        #Employee Details
        Emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        Emp_frame.place(x=650,y=60,width=420,height=300)
        
        scrolly=Scrollbar(Emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(Emp_frame,orient=HORIZONTAL)
        
        self.supplierTable=ttk.Treeview(Emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Desc")
        
        self.supplierTable["show"]="headings"


        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
       
        self.show()
        

    def show(self):
         conn1=sqlite3.connect('ims.db')
         c1=conn1.cursor()
         try:
             c1.execute("""SELECT * FROM supplier""")
             rows=c1.fetchall()
             self.supplierTable.delete(*self.supplierTable.get_children())
             for row in rows:
                 self.supplierTable.insert('',END,values=row)
         except Exception as e:
             print(e) 

        
    def search(self):
        conn1=sqlite3.connect('ims.db')
        c1=conn1.cursor()
        try:
            sql="SELECT * FROM supplier where name=? or contact=? or invoice=? or desc=?"
            c1.execute(sql,(self.name.get(),self.contact.get(),self.suplier_id_invoice.get(),self.utype.get()))
            rows=c1.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
            if rows:
                messagebox.showinfo("Title","Record Found")
            else:
                messagebox.showerror("Title","Record Not Found")
            
                
        except Exception as e:
            print(e) 

    def clear(self):  
        self.suplier_id_invoice.set(""),
        self.name.set(""),
        self.contact.set(""),
        self.txt_desc.delete('1.0',END),
      
    
    def get_data(self,event=""):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        try:
             self.suplier_id_invoice.set(row[0]),
             self.name.set(row[1]),
             self.contact.set(row[2]),
             self.txt_desc.delete('1.0',END),
             self.txt_desc.insert(END,row[3]),
        except Exception as e:
            print(e)
    
    
    def delete(self):
       value_del=(self.suplier_id_invoice.get())
       print(value_del)
       conn=sqlite3.connect('ims.db')
       c2=conn.cursor()
       sql="DELETE FROM supplier WHERE invoice=?"
       c2.execute(sql,(value_del,))
       c2.execute("""SELECT * FROM supplier""")
       list123 = c2.fetchall()
       conn.commit()
       messagebox.showinfo("Title","Record is deleted")
       self.show()
    
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.suplier_id_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. Must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.suplier_id_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no. ",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                        self.name.get(),
                        self.contact.get(),
                        self.txt_desc.get('1.0',END),
                        self.suplier_id_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Succesfully Updated",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")
    


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.suplier_id_invoice.get()=="":
                messagebox.showerror("Error","Invoice Must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.suplier_id_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no. is already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                        self.suplier_id_invoice.get(),
                        self.name.get(),
                        self.contact.get(),
                        self.txt_desc.get('1.0',END),
                       
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Succesfully ",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")

if __name__=="__main__":
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()

