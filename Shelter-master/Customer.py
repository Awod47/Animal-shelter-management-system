import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk
from tkinter.font import nametofont
from Adopt import *
from Foster import * 

def openCustomer():
    root_cus = Toplevel()
    root_cus.title("Customer")
    root_cus.minsize(width=400,height=400)
    root_cus.geometry("1920x1800")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('shelter-cust.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_cus, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_cus,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Customer data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_cus,text="Add Customer",bg='black', fg='white', command=registerCustomer)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_cus,text="Remove Customer",bg='black', fg='white', command=removeCustomer)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_cus,text="View Customers",bg='black', fg='white', command=viewCustomers)
    btn3.place(relx=0.37,rely=0.5, relwidth=0.25,relheight=0.05)

    btn7 = Button(root_cus,text="Foster",bg='black', fg='white', command=openFoster)
    btn7.place(relx=0.05,rely=0.70, relwidth=0.25,relheight=0.05)

    btn8 = Button(root_cus,text="Issue Adoption",bg='black', fg='white', command=openAdopt)
    btn8.place(relx=0.70,rely=0.70, relwidth=0.25,relheight=0.05)

    btn1.config(font=('Times New Roman',15))
    btn2.config(font=('Times New Roman',15))
    btn3.config(font=('Times New Roman',15))
    btn7.config(font=('Times New Roman',15))
    btn8.config(font=('Times New Roman',15))


    root_cus.mainloop()


def registerCustomer():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Animal")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    CustomerTable = "Customer" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Animal", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # # Customer ID
    # lb1 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    # lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    # cust_id = Entry(labelFrame)
    # cust_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Customer name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    cust_name = Entry(labelFrame)
    cust_name.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Customer phone
    lb3 = Label(labelFrame,text="Phone : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    cust_phone = Entry(labelFrame)
    cust_phone.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # Customer dob
    lb4 = Label(labelFrame,text="Date of birth (yyyy-mm-dd) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    dob= Entry(labelFrame)
    dob.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # Customer address
    lb4 = Label(labelFrame,text="Address : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.6, relheight=0.08)
        
    address = Entry(labelFrame)
    address.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    def sqInsertCustomer(cname,phone,dob,address):
        cur.execute("SELECT cust_id from Customer")
        anidlist=cur.fetchall()
        idlist=list()
        for i in anidlist :
            num=int(i[0][1:])
            idlist.append(num)
        for newid in range(1,9999) :
            if newid in idlist :
                continue
            else :
                break
        if newid<10 :
            newidstr = "c000" + str(newid)
        elif newid<100 :
            newidstr = "c00" + str(newid)
        elif newid<1000 :
            newidstr = "c0" + str(newid)
        else :
            newidstr = "c" +str(newid)
        cur.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?);",(newidstr,cname,phone,dob,address))
        con.commit()
        return newidstr

    def AddCustomer():
        #customer_id = cust_id.get()
        customer_name = cust_name.get()
        customer_phone = int(cust_phone.get())
        customer_dob = dob.get()
        customer_address = address.get()

        try:
            customer_id = sqInsertCustomer(customer_name, customer_phone, customer_dob, customer_address)
            messagebox.showinfo('Success', "Customer added")
        except:
            messagebox.showerror('Error', "Something went wrong")
        
        print(customer_id)
        print(customer_name)
        print(customer_phone)
        print(customer_dob)
        print(customer_address)

        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=AddCustomer)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',15))
    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))
    
    root.mainloop()


def removeCustomer():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Customer")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    CustomerTable = "Customer"


    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Customer", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    cust_id = Entry(labelFrame)
    cust_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)


    def sqDeleteCustomer(cid):
        cur.execute("DELETE FROM ADOPT WHERE CUST_ID=?;",(cid,))
        cur.execute("DELETE FROM FOSTER WHERE CUST_ID=?;",(cid,))
        cur.execute("DELETE FROM CUSTOMER WHERE CUST_ID=?;",(cid,))
        con.commit()

    def deleteCustomer():
        customer_id = cust_id.get()
        

        try:
            sqDeleteCustomer(customer_id)
            messagebox.showinfo("Success", "Customer record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        print(customer_id)
        cust_id.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteCustomer)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',15))
    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))
    
    root.mainloop()





