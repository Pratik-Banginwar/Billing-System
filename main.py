from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Billing Software")
        
        # ================Variables=================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.c_email=StringVar()
        self.bill_no=StringVar()
        z=random.randint(10000,99999)
        self.bill_no.set(z)
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        
        # Product Categories list
        self.Category=["Select Option","Clothing","LifeStyle","Mobile"]
        
        self.SubCatClothing=["Pant","Tshirt","Shirt"]
        self.pant=["Levis","Denim","Spykar"]
        self.price_Levis=1999
        self.price_Denim=1599
        self.price_Spykar=999
        
        self.T_shirt=["RoadStar","Jack&Jons","Peter-England"]
        self.price_RoadStar=800
        self.price_JackJons=1200
        self.price_PeterEngland=1000
        
        self.Shirt=["Polo","Louis","Park Avenue"]
        self.price_polo=1999
        self.price_Louis=1599
        self.price_Park=999
        
        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        self.Bath_soap=["Lifeboy","Lux","Santoor","Pear"]
        self.price_Lifeboy=float(20)
        self.price_Lux=48
        self.price_Santoor=53
        self.price_Pear=61
        
        self.Face_cream=["Fair&lovely","Ponds","Garnier","Olay"]
        self.price_Fairlovely=20
        self.price_Ponds=33
        self.price_Garnier=57
        self.price_Olay=16
        
        self.Hair_oils=["Bajaj","Parashoot","Nihar","Navratna"]
        self.price_Bajaj=80
        self.price_Parashoot=54
        self.price_Nihar=37
        self.price_Navratna=63
        
        self.SubCatMobile=["Iphone","Samsung","OnePlus","Redmi"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12","Iphone_13"]
        self.price_ix=57099
        self.price_i11=60499
        self.price_i12=70000
        self.price_i13=96000
        
        self.Samsung=["Samsung_16","Samsung_21","Samsung_12","Samsung_36"]
        self.price_s16=20000
        self.price_s21=24999
        self.price_s12=28999
        self.price_s36=36000
        
        self.OnePlus=["OnePlus_1","OnePlus_2","OnePlus_3"]
        self.price_o1=29000
        self.price_o2=32999
        self.price_o3=34000
        
        self.Redmi=["Redmi_11","Redmi_8","Redmi_7"]
        self.price_r11=22500
        self.price_r8=18999
        self.price_r7=16000
        
        
        # Img-1
        img=Image.open("./image/cart.jpg")
        img=img.resize((455,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=455,height=130)
        
        # Img-2
        img_1=Image.open("image/fruit.jpg")
        img_1=img_1.resize((455,130),Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=455,y=0,width=455,height=130)
        
        # Img-3
        img_2=Image.open("image/flower.jpg")
        img_2=img_2.resize((455,130),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=910,y=0,width=455,height=130)
        
        
        
        # Now We make label
        lbl_title=Label(self.root,text="Pratik Banginwar Mart Billing Software",font=("time new roman",32,"bold"),bg="aqua",fg="red")
        lbl_title.place(x=0,y=130,width=1366,height=50)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(lbl_title,font=("time new roman",16,"bold"),bg="aqua",fg="black")
        lbl.place(x=5,y=0,width=120,height=50)
        time()
        
        # Frame
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=180,width=1366,height=588)
        
        # Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("time new roman",13,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=320,height=140)
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile No:",font=("time new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("time new roman",12,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1)
        
        self.lblCustName=Label(Cust_Frame,text="Cust Name:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("time new roman",12,"bold"),width=20)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblEmail=Label(Cust_Frame,text="Email:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("time new roman",12,"bold"),width=20)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        
        
        # Product LabelFrame
        Prod_Frame=LabelFrame(Main_Frame,text="Product",font=("time new roman",13,"bold"),bg="white",fg="red")
        Prod_Frame.place(x=340,y=5,width=560,height=140)
        
            # Category drtail
        self.lblCategory=Label(Prod_Frame,text="Categories:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.Combo_Category=ttk.Combobox(Prod_Frame,value=self.Category,font=("time new roman",10,"bold"),width=20,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
            # SubCategory
        self.lblSubCategory=Label(Prod_Frame,text="Subcategory:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.ComboSubCategory=ttk.Combobox(Prod_Frame,value=[""],font=("time new roman",10,"bold"),width=20,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
            # Product
        self.lblProduct=Label(Prod_Frame,text="Product:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.ComboProduct=ttk.Combobox(Prod_Frame,textvariable=self.product,font=("time new roman",10,"bold"),width=20,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
           # Price
        self.lblPrice=Label(Prod_Frame,text="Price:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        self.ComboPrice=ttk.Combobox(Prod_Frame,textvariable=self.prices,font=("time new roman",10,"bold"),width=20,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
           # Qty
        self.lblQty=Label(Prod_Frame,text="Qty:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.ComboQty=ttk.Entry(Prod_Frame,textvariable=self.qty,font=("time new roman",10,"bold"),width=22)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        
        
        # middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=888,height=300)
        
        # Img-1
        img12=Image.open("./image/cloths.jpg")
        img12=img12.resize((444,300),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=-10,y=-10,width=454,height=280)
        
         # Img-2
        img13=Image.open("./image/shop.jpg")
        img13=img13.resize((444,300),Image.Resampling.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=444,y=-10,width=444,height=280)
        
        
        
        # search bill  txt_Entry_Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=910,y=0,width=400,height=50)

        self.lblBill=Label(Search_Frame,text="Bill No:",font=("time new roman",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=5, pady=10)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("time new roman",12,"bold"),width=18)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5, pady=10)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("time new roman",10,"bold"),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2,padx=10, pady=10)
        

        
        
        # Right side bill area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("time new roman",13,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=910,y=45,width=440,height=350)
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("time new roman",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        
        
        # Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("time new roman",13,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=395,width=1355,height=120)
        
        self.lblSubTotal=Label(Bottom_Frame,text="SubTotal:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.EntySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("time new roman",10,"bold"),width=24)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lbl_tax=Label(Bottom_Frame,text="GOV_Tax:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("time new roman",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblAmountTotal=Label(Bottom_Frame,text="Total:",font=("time new roman",12,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("time new roman",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("time new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)
        
        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("time new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)
        
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("time new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=("time new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("time new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=("time new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        
        self.l=[]
    
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome to Pratik Banginwar Mart")
        self.textarea.insert(END,f"\n Bill No: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Mobile No: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email: {self.c_email.get()}")
        
        self.textarea.insert(END,"\n===================================================")
        self.textarea.insert(END,f"\n Product\t\t\tQty\t\t\tPrice")
        self.textarea.insert(END,"\n===================================================\n")
        
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)
 
        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Mobile":
            self.ComboSubCategory.config(value=self.SubCatMobile)
            self.ComboSubCategory.current(0)
    
    def Product_add(self,event=""):
        # "Pant","Tshirt","Shirt"
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Tshirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)
        
        # "Bath Soap","Face Cream","Hair Oil"
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Face Cream":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oils)
            self.ComboProduct.current(0)
            
        # "Iphone","Samsung","OnePlus","Redmi"
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="OnePlus":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Redmi":
            self.ComboProduct.config(value=self.Redmi)
            self.ComboProduct.current(0)
            
    def price(self,event=""):
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Denim":
            self.ComboPrice.config(value=self.price_Denim)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_Spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="RoadStar":
            self.ComboPrice.config(value=self.price_RoadStar)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Jack&Jons":
            self.ComboPrice.config(value=self.price_JackJons)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Peter-England":
            self.ComboPrice.config(value=self.price_PeterEngland)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Louis":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Lifeboy":
            self.ComboPrice.config(value=self.price_Lifeboy)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_Lux)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Pear":
            self.ComboPrice.config(value=self.price_Pear)
            self.ComboPrice.current(0)
            self.qty.set(1) 
            
        if self.ComboProduct.get()=="Fair&lovely":
            self.ComboPrice.config(value=self.price_Fairlovely)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_Ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_Garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_Olay)
            self.ComboPrice.current(0)
            self.qty.set(1)   
        # Bajaj","Parashoot","Nihar","Navratna"  
        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_Bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Parashoot":
            self.ComboPrice.config(value=self.price_Parashoot)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Nihar":
            self.ComboPrice.config(value=self.price_Nihar)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Navratna":
            self.ComboPrice.config(value=self.price_Navratna)
            self.ComboPrice.current(0)
            self.qty.set(1)
            # Iphone_X","Iphone_11","Iphone_12","Iphone_13" 
        if self.ComboProduct.get()=="Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Iphone_13":
            self.ComboPrice.config(value=self.price_i13)
            self.ComboPrice.current(0)
            self.qty.set(1)
            # "Samsung_16","Samsung_21","Samsung_12","Samsung_36"
        if self.ComboProduct.get()=="Samsung_16":
            self.ComboPrice.config(value=self.price_s16)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Samsung_21":
            self.ComboPrice.config(value=self.price_s21)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Samsung_12":
            self.ComboPrice.config(value=self.price_s12)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Samsung_36":
            self.ComboPrice.config(value=self.price_s36)
            self.ComboPrice.current(0)
            self.qty.set(1)
            # OnePlus_1","OnePlus_2","OnePlus_3
        if self.ComboProduct.get()=="OnePlus_1":
            self.ComboPrice.config(value=self.price_o1)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="OnePlus_2":
            self.ComboPrice.config(value=self.price_o2)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="OnePlus_3":
            self.ComboPrice.config(value=self.price_o3)
            self.ComboPrice.current(0)
            self.qty.set(1)
            # Redmi_11","Redmi_8","Redmi_7
        if self.ComboProduct.get()=="Redmi_11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Redmi_8":
            self.ComboPrice.config(value=self.price_r8)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Redmi_7":
            self.ComboPrice.config(value=self.price_r7)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
    # ==========================Function Declaration===============================
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()==" ":
            messagebox.showerror("Error","Plz select the product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Plz Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n===================================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("Saved_Bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill Num:{self.bill_no.get()} saved successfully")
            f1.close()
            
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
    
    def find_bill(self):
        found="no"
        for i in os.listdir("Saved_Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Saved_Bills/{i}",'r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No")
    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        # self.bill_no=set("")
        x=random.randint(10000,99999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
        
    
    
    
    
if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()