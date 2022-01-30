from email import message
import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openAdopt():
    root_adopt = Toplevel()
    root_adopt.title("Adopt")
    root_adopt.minsize(width=400,height=400)
    root_adopt.geometry("1920x1800")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('pup.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_adopt, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_adopt,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Adoption data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_adopt,text="Add Adoption record",bg='black', fg='white', command=IssueAdoption)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_adopt,text="Remove Adoption record",bg='black', fg='white', command=removeAdoptions)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_adopt,text="View Adoptions",bg='black', fg='white', command=viewAdoptions)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    root_adopt.mainloop()


def IssueAdoption():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Animal Adoption")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Issue Adoption", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Customer ID
    lb2 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    cus_id = Entry(labelFrame)
    cus_id.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Adoption Date
    lb3 = Label(labelFrame,text="Date (yyyy-mm-dd) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    ad_date = Entry(labelFrame)
    ad_date.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
    
    def sqInsertAdopt(an_id,cust_id,ad_date):
        cur.execute("INSERT INTO ADOPT VALUES(?,?,?);",(an_id,cust_id,ad_date))
        con.commit()

    def Issue():
        animal_id = an_id.get()
        customer_id = cus_id.get()
        adopt_date = ad_date.get()
        
        checkAvail = "select details from animal where an_id = '"+an_id.get()+"'"
        cur.execute(checkAvail)
        con.commit()
        for i in cur:
            check = i[0]
            
        if check == 'avail':
            status = True
        else:
            status = False

        try:
            if status == True:
                sqInsertAdopt(animal_id, customer_id, adopt_date)
                cur.execute("UPDATE ANIMAL SET DETAILS = 'Adopted' WHERE AN_ID = '"+animal_id+"'")
                con.commit()
                messagebox.showinfo('Success', "Successfully Issued for Adoption", parent = root)
            else:
                messagebox.showerror("Error", "Animal not available for adoption", parent = root)
        except:
            messagebox.showerror('Error', "Something went wrong", parent = root)
        
        print(animal_id)
        print(customer_id)
        print(adopt_date)
        
        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=Issue)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

    

def removeAdoptions():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove Adoptions")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Adoption record", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Customer ID
    lb2 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    cust_id = Entry(labelFrame)
    cust_id.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

    # foster date
    lb3 = Label(labelFrame,text="Date (yyyy-mm-dd): ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    ad_date = Entry(labelFrame)
    ad_date.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)


    def sqDeleteAdopt(an_id, cust_id, ad_date):
        cur.execute("DELETE FROM ADOPT WHERE AN_ID=? AND CUST_ID=? AND AD_DATE=?;",(an_id, cust_id, ad_date))
        con.commit()

    def deleteAdopt():
        animal_id =an_id.get()
        customer_id = cust_id.get()
        adopt_date = ad_date.get()

        try:
            sqDeleteAdopt(animal_id, customer_id, adopt_date)
            messagebox.showinfo("Success", "Foster record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        an_id.delete(0, END)
        cust_id.delete(0, END)
        ad_date.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteAdopt)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()



def viewAdoptions():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Adopt")
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

        def sqSearchAdopt(key):
            cur.execute("SELECT * FROM ADOPT WHERE AN_ID LIKE ? OR CUST_ID LIKE ? OR AD_DATE LIKE ?;",(key,key,key))
            adlist=cur.fetchall()
            return adlist 


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

            records = sqSearchAdopt(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)



    records = cur.execute("SELECT * FROM adopt")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("an_id", "cust_id", "ad_date")
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
    style.map("Treeview", background = [('selected', 'orange')])


    tree.column("an_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("cust_id", width=250, minwidth=50, anchor=CENTER)
    tree.column("ad_date", width=200, minwidth=50, anchor=CENTER)

    tree.heading("an_id", text="Animal Id", anchor=CENTER)
    tree.heading("cust_id", text="Customer ID", anchor=CENTER)
    tree.heading("ad_date", text="Date", anchor=CENTER)

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels
    lb1 = Label(add_frame, text="Animal ID")
    lb1.grid(row=0, column=0,  padx=210, pady=10)

    lb2 = Label(add_frame, text="Customer ID")
    lb2.grid(row=0, column=1,  padx=210, pady=10)

    lb3 = Label(add_frame, text="Date")
    lb3.grid(row=0, column=2, padx=210, pady=10)


    #Entry boxes
    an_id = Entry(add_frame)
    an_id.grid(row=1, column=0)

    cust_id = Entry(add_frame)
    cust_id.grid(row=1, column=1)

    ad_date = Entry(add_frame)
    ad_date.grid(row=1, column=2)


    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertAdopt(an_id,cust_id,ad_date):
            cur.execute("INSERT INTO ADOPT VALUES(?,?,?);",(an_id,cust_id,ad_date))
            con.commit()
           
        checkAvail = "select details from animal where an_id = '"+an_id.get()+"'"
        cur.execute(checkAvail)
        con.commit()
        for i in cur:
            check = i[0]
            
        if check == 'avail':
            status = True
        else:
            status = False

        try:
            if status == True:
                sqInsertAdopt(an_id.get(), cust_id.get(), ad_date.get())
                cur.execute("UPDATE ANIMAL SET DETAILS = 'Adopted' WHERE AN_ID = '"+an_id.get()+"'")
                con.commit()
                tree.insert(parent='', index='end', text="", values=(an_id.get(), cust_id.get(), ad_date.get()))
                
                # Clear the boxes
                an_id.delete(0, END)
                cust_id.delete(0, END)
                ad_date.delete(0, END) 
            else:
                messagebox.showerror("Error", "Animal not available for adoption", parent=root_new)
        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteAdopt(ftuple):
            cur.execute("DELETE FROM ADOPT WHERE AN_ID=? AND CUST_ID=? AND AD_DATE=?;",(ftuple[0], ftuple[1], ftuple[2]))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteAdopt(values)

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        an_id.delete(0, END)
        cust_id.delete(0, END)
        ad_date.delete(0, END)

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        an_id.insert(0, values[0])
        cust_id.insert(0, values[1])
        ad_date.insert(0, values[2])

    
    def update_record():

        def sqDeleteAdopt(ftuple):
            cur.execute("DELETE FROM ADOPT WHERE AN_ID=? AND CUST_ID=? AND AD_DATE=?;",(ftuple[0], ftuple[1], ftuple[2]))
            con.commit()

        def sqInsertAdopt(an_id,cust_id,ad_date):
            cur.execute("INSERT INTO ADOPT VALUES(?,?,?);",(an_id,cust_id,ad_date))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(an_id.get(), cust_id.get(), ad_date.get()))
            sqDeleteAdopt(values)
            values = tree.item(selected, 'values')
            sqInsertAdopt(an_id.get(), cust_id.get(), ad_date.get())
            

            # Clear entry boxes
            an_id.delete(0, END)
            cust_id.delete(0, END)
            ad_date.delete(0, END)

        except:
            messagebox.showerror("Error", "Something went wrong", parent=root_new)

        
    button_frame = LabelFrame(root_new, bg = "orange", text = "Commands")
    button_frame.pack(fill= "x", expand = "yes", padx = 20)

    #add new record
    add_button = Button(button_frame, text="Add Record", command=add_record)
    add_button.grid(row=0, column=0, padx=145, pady=10)

    #select record to edit
    edit_button = Button(button_frame, text="Edit Record", command=edit_record)
    edit_button.grid(row=0, column=1, padx=145, pady=10)

    #update selected
    update_button = Button(button_frame, text="Save Record", command=update_record)
    update_button.grid(row=0, column=2, padx=145, pady=10)

    # Remove Selected
    remove_one = Button(button_frame, text="Remove Selected Record", command=remove_record)
    remove_one.grid(row=0, column=3, padx=145, pady=10)

    root_new.mainloop()
    
   