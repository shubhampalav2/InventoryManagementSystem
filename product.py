from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
class ProductClass():
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System |  Product Page")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # -- ALL Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
      

        # -- Product Frame 

        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)
        
        #title
        title=Label(product_frame,text="Manage Product Details",bg="#0f4d7d",font=("times new roman",18),fg="white").pack(side=TOP,fill=X)
        # --  Column 1 -- 
        lbl_category=Label(product_frame,text="Category",bg="white",font=("times new roman",18),).place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Supplier",bg="white",font=("times new roman",18),).place(x=30,y=110)
        lbl_product_name=Label(product_frame,text="Name",bg="white",font=("times new roman",18),).place(x=30,y=160)
        lbl_price=Label(product_frame,text="Price",bg="white",font=("times new roman",18),).place(x=30,y=210)
        lbl_quantity=Label(product_frame,text="Quantity",bg="white",font=("times new roman",18),).place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status",bg="white",font=("times new roman",18),).place(x=30,y=310)
  
        
        # --  Column 2 -- 

        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        # --  Column 3 -- 

        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)
         # --  Column 4 -- 

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("times new roman",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("times new roman",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("times new roman",15),bg='lightyellow').place(x=150,y=260,width=200)

        
         # --  Column 5 -- 
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        # --  Buttons  -- 
        B1_add= Button(product_frame,command=self.add, text="Insert",bg="#2196f3",height=3,width=13)
        B1_add.place(x=10,y=400,width=100,height=40)
        B2_update= Button(product_frame,command=self.update, text="Update",bg="#4caf50",height=3,width=13)
        B2_update.place(x=120,y=400,width=100,height=40)
        B3_delete= Button(product_frame,command=self.delete, text="Delete",bg="#f44336",height=3,width=13)
        B3_delete.place(x=230,y=400,width=100,height=40)
        B4_clear= Button(product_frame,command=self.clear,text="Clear",bg="#607d8b",height=3,width=13)
        B4_clear.place(x=340,y=400,width=100,height=40)
       
        

        # -- Search Frame  ---- 
        
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)
        
        # -- Options 
        # --  Column 5 -- 
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("select","category","supplier","Name"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=700,y=39,width=220,height=35)
        btn_search=Button(self.root,command=self.search,text="Search",font=("times new roman",15),bg="#4caf50",fg="white").place(x=950,y=39,width=120,height=35)

        # ---  Products Details
        product_frame=Frame(root,bd=3,relief=RIDGE)
        product_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollx=Scrollbar(product_frame,orient=HORIZONTAL)
        
        self.producTable=ttk.Treeview(product_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.producTable.xview)
        scrolly.config(command=self.producTable.yview)
        self.producTable.heading("pid",text="P ID")
        self.producTable.heading("Category",text="Category")
        self.producTable.heading("Supplier",text="Supplier")
        self.producTable.heading("name",text="Name")
        self.producTable.heading("price",text="Price")
        self.producTable.heading("qty",text="Qty")
        self.producTable.heading("status",text="Status")
        
        self.producTable["show"]="headings"


        self.producTable.column("pid",width=90)
        self.producTable.column("Category",width=100)
        self.producTable.column("Supplier",width=100)
        self.producTable.column("name",width=100)
        self.producTable.column("price",width=100)
        self.producTable.column("qty",width=100)
        self.producTable.column("status",width=100)
        
        self.producTable.pack(fill=BOTH,expand=1)
        self.producTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        




 #   --- Functions ---

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()   
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            

            cur.execute("select name from supplier")
            sup=cur.fetchall()   
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or  self.var_sup.get()=="Select" or self.var_sup.get()=="Empty":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product Already present , try different",parent=self.root)
                else:
                    cur.execute("Insert into product (Supplier,Category,name,price,qty,status) values(?,?,?,?,?,?)",(
                       self.var_cat.get(),
                       self.var_sup.get(),
                       self.var_name.get(),
                       self.var_price.get(),
                       self.var_qty.get(),
                       self.var_status.get(),
                       
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Saved",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)





    def show(self):
         conn1=sqlite3.connect('ims.db')
         c1=conn1.cursor()
         try:
             c1.execute("""SELECT * FROM product""")
             rows=c1.fetchall()
             self.producTable.delete(*self.producTable.get_children())
             for row in rows:
                 self.producTable.insert('',END,values=row)
         except Exception as e:
             messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

        
    # def search(self):
    #     conn1=sqlite3.connect('ims.db')
    #     c1=conn1.cursor()
    #     try:
    #         sql="SELECT * FROM product where name=? or contact=? or eid=? or utype=?"
    #         c1.execute(sql,(self.name.get(),self.contact.get(),self.emp_id.get(),self.utype.get()))
    #         rows=c1.fetchall()
    #         self.producTable.delete(*self.producTable.get_children())
    #         for row in rows:
    #             self.producTable.insert('',END,values=row)
    #         if rows:
    #             messagebox.showinfo("Title","Record Found")
    #         else:
    #             messagebox.showerror("Title","Record Not Found")
            
                
    #     except Exception as e:
    #         print(e) 

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Please Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
                            
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.producTable.delete(*self.producTable.get_children())
                    for row in rows:
                        self.producTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error"," No record found!!!",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root) 


    def clear(self):
        self.var_pid.set(""),
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        
        self.var_searchtxt.set(""),
        self.var_searchby.set("Select"),
        self.show()
    
    def get_data(self,event=""):
        f=self.producTable.focus()
        content=(self.producTable.item(f))
        row=content['values']
        try:
            self.var_pid.set(row[0])
            self.var_sup.set(row[1])
            self.var_cat.set(row[2])
            self.var_name.set(row[3])
            self.var_price.set(row[4])
            self.var_qty.set(row[5])
            self.var_status.set(row[6])
        except Exception as e:
            print(e)

    # def delete(self):
    #    value_del=(self.emp_id.get())
    #    print(value_del)
    #    conn=sqlite3.connect('ims.db')
    #    c2=conn.cursor()
    #    sql="DELETE FROM employee WHERE eid=?"
    #    c2.execute(sql,(value_del,))
    #    c2.execute("""SELECT * FROM employee""")
    #    list123 = c2.fetchall()
    #    conn.commit()
    #    messagebox.showinfo("Title","Record is deleted")
    #    self.show()

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product from the list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Conform","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM product WHERE pid=?",(
                       self.var_pid.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root) 

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select product from list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID ",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get()
                       
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Succesfully ",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}")
   
   
    
      
        
if __name__=="__main__":
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()