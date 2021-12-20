from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
class Emp():
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()
        #All Variables
        self.emp_id=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.name=StringVar()
        self.dob=StringVar()
        self.doj=StringVar()
        self.email=StringVar()
        self.var_pass=StringVar()
        self.utype=StringVar()
        self.address=StringVar()
        self.salary=StringVar()
        
      
    
        #btn_search=Button(command=self.search,text="Search",font=("times new roman",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        #title
        title=Label(self.root,text="Employee Details",bg="#0f4d7d",font=("times new roman",15),fg="white").place(x=50,y=100,width=1000)
        #==content==
        #row1
        empid=Label(self.root,text="Emp ID",bg="white",font=("times new roman",15)).place(x=50,y=150)
        gender=Label(self.root,text="Gender",bg="white",font=("times new roman",15)).place(x=370,y=150)
        contact=Label(self.root,text="Contact",bg="white",font=("times new roman",15)).place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable= self.emp_id,bg="white",font=("times new roman",15)).place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.gender,bg="white",font=("times new roman",15)).place(x=500,y=150)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.contact,bg="white",font=("times new roman",15)).place(x=850,y=150,width=180)
        #row2
        name=Label(self.root,text="Name",bg="white",font=("times new roman",15)).place(x=50,y=190)
        txt_name=Entry(self.root,textvariable= self.name,bg="white",font=("times new roman",15)).place(x=150,y=190,width=180)
        dob=Label(self.root,text="D.O.B",bg="white",font=("times new roman",15)).place(x=370,y=190)
        txt_dob=Entry(self.root,textvariable=self.dob,bg="white",font=("times new roman",15)).place(x=500,y=190,width=180)
        doj=Label(self.root,text="D.O.J",bg="white",font=("times new roman",15)).place(x=750,y=190)
        txt_doj=Entry(self.root,textvariable=self.doj,bg="white",font=("times new roman",15)).place(x=850,y=190,width=180)

        #row3
        email=Label(self.root,text="Email",bg="white",font=("times new roman",15)).place(x=50,y=230)
        txt_email=Entry(self.root,textvariable= self.email,bg="white",font=("times new roman",15)).place(x=150,y=230,width=180)
        var_pass=Label(self.root,text="Password",bg="white",font=("times new roman",15)).place(x=370,y=230)
        txt_var_pass=Entry(self.root,textvariable=self.var_pass,bg="white",font=("times new roman",15)).place(x=500,y=230,width=180)
        utype=Label(self.root,text="User Type",bg="white",font=("times new roman",15)).place(x=750,y=230)
        #txt_utype=Entry(self.root,textvariable=self.utype,bg="white",font=("times new roman",15)).place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #row4
        address=Label(self.root,text="Address",bg="white",font=("times new roman",15)).place(x=50,y=270)
        self.txt_address=Text(self.root,bg="white",font=("times new roman",15))
        self.txt_address.place(x=150,y=270,width=300,height=60)
        salary=Label(self.root,text="Salary",bg="white",font=("times new roman",15)).place(x=500,y=270)
        salary=Entry(self.root,textvariable=self.salary,bg="white",font=("times new roman",15)).place(x=600,y=270,width=180)
        #Buttons
        B1= Button(self.root,command=self.add, text="Insert",bg="#2196f3",height=3,width=13)
        B1.place(x=500,y=305,width=110,height=28)
        B2= Button(self.root,command=self.update, text="Update",bg="#4caf50",height=3,width=13)
        B2.place(x=620,y=305,width=110,height=28)
        B3= Button(self.root,command=self.delete, text="Delete",bg="#f44336",height=3,width=13)
        B3.place(x=740,y=305,width=110,height=28)
        B4= Button(self.root,command=self.clear,text="Clear",bg="#607d8b",height=3,width=13)
        B4.place(x=860,y=305,width=110,height=28)
        btn_search=Button(self.root,command=self.search,text="Search",font=("times new roman",15),bg="#4caf50",fg="white").place(x=980,y=305,width=110,height=28)
        #Employee Details
        Emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        Emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(Emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(Emp_frame,orient=HORIZONTAL)
        self.EmployeeTable=ttk.Treeview(Emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"


        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

    def show(self):
         conn1=sqlite3.connect('ims.db')
         c1=conn1.cursor()
         try:
             c1.execute("""SELECT * FROM employee""")
             rows=c1.fetchall()
             self.EmployeeTable.delete(*self.EmployeeTable.get_children())
             for row in rows:
                 self.EmployeeTable.insert('',END,values=row)
         except Exception as e:
             print(e) 

        
    def search(self):
        conn1=sqlite3.connect('ims.db')
        c1=conn1.cursor()
        try:
            sql="SELECT * FROM employee where name=? or contact=? or eid=? or utype=?"
            c1.execute(sql,(self.name.get(),self.contact.get(),self.emp_id.get(),self.utype.get()))
            rows=c1.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
            if rows:
                messagebox.showinfo("Title","Record Found")
            else:
                messagebox.showerror("Title","Record Not Found")
            
                
        except Exception as e:
            print(e) 

    def clear(self):  
        self.emp_id.set(""),
        self.name.set(""),
        self.email.set(""),
        self.gender.set(""),
        self.contact.set(""),
        self.dob.set(""),
        self.doj.set(""),
        self.var_pass.set(""),
        self.utype.set(""),
        self.txt_address.delete('1.0',END),
        self.salary.set("") 
    def get_data(self,event=""):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        try:
             self.emp_id.set(row[0]),
             self.name.set(row[1]),
             self.email.set(row[2]),
             self.gender.set(row[3]),
             self.contact.set(row[4]),
             self.dob.set(row[5]),
             self.doj.set(row[6]),
             self.var_pass.set(row[7]),
             self.utype.set(row[8]),
             self.txt_address.delete('1.0',END),
             self.txt_address.insert(END,row[9]),
             self.salary.set(row[10]) 
            
        except Exception as e:
            print(e)
    def delete(self):
       value_del=(self.emp_id.get())
       print(value_del)
       conn=sqlite3.connect('ims.db')
       c2=conn.cursor()
       sql="DELETE FROM employee WHERE eid=?"
       c2.execute(sql,(value_del,))
       c2.execute("""SELECT * FROM employee""")
       list123 = c2.fetchall()
       conn.commit()
       messagebox.showinfo("Title","Record is deleted")
       self.show()
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select*from employee where eid=?",(self.emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID ",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                        self.name.get(),
                        self.email.get(),
                       self.gender.get(),
                       self.contact.get(),
                       self.dob.get(),
                       self.doj.get(),
                       self.var_pass.get(),
                       self.utype.get(),
                       self.txt_address.get('1.0',END),
                       self.salary.get(), 
                       self.emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Succesfully Updated",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select*from employee where eid=?",(self.emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID is already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                       self.emp_id.get(),
                        self.name.get(),
                        self.email.get(),
                       self.gender.get(),
                       self.contact.get(),
                       self.dob.get(),
                       self.doj.get(),
                       self.var_pass.get(),
                       self.utype.get(),
                       self.txt_address.get('1.0',END),
                       self.salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Succesfully Saved",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")

if __name__=="__main__":
    root=Tk()
    obj=Emp(root)
    root.mainloop()
3    
