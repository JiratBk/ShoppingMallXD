from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk #Treeview

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect("shoppingmallxd.db")  
    cursor = conn.cursor()
    
def mainwindow() :
    root = Tk()
    root.title("Welcome to Shopping Mall XD")
    w= 890
    h = 700
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.title("Shopping Mall XD")
    menubar = Menu(root)
    menubar.add_command(label="Exit",command = root.quit)
    root.option_add('*font','Garamond 16 bold')
    root.config(bg="pink",menu=menubar)
    root.resizable(False, False)  #ไม่อนุญาติให้ผู้ใช้ปรับขนาดหน้าจอได้
    root.rowconfigure([0,1,2],weight=1)
    root.columnconfigure([0,1,2],weight=1)
    return root

def loginlayout() :
    global loginframe,userentry,pwdentry,count,imagelist
    loginframe = Frame(root,bg="gray")
    root.title("Welcome to Shopping Mall XD")
    loginframe.rowconfigure([0,3],weight=1)
    loginframe.rowconfigure([1,2],weight=3)
    loginframe.columnconfigure([0,3],weight=1)
    loginframe.columnconfigure([1,2],weight=3)
    Label(loginframe,image=img_bg1).grid(rowspan=4,columnspan=4)
    logincenter = Frame(loginframe,bg="green")
    logincenter.rowconfigure([0,1,2,3,4,5],weight=1)
    logincenter.columnconfigure(0,weight=10)
    logincenter.columnconfigure([1,2],weight=1)
    Label(logincenter,bg="brown").grid(row=0,rowspan=6,column=0,sticky="news")
    Label(logincenter,bg="#FCA451").grid(row=0,rowspan=6,column=1,columnspan=2,sticky="news")
    
    Label(logincenter,image=logo_img,bg="brown").grid(row=0,rowspan=6,column=0,sticky="news")
    Label(logincenter,text="Username",bg="#FCA451",font="Tahoma 20 bold").grid(row=1,column=1,columnspan=2,sticky="sw")
    userentry = Entry(logincenter,bg='#e4fbff',width=30,textvariable=userinfo,font="Tahoma 16")
    userentry.grid(row=2,column=1,columnspan=2,sticky='w',padx=20)
    Label(logincenter,text="Password",bg="#FCA451",font="Tahoma 20 bold").grid(row=3,column=1,sticky="sw")
    pwdentry = Entry(logincenter,bg='#e4fbff',width=30,show='*',textvariable=pwdinfo,font="Tahoma 16")
    pwdentry.grid(row=4,column=1,columnspan=2,sticky='w',padx=20)
    Button(logincenter,text="Login",width=10,bg='#0AEAA3',font="Tahoma 16 bold",command=lambda:loginclick()).grid(row=5,column=1,pady=20,ipady=15)
    Button(logincenter,text="Register",width=10,bg='#7CBBFA',font="Tahoma 16 bold",command=regislayout).grid(row=5,column=2,pady=20,ipady=15)
    
    loginframe.grid(rowspan=3,columnspan=3,sticky="news")
    logincenter.grid(row=1,column=1,rowspan=2,columnspan=2,sticky="news")