def viewCustomers():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Customer")
    root_new.minsize(width=400,height=400)
    root_new.geometry("1920x1800")
    root_new.configure(bg="#222222")

    def lookup_records():

        search = Toplevel(root_new)
        search.title("Lookup Records")
        search.geometry("400x200")

        # Create label frame
        search_frame = LabelFrame(search, text="Key")
        search_frame.pack(padx=10, pady=10)

        # Add entry box
        search_entry = Entry(search_frame, font=("Helvetica", 18))
        search_entry.pack(pady=20, padx=20)

        def sqSearchCustomer(key):
            cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID LIKE ? OR CUST_NAME LIKE ? OR PHONE LIKE ? OR DOB LIKE ? OR ADDRESS LIKE ?;",(key,key,key,key,key))
            custlist = cur.fetchall()
            return custlist


        def search_records():
            lookup_record = search_entry.get()
            search.destroy()
            
            for record in tree.get_children():
                tree.delete(record)
            
            try:
                con = sqlite3.connect("shelter.db")
                cur = con.cursor()
            except Exception as e:
                print("error during connection: "+str(e))

            records = sqSearchCustomer(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)

    records = cur.execute("SELECT * FROM Customer")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("cust_id", "cust_name", "phone", "DOB", "address")
    tree['show'] =  'headings'

    my_menu = Menu(root_new)
    root_new.config(menu=my_menu)

    search_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Search", menu=search_menu)
    # Drop down menu
    search_menu.add_command(label="Search", command=lookup_records)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="white", foreground="white", fieldbackground = "white")
    style.configure('Treeview', rowheight=40)
    style.configure('Treeview', columnwidth=70)
    style.configure("Treeview.Heading", font=(None, 20))
    style.configure("Treeview.Column", font=(None, 20))
    style.map("Treeview", background = [('selected', 'orange')])

    nametofont("TkDefaultFont").configure(size=13)

    tree.column("cust_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("cust_name", width=200, minwidth=50, anchor=CENTER)
    tree.column("phone", width=200, minwidth=50, anchor=CENTER)
    tree.column("DOB", width=250, minwidth=50, anchor=CENTER)
    tree.column("address", width=350, minwidth=50, anchor=CENTER)
    

    tree.heading("cust_id", text="Customer Id", anchor=CENTER)
    tree.heading("cust_name", text="Name", anchor=CENTER)
    tree.heading("phone", text="Phone Number", anchor=CENTER)
    tree.heading("DOB", text="Date of birth", anchor=CENTER)
    tree.heading("address", text="Home Address", anchor=CENTER)
    

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
        i+= 1

    tree.pack()
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels

    lb2 = Label(add_frame, text="Name")
    lb2.grid(row=0, column=0, padx=160, pady=10)

    lb3 = Label(add_frame, text="Phone")
    lb3.grid(row=0, column=1, padx=160, pady=10)

    lb4 = Label(add_frame, text="Date of birth")
    lb4.grid(row=0, column=2, padx=160, pady=10)

    lb5 = Label(add_frame, text="Address")
    lb5.grid(row=0, column=3, padx=160, pady=10)

    lb2.config(font=('Times New Roman',15))
    lb3.config(font=('Times New Roman',15))
    lb4.config(font=('Times New Roman',15))
    lb5.config(font=('Times New Roman',15))

    #Entry boxes

    cust_name = Entry(add_frame)
    cust_name.grid(row=1, column=0)

    phone = Entry(add_frame)
    phone.grid(row=1, column=1)

    Dob = Entry(add_frame)
    Dob.grid(row=1, column=2)

    address = Entry(add_frame)
    address.grid(row=1, column=3)



    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertCustomer(cname,phone,dob,address):
            cur.execute("SELECT cust_id from Customer")
            anidlist=cur.fetchall()
            idlist=list()
            for i in anidlist :
                num=int(i[0][1:])
                idlist.append(num)
            for newid in range(1,9999) :
                if newid in idlist :
                    continue
                else :
                    break
            if newid<10 :
                newidstr = "c000" + str(newid)
            elif newid<100 :
                newidstr = "c00" + str(newid)
            elif newid<1000 :
                newidstr = "c0" + str(newid)
            else :
                newidstr = "c" +str(newid)
            cur.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?);",(newidstr,cname,phone,dob,address))
            con.commit()
            return newidstr

        try:
            customer_id = sqInsertCustomer(cust_name.get(), int(phone.get()), Dob.get(), address.get())
            tree.insert(parent='', index='end', text="", values=(customer_id, cust_name.get(), phone.get(), Dob.get(), address.get()))
           
            # Clear the boxes
            cust_name.delete(0, END)
            phone.delete(0, END)
            Dob.delete(0, END)
            address.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteCustomer(cid):
            cur.execute("DELETE FROM ADOPT WHERE CUST_ID=?;",(cid,))
            cur.execute("DELETE FROM FOSTER WHERE CUST_ID=?;",(cid,))
            cur.execute("DELETE FROM CUSTOMER WHERE CUST_ID=?;",(cid,))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteCustomer(values[0])

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        cust_name.delete(0, END)
        phone.delete(0, END)
        Dob.delete(0, END)
        address.delete(0, END)
        
        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        cust_name.insert(0, values[1])
        phone.insert(0, values[2])
        Dob.insert(0, values[3])
        address.insert(0, values[4])

    
    def update_record():

        def sqModifyCustomer(ctuple):
            cur.execute("UPDATE CUSTOMER SET CUST_NAME=?,PHONE=?,DOB=?,ADDRESS=? WHERE CUST_ID=?;",(ctuple[1],ctuple[2],ctuple[3],ctuple[4],ctuple[0]))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(values[0], cust_name.get(), phone.get(), Dob.get(), address.get()))
            values = tree.item(selected, 'values')
            sqModifyCustomer(values)

            # Clear entry boxes
            cust_name.delete(0, END)
            phone.delete(0, END)
            Dob.delete(0, END)
            address.delete(0, END)

        except:
            messagebox.showerror("Error", "Something went wrong", parent=root_new)

        
    button_frame = LabelFrame(root_new, bg = "orange", text = "Commands")
    button_frame.pack(fill= "x", expand = "yes", padx = 20)

    #add new record
    add_button = Button(button_frame, text="Add Record", command=add_record)
    add_button.grid(row=0, column=0, padx=125, pady=5)

    #select record to edit
    edit_button = Button(button_frame, text="Edit Record", command=edit_record)
    edit_button.grid(row=0, column=1, padx=125, pady=5)

    #update selected
    update_button = Button(button_frame, text="Save Record", command=update_record)
    update_button.grid(row=0, column=2, padx=125, pady=5)

    # Remove Selected
    remove_one = Button(button_frame, text="Remove Selected Record", command=remove_record)
    remove_one.grid(row=0, column=3, padx=125, pady=5)

    add_button.config(font=('Times New Roman',15))
    edit_button.config(font=('Times New Roman',15))
    update_button.config(font=('Times New Roman',15))
    remove_one.config(font=('Times New Roman',15))

    root_new.mainloop()
    
   


