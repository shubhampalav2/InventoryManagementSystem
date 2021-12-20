from os import stat
import os
from tkinter import *
from tkinter import ttk,StringVar
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
from typing import Sized
from PIL import Image,ImageTk
from Employee import Emp
import time
import sqlite3
import tempfile
# from supplier import SupplierClass
# from category import CategoryClass
# from product import ProductClass
# from sales import SalesClass

class BillClass():
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System  | By Shubham Palav and Mitesh Rege")
        self.root.geometry("1530x800+0+0")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0

        #title
        img=Image.open("images/cart.png")
        img=img.resize((300,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lb_img=Label(self.root,image=self.photoimg)
        lb_img.place(x=0,y=0,width=300,height=130)
        title=Label(self.root,text="Inventory Management System",compound=LEFT,font=("times new roman",40,"bold"),bg="red",fg="white",anchor="w",padx=20).place(x=300,y=0,relwidth=1,height=130)
        #Button
        btn_logout=Button(self.root, text="Logout",command=self.logout, font=("times new roman",15, "bold"), bg="yellow",height="2",width="12").place(x=1150,y=10)
        #clock
        self.clock_lb=Label(self.root,text="Welcome To Inventory Management System\t\t Date:DD-MM-YYY\t\tTime: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.clock_lb.place(x=0,y=120,relwidth=1,height=30)
        
        # -- Product Frame ----
           # -- Variables  ----
        self.var_search=StringVar()

        # --    ProductFrame 1 is Main Frame 
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=160,width=410,height=550)
        pTitle=Label(ProductFrame1,text="All Product",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        # --    ProductFrame 2 is Search Frame 
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)   
        lbl_name=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)   
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=128,y=48,width=150,height=22)  
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=284,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=284,y=10,width=100,height=25)

        


       # --    ProductFrame 3 is  Frame 

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=420,height=380)
        
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="qty")
        self.product_Table.heading("status",text="Status")
        
        self.product_Table["show"]="headings"


        self.product_Table.column("pid",width=90)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
        
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the Cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
       
        
        # -- Customer Frame ----
          # -- Variables ---

        self.var_C_name=StringVar()
        self.var_contact=StringVar()


        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=160,width=530,height=70)
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=35)   
        txt_name=Entry(CustomerFrame,textvariable=self.var_C_name,font=("times new roman",15,),bg="lightyellow").place(x=80,y=35,width=180) 

        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15,"bold"),bg="white").place(x=270,y=35)   
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",15,),bg="lightyellow").place(x=380,y=35,width=140)

        
        #   Calculator and Cart Frame  borh frae bolow in dtail:
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        #190
        Cal_Cart_Frame.place(x=420,y=240,width=530,height=360)
        # --      Cal Frame Begins

        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,'bold'),bg="lightyellow",width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text='7',font=("arial",15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=("arial",15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=("arial",15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=("arial",15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text='4',font=("arial",15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=("arial",15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=("arial",15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=("arial",15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text='1',font=("arial",15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=("arial",15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=("arial",15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=("arial",15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text='0',font=("arial",15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=("arial",15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=("arial",15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=("arial",15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)

        
         # --    Cart Frame Begins  

        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=306)
        self.cartTitle=Label(Cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        
        self.CartTable=ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="qty")
        
        self.CartTable["show"]="headings"


        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
        # -- Add Cart Wodgets Frame   ---
        self.var_pid=StringVar()
        self.var_P_name=StringVar()
        self.var_P_price=StringVar()
        self.var_P_qty=StringVar()
        self.var_P_status=StringVar()
        self.var_P_stock=StringVar()
        
        Add_CartWidgets_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgets_Frame.place(x=420,y=550,width=530,height=110)
        

        lbl_p_name=Label(Add_CartWidgets_Frame,text="Product Name",font=("goudy old style",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgets_Frame,textvariable=self.var_P_name,font=("goudy old style",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=180,height=22)
        
        lbl_p_price=Label(Add_CartWidgets_Frame,text="Price Per Qty",font=("goudy old style",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgets_Frame,textvariable=self.var_P_price,font=("goudy old style",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=130,height=22)

        lbl_p_qty=Label(Add_CartWidgets_Frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgets_Frame,textvariable=self.var_P_qty,font=("goudy old style",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_p_inStock=Label(Add_CartWidgets_Frame,text="In Stock [0]",font=("goudy old style",15),bg="white")
        self.lbl_p_inStock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_CartWidgets_Frame,text="Clear",command=self.clear_cart,font=("goudy old style",15),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        # btn_clear_cart=Button(Add_CartWidgets_Frame,text="Clear",font=("goudy old style",15),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgets_Frame,text="Add | Update Cart",command=self.add_update_cart,font=("goudy old style",15),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        

        # --  Billing Area ---
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=160,width=410,height=410)
        
        BTitle=Label(billFrame,text="Customer Bill Ara",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set) #,font=('goudy old')
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        
        scrolly.config(command=self.txt_bill_area.yview)


        # -----   Billings Buttons  ----
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=140)
        
        
        self.lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(billMenuFrame,text='Discount \n[5%]',font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text='Net Pay\n[0]',font=("goudy old style",15,"bold"),bg="#687d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)


        btn_print=Button(billMenuFrame,text='Print',command=self.print,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)
        
        btn_clear_all=Button(billMenuFrame,text='Clear All ',command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(billMenuFrame,text='Generate/Save Bill',command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

    # --  Footer ----

        footer=Label(self.root,text="IMS-Inventory System | Devloped By Mitesh and Shubham \n For any problem or Technical Issues Contact : 9082485137 or Mail on miteshrege@gmail.com  ",font=("times new roman",11,"bold"),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update()
        self.show()
        #self.bil_top()
# ================     All Functions ========== 
    def update(self):
         time_=time.strftime("%I:%M:%S");
         date_=time.strftime("%d-%m-%y");
         self.clock_lb.config(text=f"IMS-Inventory Management System\t\t Date:{str(date_)}\t\tTime:{str(time_)}")
         self.clock_lb.after(200,self.update)
    def get_input(self,num):
        num=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(num)

    def clear_cal(self):
        self.var_cal_input.set('')
    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    def show(self):
         conn1=sqlite3.connect('ims.db')
         c1=conn1.cursor()
         try:
             c1.execute("""SELECT pid,name,price,qty,status FROM product where status='Active'""")
             rows=c1.fetchall()
             self.product_Table.delete(*self.product_Table.get_children())
             for row in rows:
                 self.product_Table.insert('',END,values=row)
         except Exception as e:
             messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)
            
    def search(self):
        conn1=sqlite3.connect('ims.db')
        c1=conn1.cursor()
        try:
            sql="SELECT pid,name,price,qty,status FROM product where name=? and status='Active'"
            c1.execute(sql,(self.var_search.get(),))
            rows=c1.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
            if rows:
                messagebox.showinfo("Title","Record Found")
            else:
                messagebox.showerror("Title","Record Not Found")        
        except Exception as e:
             print(e) 

    def get_data(self,event=""):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        try:
            self.var_pid.set(row[0])
            self.var_P_name.set(row[1])
            self.var_P_price.set(row[2])
            self.var_P_qty.set(row[3])
            self.var_P_stock.set(row[4])
            self.lbl_p_inStock.config(text=f"In Stock [{str(row[3])}]")
            self.var_P_stock.set(row[3])
        except Exception as e:
            print(e)

    def get_data_cart(self,event=""):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        try:
            self.var_pid.set(row[0])
            self.var_P_name.set(row[1])
            self.var_P_price.set(row[2])
            self.var_P_qty.set(row[3])
            self.var_P_stock.set(row[4])
            self.lbl_p_inStock.config(text=f"In Stock [{str(row[4])}]")
        except Exception as e:
            print(e)

    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))

        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")



    
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error',"Please select product from the list",parent=self.root)
        elif self.var_P_qty.get()=='':
            messagebox.showerror('Error',"Quantity is Requierd",parent=self.root)
        elif int(self.var_P_qty.get())>int(self.var_P_stock.get()):
            messagebox.showerror('Error',"Invalid Quantity",parent=self.root)
        else:
            #price_cal=float(int(self.var_P_qty.get())*float(self.var_P_price.get()))
            price_cal=self.var_P_price.get()
            cart_data=[self.var_pid.get(), self.var_P_name.get(),price_cal,self.var_P_qty.get(),self.var_P_stock.get()]
            
            #====update_cart====
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
                print(present,index_)

            

            if(present=='yes'):
                op=messagebox.askyesno('Confirm',"Product already present\nDo you want to update|Remove from the cart List",parent=self.root)
                if op==True:
                    if self.var_P_qty.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_P_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def show_cart(self):
        try:
             self.CartTable.delete(*self.CartTable.get_children())
             for row in self.cart_list:
                 self.CartTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)
            

    def generate_bill(self):
        if self.var_C_name.get()==''or self.var_contact.get()=='':
                messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
             messagebox.showerror("Error",f"Please add products to the cart",parent=self.root)
        else:
            #===Bill_Top===
            self.bil_top()
            #===Bill_Middle===
            self.bill_middle()
            #==Bill_Bottom===
            self.bill_bottom()
            f=open(f'bill/{str(self.invoice)}.txt','w')
            f.write(self.txt_bill_area.get('1.0',END))
            f.close()
            messagebox.showinfo('Saved',"Bill has been generated|Save in Backend",parent=self.root)
            self.chk_print=1

    def bil_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
        \t\tDeepak-Inventory
        \t Phone No. 9082485137, Mumbai-400033
        {str("="*47)}
        Customer Name: {self.var_C_name.get()}
        Ph no. :{self.var_contact.get()}
        Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
        {str("="*47)}
        Product Name\t\t\tQTY\tPrice
        {str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
            bill_bottom_temp=f'''
            {str("="*47)}
            Bill Amount\t\t\t\tRs.{self.bill_amnt}
            Discount\t\t\t\tRs.{self.discount}
            Net Pay\t\t\t\tRs.{self.net_pay}
            {str("="*47)}\n
            '''
            self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        conn1=sqlite3.connect('ims.db')
        c1=conn1.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                # pid,name,price,qty,stock
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive';
                if int(row[3])!=int(row[4]):
                    status='Active';
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                #====Update quantity in product table====
                c1.execute("Update product set qty=?,status=? where pid=?",(
                    qty,
                    status,
                    pid

                 ))
                conn1.commit()
            conn1.close()
            self.show()
        except Exception as e:
              messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)



      



    def clear_cart(self):
          self.var_pid.set('')
          self.var_P_name.set('')
          self.var_P_price.set('')
          self.var_P_qty.set('')
          self.var_P_stock.set('')
          self.lbl_p_inStock.config(text=f"In Stock")
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_C_name.set('')
        self.var_contact.set('')
        self.var_search.set('')
        self.txt_bill_area.delete('1.0',END)
        self.clear_cart()
        self.show()
        self.show_cart()
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")

    def print(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            f2=tempfile.mktemp('.txt')
            open(f2,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(f2,'print')

        else:
            messagebox.showerror('Error',"Please generate bill,to print the receipt",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python Login.py")
           

if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()
    