def loginclick() :
    global user_result
    
    user = userinfo.get()
    pwd = pwdinfo.get()
    if user == "" :
        messagebox.showwarning("Admin:","Please enter Username")
        userentry.focus_force()
    else :
        sql = "select * from members where username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")  #แจ้งเตือนข้อความต่างๆ
                pwdentry.focus_force()
            else :
                sql = "select * from members where username=? and password=? "
                cursor.execute(sql,[user,pwd])   
                user_result = cursor.fetchone()
                if user_result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(user_result)
                    homepage()
                else :
                    messagebox.showwarning("Admin:","Incorrect Username or Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.select_range(0,END)
            userentry.focus_force()
            
def regislayout() :
    global regisframe,first_name,last_name,username,password,confirm_password
    loginframe.destroy()
    root.title("Welcome to Member Registration : ")
    root.config(bg='lightblue')
    regisframe = Frame(root,bg="gray")
    regisframe.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    regisframe.columnconfigure((0,1,2,3),weight=1)
    Label(regisframe,image=img_bg2).grid(row=0,rowspan=9,column=0,columnspan=4)
    Label(regisframe,bg="gray").grid(row=1,rowspan=6,column=1,columnspan=2,sticky="news")
    Label(regisframe,text="Member Registration Form",font="Garamond 26 bold",fg='#e4fbff',compound=LEFT,bg='#001F28').grid(row=0,columnspan=4,sticky='news',pady=10)

    Label(regisframe,text='First name : ',bg="gray",fg='#000000',font="Tahoma 16 bold").grid(row=1,column=1,sticky='e',padx=10)
    first_name = Entry(regisframe,width=20,bg='#d3e0ea',font="Tahoma 16 bold")
    first_name.grid(row=1,column=2,sticky='w',padx=10,pady=3)

    Label(regisframe,text='Last name : ',bg="gray",fg='#000000',font="Tahoma 16 bold").grid(row=2,column=1,sticky='e',padx=10)
    last_name = Entry(regisframe,width=20,bg='#d3e0ea',font="Tahoma 16 bold")
    last_name.grid(row=2,column=2,sticky='w',padx=10,pady=3)

    Label(regisframe,text='User name : ',bg="gray",fg='#000000',font="Tahoma 16 bold").grid(row=3,column=1,sticky='e',padx=10)
    username = Entry(regisframe,width=20,bg='#d3e0ea',font="Tahoma 16 bold")
    username.grid(row=3,column=2,sticky='w',padx=10,pady=3)

    Label(regisframe,text='Password : ',bg="gray",fg='#000000',font="Tahoma 16 bold").grid(row=4,column=1,sticky='e',padx=10)
    password = Entry(regisframe,width=20,bg='#d3e0ea',show="*",font="Tahoma 16 bold")
    password.grid(row=4,column=2,sticky='w',padx=10,pady=3)

    Label(regisframe,text='Confirm Password : ',bg="gray",fg='#000000',font="Tahoma 16 bold").grid(row=5,column=1,sticky='e',padx=10)
    confirm_password = Entry(regisframe,width=20,bg='#d3e0ea',show="*",font="Tahoma 16 bold")
    confirm_password.grid(row=5,column=2,sticky='w',padx=10,pady=3)

    
    regisaction = Button(regisframe,text="Cancel",font="Tahoma 16 bold",fg="#FFFFFF",bg="#680000",command=lambda:(regisframe.destroy(),loginlayout()))
    regisaction.grid(row=6,column=1,ipady=5,ipadx=5,padx=5,pady=5,sticky='w')
    first_name.focus_force()
    rebtn = Button(regisframe,text="Registration",bg='#000C65',font="Tahoma 16 bold",fg='#f6f5f5',command=registration)
    rebtn.grid(row=6,column=2,ipady=5,ipadx=5,pady=5,sticky='e',padx=10)
    regisframe.grid(rowspan=3,columnspan=3,sticky="news")
    
def registration() :
    print("Hello from registration")
    if first_name.get() == "" :
        messagebox.showwarning("Admin","Please enter First name")
        first_name.focus_force()
    elif last_name.get() == "" :
        messagebox.showwarning("Admin","Please enter Last name")
        last_name.focus_force()
    elif username.get() == "" :
        messagebox.showwarning("Admin","Please enter confirm User name")
        username.focus_force()
    elif password.get() == "" :
        messagebox.showwarning("Admin","Please enter Password")
        password.focus_force()
    elif confirm_password.get() == "" :
        messagebox.showwarning("Admin","Please enter Confirm Password")
        confirm_password.focus_force()
    elif password.get() != confirm_password.get() :
        messagebox.showwarning("Admin","Incorrect confirm password")
        password.focus_force()
    else:
        sql = "select * from members where username = ?"
        cursor.execute(sql, [username.get()])
        result = cursor.fetchall()
        if result:
            messagebox.showwarning("Admin","Username is already used") 
            username.select_range(0,END)
            username.focus_force()
        else:
            ins_sql = "INSERT INTO members VALUES(?,?,?,?,?)"
            param = [username.get(),password.get(),first_name.get(),last_name.get(),0]
            cursor.execute(ins_sql, param)
            conn.commit()
            messagebox.showinfo("Admin","Registration successfully")
            loginlayout()
            regisframe.destroy()

def homepage() :
    global logo,menuframe,bottom,lightdarkbtd,shoplist,welcometext,pointtext
    loginframe.destroy()
    updatepoint()
    menuframe = Frame(root,bg="#FDDF4B")
    menuframe.rowconfigure(0,weight=1)
    menuframe.rowconfigure(1,weight=1)
    menuframe.rowconfigure((2),weight=9)
    menuframe.columnconfigure((0,1),weight=1)
    welcometext = Label(menuframe,text=user_result[2]+" "+user_result[3],font="Tahoma 14 bold",bg="#FDDF4B")
    welcometext.grid(row=0,column=1,columnspan=2,padx=5)
    pointtext = Label(menuframe,text="Point : "+currentpoint,font="Tahoma 12 bold",bg="#FDDF4B")
    pointtext.grid(row=0,column=1,columnspan=2,padx=5,sticky="se")
    bottom = Label(menuframe,bg="red")
    bottom.grid(row=2,columnspan=2,sticky="news")
    
    logo = Label(menuframe,image=logo2_img,text="Shopping Mall XD",compound="left",bg="#FDDF4B",font="Tahoma 22 bold")
    logo.grid(row=0,columnspan=4,sticky="w")
    cartbtd = Button(menuframe,image=img_history,command=history)
    cartbtd.grid(row=1,columnspan=2,sticky="e",padx=5)
    
    lightdarkbtd = Button(menuframe,image=light,bd=0,activebackground="#FDDF4B",command=lightdarkmode,bg="#FDDF4B")
    promobtd = Button(menuframe,text="สินค้าโปรโมชั่น Click!",font="Tahoma 20 bold",command=promotion)
    Button(menuframe,text="Log out",font="Tahoma 12 bold",command=logout).grid(row=0,columnspan=2,sticky="e",padx=5)
    lightdarkbtd.grid(row=1,column=0,sticky="w",padx=10)
    promobtd.grid(row=1,columnspan=2)
    menuframe.grid(rowspan=3,columnspan=3,sticky="news")
        
    shoplist = Frame(menuframe,bg="white")
    shoplist.rowconfigure([0,1],weight=1)
    shoplist.columnconfigure([0,1,2],weight=1)

    if lightdark == True :
        shoplist.config(bg="white")
        menuframe.config(bg="#FDDF4B")
        logo.config(bg="#FDDF4B",fg="black")
        welcometext.config(bg="#FDDF4B",fg="black")
        pointtext.config(bg="#FDDF4B",fg="black")
        lightdarkbtd.config(image=light,bg="#FDDF4B",activebackground="#FDDF4B")
    else :
        shoplist.config(bg="#515151")
        menuframe.config(bg="#64367D")
        logo.config(bg="#64367D",fg="white")
        welcometext.config(bg="#64367D",fg="white")
        pointtext.config(bg="#64367D",fg="white")
        lightdarkbtd.config(image=dark,bg="#64367D",activebackground="#64367D")
        
    Button(shoplist,image=item1,bg='white',bd=0,command=menu1).grid(row=0,column=0)
    Button(shoplist,image=item2,bg='white',bd=0,command=menu2).grid(row=0,column=1)
    Button(shoplist,image=item3,bg='white',bd=0,command=menu3).grid(row=0,column=2)
    Button(shoplist,image=item4,bg='white',bd=0,command=menu4).grid(row=1,column=0)
    Button(shoplist,image=item5,bg='white',bd=0,command=menu5).grid(row=1,column=1)
    Button(shoplist,image=item6,bg='white',bd=0,command=menu6).grid(row=1,column=2)
    
    shoplist.grid(row=2,columnspan=2,sticky="news")

def promotion() :
    global framepromo
    framepromo = Frame(root,bg="#B04FFF",highlightthickness=10)
    framepromo.rowconfigure([0,1],weight=1)
    framepromo.columnconfigure([0,1,2],weight=1)
    Label(framepromo,text="สินค้าโปรโมชั่นสำหรับคุณ",bg="#B04FFF",font="Tahoma 20 bold",fg="white").grid(row=0,columnspan=3)
    Button(framepromo,image=promo1,bg="#B04FFF",fg='#000000',font="Garamond 20 bold",command=promotion1).grid(row=1,column=0)
    Button(framepromo,image=promo2,bg="#B04FFF",fg='#000000',font="Garamond 20 bold",compound=LEFT,command=promotion2).grid(row=1,column=1) 
    Button(framepromo,image=promo3,bg="#B04FFF",fg='#000000',font="Garamond 20 bold",compound=LEFT,command=promotion3).grid(row=1,column=2)
    Button(framepromo,image=returnbtd,bg="#B04FFF",fg='#000000',command=lambda:(framepromo.destroy())).grid(row=0,columnspan=3,sticky="e")
    framepromo.grid(row=0,column=0,rowspan=3,columnspan=3,sticky="we")
    
def menu1() :
    global framemenu1
    framemenu1 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    shoplist.destroy()
    framemenu1.rowconfigure((0,1,2,3,4),weight=1)
    framemenu1.columnconfigure((0,1,2,3),weight=1)
    framemenu1.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framemenu1,image=menu1_img1,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framemenu1,image=menu1_img2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btd1 = Button(framemenu1,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etn1)
    btd1.grid(row=1,column=2,padx=20)
    text1 = Label(framemenu1,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    text1.grid(row=1,column=1)
    Spinbox(framemenu1,from_=0,to=100,width=10,justify='center',textvariable=v1).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framemenu1,image=returnbtd,width=20,height=20,command=lambda:(framemenu1.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framemenu1.config(bg='#8ac4d0')
        text1.config(bg='#8ac4d0',fg='#000000')
        btd1.config(bg="#FFAB57",fg='#000000')
    else :
        framemenu1.config(bg='#4A4A4A')
        text1.config(bg='#4A4A4A',fg='#FFFFFF')
        btd1.config(bg="#643000",fg='#FFFFFF')
           
def etn1():
    global net1,data1
    total1 = Label(framemenu1,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=output1)
    total1.grid(row=2,column=1,columnspan=2,sticky="news")
    net1 = 0
    data1= int(v1.get())
    if v1.get() :
        net1 =165*data1
        output1.set("Total Price = %.2f Bahts"%net1)
    
    Button(framemenu1,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkout1).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        total1.config(bg='#8ac4d0',fg='#000000')
    else :
        total1.config(bg='#4A4A4A',fg='#FFFFFF')
        
def checkout1() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if net1 >= 300 :
        point = int(totalpoint) + 1
    if net1 >= 700 :
        point = int(totalpoint) + 2
    if net1 >= 1000 :
        point = int(totalpoint) + 3
    if net1 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"Crocs LiteRide Clog",data1,net1]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framemenu1.destroy()
        homepage()
        
def menu2() :
    global framemenu2
    framemenu2 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    shoplist.destroy()
    framemenu2.rowconfigure((0,1,2,3,4),weight=1)
    framemenu2.columnconfigure((0,1,2,3),weight=1)
    framemenu2.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framemenu2,image=menu2_img1,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framemenu2,image=menu2_img2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btd2 = Button(framemenu2,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etn2)
    btd2.grid(row=1,column=2,padx=20)
    text2 = Label(framemenu2,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    text2.grid(row=1,column=1)
    Spinbox(framemenu2,from_=0,to=100,width=10,justify='center',textvariable=v2).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framemenu2,image=returnbtd,width=20,height=20,command=lambda:(framemenu2.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framemenu2.config(bg='#8ac4d0')
        text2.config(bg='#8ac4d0',fg='#000000')
        btd2.config(bg="#FFAB57",fg='#000000')
    else :
        framemenu2.config(bg='#4A4A4A')
        text2.config(bg='#4A4A4A',fg='#FFFFFF')
        btd2.config(bg="#643000",fg='#FFFFFF')
           
def etn2():
    global net2,data2
    total2 = Label(framemenu2,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=output2)
    total2.grid(row=2,column=1,columnspan=2,sticky="news")
    net2 = 0
    data2= int(v2.get())
    if v2.get() :
        net2 =167*data2
        output2.set("Total Price = %.2f Bahts"%net2)
    
    Button(framemenu2,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkout2).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        total2.config(bg='#8ac4d0',fg='#000000')
    else :
        total2.config(bg='#4A4A4A',fg='#FFFFFF')
        
def checkout2() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if net2 >= 300 :
        point = int(totalpoint) + 1
    if net2 >= 700 :
        point = int(totalpoint) + 2
    if net2 >= 1000 :
        point = int(totalpoint) + 3
    if net2 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"ตุ๊กตาหมีหลายสีรุ้ง",data2,net2]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framemenu2.destroy()
        homepage()

def menu3() :
    global framemenu3
    framemenu3 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    shoplist.destroy()
    framemenu3.rowconfigure((0,1,2,3,4),weight=1)
    framemenu3.columnconfigure((0,1,2,3),weight=1)
    framemenu3.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framemenu3,image=menu3_img1,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framemenu3,image=menu3_img2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btd3 = Button(framemenu3,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etn3)
    btd3.grid(row=1,column=2,padx=20)
    text3 = Label(framemenu3,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    text3.grid(row=1,column=1)
    Spinbox(framemenu3,from_=0,to=100,width=10,justify='center',textvariable=v3).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framemenu3,image=returnbtd,width=20,height=20,command=lambda:(framemenu3.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framemenu3.config(bg='#8ac4d0')
        text3.config(bg='#8ac4d0',fg='#000000')
        btd3.config(bg="#FFAB57",fg='#000000')
    else :
        framemenu3.config(bg='#4A4A4A')
        text3.config(bg='#4A4A4A',fg='#FFFFFF')
        btd3.config(bg="#643000",fg='#FFFFFF')
           
def etn3():
    global net3,data3
    total3 = Label(framemenu3,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=output3)
    total3.grid(row=2,column=1,columnspan=2,sticky="news")
    net3 = 0
    data3= int(v3.get())
    if v3.get() :
        net3 =77*data3
        output3.set("Total Price = %.2f Bahts"%net3)
    
    Button(framemenu3,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkout3).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        total3.config(bg='#8ac4d0',fg='#000000')
    else :
        total3.config(bg='#4A4A4A',fg='#FFFFFF')
        
def checkout3() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if net3 >= 300 :
        point = int(totalpoint) + 1
    if net3 >= 700 :
        point = int(totalpoint) + 2
    if net3 >= 1000 :
        point = int(totalpoint) + 3
    if net3 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"รองเท้าใบไม้",data3,net3]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framemenu3.destroy()
        homepage()

def menu4() :
    global framemenu4
    framemenu4 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    shoplist.destroy()
    framemenu4.rowconfigure((0,1,2,3,4),weight=1)
    framemenu4.columnconfigure((0,1,2,3),weight=1)
    framemenu4.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framemenu4,image=menu4_img1,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framemenu4,image=menu4_img2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btd4 = Button(framemenu4,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etn4)
    btd4.grid(row=1,column=2,padx=20)
    text4 = Label(framemenu4,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    text4.grid(row=1,column=1)
    Spinbox(framemenu4,from_=0,to=100,width=10,justify='center',textvariable=v4).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framemenu4,image=returnbtd,width=20,height=20,command=lambda:(framemenu4.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framemenu4.config(bg='#8ac4d0')
        text4.config(bg='#8ac4d0',fg='#000000')
        btd4.config(bg="#FFAB57",fg='#000000')
    else :
        framemenu4.config(bg='#4A4A4A')
        text4.config(bg='#4A4A4A',fg='#FFFFFF')
        btd4.config(bg="#643000",fg='#FFFFFF')
           
def etn4():
    global net4,data4
    total4 = Label(framemenu4,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=output4)
    total4.grid(row=2,column=1,columnspan=2,sticky="news")
    net4 = 0
    data4= int(v4.get())
    if v4.get() :
        net4 =49*data4
        output4.set("Total Price = %.2f Bahts"%net4)
    
    Button(framemenu4,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkout4).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        total4.config(bg='#8ac4d0',fg='#000000')
    else :
        total4.config(bg='#4A4A4A',fg='#FFFFFF')
        
def checkout4() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if net4 >= 300 :
        point = int(totalpoint) + 1
    if net4 >= 700 :
        point = int(totalpoint) + 2
    if net4 >= 1000 :
        point = int(totalpoint) + 3
    if net4 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"LUODAIS น้ำหอมบำรุงผม",data4,net4]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framemenu4.destroy()
        homepage()

def menu5() :
    global framemenu5
    framemenu5 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    shoplist.destroy()
    framemenu5.rowconfigure((0,1,2,3,4),weight=1)
    framemenu5.columnconfigure((0,1,2,3),weight=1)
    framemenu5.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framemenu5,image=menu5_img1,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framemenu5,image=menu5_img2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btd5 = Button(framemenu5,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etn5)
    btd5.grid(row=1,column=2,padx=20)
    text5 = Label(framemenu5,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    text5.grid(row=1,column=1)
    Spinbox(framemenu5,from_=0,to=100,width=10,justify='center',textvariable=v5).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framemenu5,image=returnbtd,width=20,height=20,command=lambda:(framemenu5.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framemenu5.config(bg='#8ac4d0')
        text5.config(bg='#8ac4d0',fg='#000000')
        btd5.config(bg="#FFAB57",fg='#000000')
    else :
        framemenu5.config(bg='#4A4A4A')
        text5.config(bg='#4A4A4A',fg='#FFFFFF')
        btd5.config(bg="#643000",fg='#FFFFFF')
           
def etn5():
    global net5,data5
    total5 = Label(framemenu5,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=output5)
    total5.grid(row=2,column=1,columnspan=2,sticky="news")
    net5 = 0
    data5= int(v5.get())
    if v5.get() :
        net5 =109*data5
        output5.set("Total Price = %.2f Bahts"%net5)
    
    Button(framemenu5,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkout5).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        total5.config(bg='#8ac4d0',fg='#000000')
    else :
        total5.config(bg='#4A4A4A',fg='#FFFFFF')
        
def checkout5() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if net5 >= 300 :
        point = int(totalpoint) + 1
    if net5 >= 700 :
        point = int(totalpoint) + 2
    if net5 >= 1000 :
        point = int(totalpoint) + 3
    if net5 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"กระเป๋าว่ายน้ำเด็ก",data5,net5]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framemenu5.destroy()
        homepage()
        
def menu6() :
    global framemenu6
    framemenu6 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    shoplist.destroy()
    framemenu6.rowconfigure((0,1,2,3,4),weight=1)
    framemenu6.columnconfigure((0,1,2,3),weight=1)
    framemenu6.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framemenu6,image=menu6_img1,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framemenu6,image=menu6_img2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btd6 = Button(framemenu6,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etn6)
    btd6.grid(row=1,column=2,padx=20)
    text6 = Label(framemenu6,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    text6.grid(row=1,column=1)
    Spinbox(framemenu6,from_=0,to=100,width=10,justify='center',textvariable=v6).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framemenu6,image=returnbtd,width=20,height=20,command=lambda:(framemenu6.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framemenu6.config(bg='#8ac4d0')
        text6.config(bg='#8ac4d0',fg='#000000')
        btd6.config(bg="#FFAB57",fg='#000000')
    else :
        framemenu6.config(bg='#4A4A4A')
        text6.config(bg='#4A4A4A',fg='#FFFFFF')
        btd6.config(bg="#643000",fg='#FFFFFF')
           
def etn6():
    global net6,data6
    total6 = Label(framemenu6,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=output6)
    total6.grid(row=2,column=1,columnspan=2,sticky="news")
    net6 = 0
    data6= int(v6.get())
    if v6.get() :
        net6 =76*data6
        output6.set("Total Price = %.2f Bahts"%net6)
    
    Button(framemenu6,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkout6).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        total6.config(bg='#8ac4d0',fg='#000000')
    else :
        total6.config(bg='#4A4A4A',fg='#FFFFFF')
        
def checkout6() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if net6 >= 300 :
        point = int(totalpoint) + 1
    if net6 >= 700 :
        point = int(totalpoint) + 2
    if net6 >= 1000 :
        point = int(totalpoint) + 3
    if net6 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"Adepter Charger",data6,net6]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framemenu6.destroy()
        homepage()
            
def promotion1() :
    global framepromo1
    framepromo1 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    framepromo.destroy()
    shoplist.destroy()
    framepromo1.rowconfigure((0,1,2,3,4),weight=1)
    framepromo1.columnconfigure((0,1,2,3),weight=1)
    framepromo1.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framepromo1,image=promo1_3,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framepromo1,image=promo1_2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btdpromo1 = Button(framepromo1,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etnpromo1)
    btdpromo1.grid(row=1,column=2,padx=20)
    textpromo1 = Label(framepromo1,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    textpromo1.grid(row=1,column=1)
    Spinbox(framepromo1,from_=0,to=100,width=10,justify='center',textvariable=vpromo1).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framepromo1,image=returnbtd,width=20,height=20,command=lambda:(framepromo1.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framepromo1.config(bg='#8ac4d0')
        textpromo1.config(bg='#8ac4d0',fg='#000000')
        btdpromo1.config(bg="#FFAB57",fg='#000000')
    else :
        framepromo1.config(bg='#4A4A4A')
        textpromo1.config(bg='#4A4A4A',fg='#FFFFFF')
        btdpromo1.config(bg="#643000",fg='#FFFFFF')

def etnpromo1():
    global netpromo1,datapromo1
    totalpromo1 = Label(framepromo1,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=outputpromo1)
    totalpromo1.grid(row=2,column=1,columnspan=2,sticky="news")
    netpromo1 = 0
    datapromo1= int(vpromo1.get())
    if vpromo1.get() :
        netpromo1 =41*datapromo1
        outputpromo1.set("Total Price = %.2f Bahts"%netpromo1)
    
    Button(framepromo1,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkoutpromo1).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        totalpromo1.config(bg='#8ac4d0',fg='#000000')
    else :
        totalpromo1.config(bg='#4A4A4A',fg='#FFFFFF')

def checkoutpromo1() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if netpromo1 >= 300 :
        point = int(totalpoint) + 1
    if netpromo1 >= 700 :
        point = int(totalpoint) + 2
    if netpromo1 >= 1000 :
        point = int(totalpoint) + 3
    if netpromo1 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"ตัวต่อ Sanrio",datapromo1,netpromo1]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framepromo1.destroy()
        homepage()      

def promotion2() :
    global framepromo2
    framepromo2 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    framepromo.destroy()
    shoplist.destroy()
    framepromo2.rowconfigure((0,1,2,3,4),weight=1)
    framepromo2.columnconfigure((0,1,2,3),weight=1)
    framepromo2.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framepromo2,image=promo2_2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framepromo2,image=promo2_3,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btdpromo2 = Button(framepromo2,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etnpromo2)
    btdpromo2.grid(row=1,column=2,padx=20)
    textpromo2 = Label(framepromo2,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    textpromo2.grid(row=1,column=1)
    Spinbox(framepromo2,from_=0,to=100,width=10,justify='center',textvariable=vpromo2).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framepromo2,image=returnbtd,width=20,height=20,command=lambda:(framepromo2.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framepromo2.config(bg='#8ac4d0')
        textpromo2.config(bg='#8ac4d0',fg='#000000')
        btdpromo2.config(bg="#FFAB57",fg='#000000')
    else :
        framepromo2.config(bg='#4A4A4A')
        textpromo2.config(bg='#4A4A4A',fg='#FFFFFF')
        btdpromo2.config(bg="#643000",fg='#FFFFFF')

def etnpromo2():
    global netpromo2,datapromo2
    totalpromo2 = Label(framepromo2,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=outputpromo2)
    totalpromo2.grid(row=2,column=1,columnspan=2,sticky="news")
    netpromo2 = 0
    datapromo2= int(vpromo2.get())
    if vpromo2.get() :
        netpromo2 =9*datapromo2
        outputpromo2.set("Total Price = %.2f Bahts"%netpromo2)
    
    Button(framepromo2,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkoutpromo2).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        totalpromo2.config(bg='#8ac4d0',fg='#000000')
    else :
        totalpromo2.config(bg='#4A4A4A',fg='#FFFFFF')

def checkoutpromo2() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if netpromo2 >= 300 :
        point = int(totalpoint) + 1
    if netpromo2 >= 700 :
        point = int(totalpoint) + 2
    if netpromo2 >= 1000 :
        point = int(totalpoint) + 3
    if netpromo2 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"สร้อยข้อมือโซ่",datapromo2,netpromo2]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framepromo2.destroy()
        homepage()
        
def promotion3() :
    global framepromo3
    framepromo3 = Frame(root,bg='#8ac4d0')
    menuframe.destroy()
    framepromo.destroy()
    shoplist.destroy()
    framepromo3.rowconfigure((0,1,2,3,4),weight=1)
    framepromo3.columnconfigure((0,1,2,3),weight=1)
    framepromo3.grid(row=0,column=0,rowspan=4,columnspan=3,sticky="news")
    Label(framepromo3,image=promo3_2,fg='#000000',font="Garamond 20 bold").grid(row=0,column=1,sticky="n",pady=27)
    Label(framepromo3,image=promo3_3,fg='#000000',font="Garamond 20 bold").grid(row=0,column=2,sticky="e")
    btdpromo3 = Button(framepromo3,text="ซื้อเลย",bg="#FFAB57",width=20,fg='#000000',font="Garamond 20 bold",command=etnpromo3)
    btdpromo3.grid(row=1,column=2,padx=20)
    textpromo3 = Label(framepromo3,text="จำนวนสินค้า",bg='#8ac4d0',fg='#000000',font="Tahoma 14 bold")
    textpromo3.grid(row=1,column=1)
    Spinbox(framepromo3,from_=0,to=100,width=10,justify='center',textvariable=vpromo3).grid(row=1,column=2,ipadx=10,sticky="w")
    Button(framepromo3,image=returnbtd,width=20,height=20,command=lambda:(framepromo3.destroy(),homepage())).grid(row=0,column=0,padx=8,sticky="ne")
    if lightdark == True :
        framepromo3.config(bg='#8ac4d0')
        textpromo3.config(bg='#8ac4d0',fg='#000000')
        btdpromo3.config(bg="#FFAB57",fg='#000000')
    else :
        framepromo3.config(bg='#4A4A4A')
        textpromo3.config(bg='#4A4A4A',fg='#FFFFFF')
        btdpromo3.config(bg="#643000",fg='#FFFFFF')

def etnpromo3():
    global netpromo3,datapromo3
    totalpromo3 = Label(framepromo3,bg='#8ac4d0',fg='#000000',font=('Angsana',25,'bold'),textvariable=outputpromo3)
    totalpromo3.grid(row=2,column=1,columnspan=2,sticky="news")
    netpromo3 = 0
    datapromo3= int(vpromo3.get())
    if vpromo3.get() :
        netpromo3 =1950*datapromo3
        outputpromo3.set("Total Price = %.2f Bahts"%netpromo3)
    
    Button(framepromo3,text="Click for CHECK OUT",bg='#FFFFFF',fg='#000000',font="Garamond 20 bold",command=checkoutpromo3).grid(row=3,column=1,columnspan=2,sticky="s")        
    if lightdark == True :
        totalpromo3.config(bg='#8ac4d0',fg='#000000')
    else :
        totalpromo3.config(bg='#4A4A4A',fg='#FFFFFF')

def checkoutpromo3() :
    sql = "select point from members where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totalpoint = "%r"%result
    if netpromo3 >= 300 :
        point = int(totalpoint) + 1
    if netpromo3 >= 700 :
        point = int(totalpoint) + 2
    if netpromo3 >= 1000 :
        point = int(totalpoint) + 3
    if netpromo3 < 300 :
        point = int(totalpoint) + 0
    print(int(point))
    msg = messagebox.askquestion("Admin","Are you sure you want to check out",icon="warning")
    if msg == "no" :
        print(" ")
    else :
        ins_sql = '''
            INSERT INTO shophistory("username","product_name","amount","price")
            VALUES (?,?,?,?)
            '''
        param = [user_result[0],"Samsung Galaxy Buds Live",datapromo3,netpromo3]
        cursor.execute(ins_sql, param)
        conn.commit()
        point_sql = '''
                UPDATE members 
                SET point = ? WHERE username = ?
        '''
        cursor.execute(point_sql,[int(point),user_result[0]])
        conn.commit()
        messagebox.showinfo("Admin","ซื้อสินค้าสำเร็จ")
        messagebox.showinfo("Admin","You have "+str(point)+" point")
        framepromo3.destroy()
        homepage()
        
def history() :
    global framehistory,mytree
    menuframe.destroy()
    shoplist.destroy()
    framehistory = Frame(root,bg="#A9EA94")
    framehistory.rowconfigure([0,1,2,3,4,5,6],weight=1)
    framehistory.columnconfigure([0,3],weight=1)
    framehistory.columnconfigure([1,2],weight=3)
    framehistory.grid(row=0,column=0,rowspan=7,columnspan=4,sticky="news")
    historyimg = Label(framehistory,image=img_bg3)
    historyimg.grid(row=0,column=0,rowspan=7,columnspan=4,sticky="news")
    history1 = Label(framehistory,bg="#A9EA94")
    history1.grid(row=1,column=1,rowspan=5,columnspan=2,sticky="news")
    history2 = Label(framehistory,text="ประวัติการสั่งซื้อ",bg="#A9EA94",font="Tahoma 24 bold")
    history2.grid(row=1,column=0,columnspan=4)
    history3 = Label(framehistory,text="User : "+user_result[2]+" "+user_result[3],bg="#A9EA94",font="Tahoma 24 bold")
    history3.grid(row=2,column=1,columnspan=4,sticky="w",padx=10)
    Button(framehistory,image=returnbtd,width=20,height=20,command=lambda:(framehistory.destroy(),homepage())).grid(row=1,column=1,columnspan=4,padx=8,sticky="w")
    mytree = ttk.Treeview(framehistory, columns=("product_name", "amount", "price"), height=2)
    #create headings
    mytree.heading('#0', text='') 
    mytree.heading('product_name', text="Product Name", anchor=W)
    mytree.heading('amount', text="Amount", anchor=W)
    mytree.heading('price', text="Price", anchor=W)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('product_name', anchor=W, width=200)
    mytree.column('amount', anchor=W, width=150)
    mytree.column('price', anchor=W, width=150)
    mytree.grid(row=3, column=1,columnspan=2, sticky='ns')
    fetch_tree()
    totalbtd = Button(framehistory,text="ราคาสินค้ารวม",font="Tahoma 20 bold",bg="#165103",fg="white",command=historytotal)
    totalbtd.grid(row=5,column=1,columnspan=4,sticky="w",padx=10)   
    if lightdark == True :
        framehistory.config(bg="#A9EA94")
        historyimg.config(image=img_bg3)
        history1.config(bg="#A9EA94",fg="black")
        history2.config(bg="#A9EA94",fg="black")
        history3.config(bg="#A9EA94",fg="black")
        totalbtd.config(bg="#165103",fg="white")
    else :
        framehistory.config(bg="#165103")
        historyimg.config(image=img_bg3_d)
        history1.config(bg="#165103",fg="white")
        history2.config(bg="#165103",fg="white")
        history3.config(bg="#165103",fg="white")
        totalbtd.config(bg="#A9EA94",fg="black")
        
def fetch_tree():
    mytree.delete(*mytree.get_children())
    sql = "select * from shophistory where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchall()
    if result :
        for i ,data in enumerate(result) :
            mytree.insert('','end',values=(data[2],data[3],data[4]))

def historytotal() :
    global total
    sql = "select SUM(price) as [Total] from shophistory where username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    totaltext1 = Label(framehistory,text="Total price = ",bg="#A9EA94",font="Tahoma 16 bold")
    totaltext1.grid(row=4,column=1,sticky="e")
    totaltext2 = Label(framehistory,text=result,bg="#A9EA94",font="Tahoma 16 bold")
    totaltext2.grid(row=4,column=2,sticky="w",padx=50)
    totaltext3 = Label(framehistory,text="บาท",bg="#A9EA94",font="Tahoma 16 bold")
    totaltext3.grid(row=4,column=2)
    if lightdark == True :
        totaltext1.config(bg="#A9EA94",fg="black")
        totaltext2.config(bg="#A9EA94",fg="black")
        totaltext3.config(bg="#A9EA94",fg="black")
    else :
        totaltext1.config(bg="#165103",fg="white")
        totaltext2.config(bg="#165103",fg="white")
        totaltext3.config(bg="#165103",fg="white")

def updatepoint() :
    global currentpoint
    sql = "SELECT point FROM members WHERE username = ?"
    cursor.execute(sql,[user_result[0]])
    result = cursor.fetchone()
    currentpoint = str(result[0])
             
def lightdarkmode() :
    global lightdark
    if lightdark :
        lightdarkbtd.config(image=dark,activebackground="#64367D",bd=0,bg="#64367D")
        shoplist.config(bg="#515151")
        menuframe.config(bg="#64367D")
        logo.config(bg="#64367D",fg="white")
        welcometext.config(bg="#64367D",fg="white")
        pointtext.config(bg="#64367D",fg="white")
        lightdark = False
        
    else :
        lightdarkbtd.config(image=light,activebackground="#FDDF4B",bd=0,bg="#FDDF4B")
        shoplist.config(bg="white")
        menuframe.config(bg="#FDDF4B")
        logo.config(bg="#FDDF4B",fg="black")
        welcometext.config(bg="#FDDF4B",fg="black")
        pointtext.config(bg="#FDDF4B",fg="black")
        lightdark = True
    
def logout() :
    menuframe.destroy()
    shoplist.destroy()
    loginlayout()
    userentry.delete(0, END)
    pwdentry.delete(0,END)
    userentry.focus_force()
    
createconnection()
root = mainwindow()

img_bg1 = PhotoImage(file="images/bg/bg1.png")
img_bg2 = PhotoImage(file="images/bg/bg2.png")
img_bg3 = PhotoImage(file="images/bg/bg3.png")
img_bg3_d = PhotoImage(file="images/bg/bg3_dark.png")

logo_img = PhotoImage(file="images/etc/logo.png").subsample(5,5)
logo2_img = PhotoImage(file="images/etc/logo.png").subsample(15,15)
img_cart = PhotoImage(file="images/etc/cart.png").subsample(5,5)
light = PhotoImage(file="images/etc/day.png").subsample(3,3)
dark = PhotoImage(file="images/etc/night.png").subsample(3,3)
returnbtd = PhotoImage(file='images/etc/return.png')
img_history = PhotoImage(file="images/etc/history.png").subsample(5,5)

item1 = PhotoImage(file="images/menu/1.png").subsample(2,2)
item2 = PhotoImage(file="images/menu/2.png").subsample(2,2)
item3 = PhotoImage(file="images/menu/3.png").subsample(2,2)
item4 = PhotoImage(file="images/menu/4.png").subsample(2,2)
item5 = PhotoImage(file="images/menu/5.png").subsample(2,2)
item6 = PhotoImage(file="images/menu/6.png").subsample(2,2)


promo1 = PhotoImage(file='images/promotion1/promo1.png').subsample(3,3)
promo1_2 = PhotoImage(file='images/promotion1/promo1_2.png')
promo1_3 = PhotoImage(file='images/promotion1/promo1_3.png').subsample(2,2)
promo2 = PhotoImage(file='images/promotion2/promo2.png').subsample(3,3)
promo2_2 = PhotoImage(file='images/promotion2/promo2_2.png').subsample(2,2)
promo2_3 = PhotoImage(file='images/promotion2/promo2_3.png')
promo3 = PhotoImage(file='images/promotion3/promo3.png').subsample(3,3)
promo3_2 = PhotoImage(file='images/promotion3/promo3_2.png').subsample(2,2)
promo3_3 = PhotoImage(file='images/promotion3/promo3_3.png')

menu1_img1 = PhotoImage(file='images/menu/Screenshot 2023-05-07 232646.png').subsample(2,2)
menu1_img2 = PhotoImage(file='images/menu/Screenshot 2023-05-07 232703.png')

menu2_img1 = PhotoImage(file='images/menu/22.png').subsample(2,2)
menu2_img2 = PhotoImage(file='images/menu/7.png')

menu3_img1 = PhotoImage(file='images/menu/8.png').subsample(2,2)
menu3_img2 = PhotoImage(file='images/menu/9.png')

menu4_img1 = PhotoImage(file='images/menu/10.png').subsample(2,2)
menu4_img2 = PhotoImage(file='images/menu/11.png')

menu5_img1 = PhotoImage(file='images/menu/12.png').subsample(2,2)
menu5_img2 = PhotoImage(file='images/menu/13.png')

menu6_img1 = PhotoImage(file='images/menu/14.png').subsample(2,2)
menu6_img2 = PhotoImage(file='images/menu/15.png')

lightdark = True
userinfo = StringVar() 
pwdinfo = StringVar()
v1,v2,v3,v4,v5,v6 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
vpromo1,vpromo2,vpromo3 = StringVar(),StringVar(),StringVar()
output1,output2,output3,output4,output5,output6,outputall = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
outputpromo1,outputpromo2,outputpromo3 = StringVar(),StringVar(),StringVar()
loginlayout()
root.mainloop()