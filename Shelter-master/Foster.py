import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openFoster():
    root_fos = Toplevel()
    root_fos.title("Foster")
    root_fos.minsize(width=400,height=400)
    root_fos.geometry("1920x1800")

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
    label = ttk.Label(root_fos, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_fos,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Animal data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_fos,text="New Foster record",bg='black', fg='white', command=IssueFoster)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_fos,text="Remove Foster record",bg='black', fg='white', command=removeFosters)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_fos,text="View Foster records",bg='black', fg='white', command=viewFosters)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    root_fos.mainloop()


def IssueFoster():

    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Animal Foster")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Foster", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.4,rely=0.2, relwidth=0.52)
    
    # Issued To customer id 
    lb2 = Label(labelFrame,text="Customer ID (foster): ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    cust_id = Entry(labelFrame)
    cust_id.place(relx=0.4,rely=0.4, relwidth=0.52)

    # Date issued
    lb3 = Label(labelFrame,text="Date (yyyy-mm-dd) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.6)
        
    fost_date = Entry(labelFrame)
    fost_date.place(relx=0.4,rely=0.6, relwidth=0.52)

    lb4 = Label(labelFrame,text="Due Date (yyyy-mm-dd) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.8)
        
    fost_duedate = Entry(labelFrame)
    fost_duedate.place(relx=0.4,rely=0.8, relwidth=0.52)
    
    def sqInsertFoster(an_id,cust_id,fost_date,due_date):
        cur.execute("INSERT INTO Foster VALUES(?,?,?,?);",(an_id,cust_id,fost_date,due_date))
        
        con.commit()
        
    def Issue():
        animal_id = an_id.get()
        customer_id = cust_id.get()
        foster_date = fost_date.get()
        foster_dueDate = fost_duedate.get()

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
                sqInsertFoster(animal_id, customer_id, foster_date, foster_dueDate)
                cur.execute("UPDATE ANIMAL SET DETAILS = 'IFC' WHERE AN_ID = '"+animal_id+"'")
                con.commit()
                messagebox.showinfo('Success', "Animal Successfully Issued for foster care", parent = root)
            else:
                messagebox.showerror("Error", "Animal not available for foster", parent = root)
        except:
            messagebox.showerror('Error', "Something went wrong", parent = root)

        print(animal_id)
        print(customer_id)
        print(foster_date)
        print(foster_dueDate)
        root.destroy()

    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=Issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def removeFosters():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove Foster")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Foster record", bg='black', fg='white', font=('Courier',15))
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
        
    fost_date = Entry(labelFrame)
    fost_date.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # due date
    lb4 = Label(labelFrame,text="Due Date (yyyy-mm-dd): ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    d_date = Entry(labelFrame)
    d_date.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)


    def sqDeleteFoster(an_id, cust_id, fost_date, due_date):
        cur.execute("DELETE FROM FOSTER WHERE AN_ID=? AND CUST_ID=? AND FOST_DATE=? AND DUE_DATE=?;",(an_id, cust_id, fost_date, due_date))
        con.commit()

    def deleteFoster():
        animal_id =an_id.get()
        customer_id = cust_id.get()
        foster_date = fost_date.get()
        due_date = d_date.get()

        try:
            sqDeleteFoster(animal_id, customer_id, foster_date, due_date)
            messagebox.showinfo("Success", "Foster record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        an_id.delete(0, END)
        cust_id.delete(0, END)
        fost_date.delete(0, END)
        d_date.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteFoster)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


    

def viewFosters():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Foster")
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

        def sqSearchFoster(key):
            cur.execute("SELECT * FROM FOSTER WHERE AN_ID LIKE ? OR CUST_ID LIKE ? OR FOST_date LIKE ? or Due_date LIKE ?;",(key,key,key,key))
            foslist=cur.fetchall()
            return foslist      
 


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

            records = sqSearchFoster(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)



    records = cur.execute("SELECT * FROM foster")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("an_id", "cust_id", "fost_date", "due_date")
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
    tree.column("fost_date", width=200, minwidth=50, anchor=CENTER)
    tree.column("due_date", width=200, minwidth=50, anchor=CENTER)

    tree.heading("an_id", text="Animal Id", anchor=CENTER)
    tree.heading("cust_id", text="Customer ID", anchor=CENTER)
    tree.heading("fost_date", text="Date", anchor=CENTER)
    tree.heading("due_date", text="Return Date", anchor=CENTER)

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels
    lb1 = Label(add_frame, text="Animal ID")
    lb1.grid(row=0, column=0,  padx=150, pady=10)

    lb2 = Label(add_frame, text="Customer ID")
    lb2.grid(row=0, column=1,  padx=150, pady=10)

    lb3 = Label(add_frame, text="Date")
    lb3.grid(row=0, column=2, padx=150, pady=10)

    lb4 = Label(add_frame, text="Return Date")
    lb4.grid(row=0, column=3, padx=150, pady=10)


    #Entry boxes
    an_id = Entry(add_frame)
    an_id.grid(row=1, column=0)

    cust_id = Entry(add_frame)
    cust_id.grid(row=1, column=1)

    fost_date = Entry(add_frame)
    fost_date.grid(row=1, column=2)

    d_date = Entry(add_frame)
    d_date.grid(row=1, column=3)



    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertFoster(an_id,cust_id,fost_date,due_date):
            cur.execute("INSERT INTO Foster VALUES(?,?,?,?);",(an_id,cust_id,fost_date,due_date))
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
                sqInsertFoster(an_id.get(), cust_id.get(), fost_date.get(), d_date.get())
                cur.execute("UPDATE ANIMAL SET DETAILS = 'IFC' WHERE AN_ID = '"+an_id.get()+"'")
                con.commit()
                tree.insert(parent='', index='end', text="", values=(an_id.get(), cust_id.get(), fost_date.get(), d_date.get()))
            
                # Clear the boxes
                an_id.delete(0, END)
                cust_id.delete(0, END)
                fost_date.delete(0, END)
                d_date.delete(0, END)
            else:
                messagebox.showerror("Error", "Animal not available for Foster", parent = root_new)
        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteFoster(ftuple):
            cur.execute("DELETE FROM FOSTER WHERE AN_ID=? AND CUST_ID=? AND FOST_DATE=? AND DUE_DATE=?;",(ftuple[0], ftuple[1], ftuple[2], ftuple[3]))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteFoster(values)

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        an_id.delete(0, END)
        cust_id.delete(0, END)
        fost_date.delete(0, END)
        d_date.delete(0, END)

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        an_id.insert(0, values[0])
        cust_id.insert(0, values[1])
        fost_date.insert(0, values[2])
        d_date.insert(0, values[3])

    
    def update_record():

        def sqDeleteFoster(ftuple):
            cur.execute("DELETE FROM FOSTER WHERE AN_ID=? AND CUST_ID=? AND FOST_DATE=? AND DUE_DATE=?;",(ftuple[0], ftuple[1], ftuple[2], ftuple[3]))
            con.commit()

        def sqInsertFoster(an_id,cust_id,fost_date,due_date):
            cur.execute("INSERT INTO Foster VALUES(?,?,?,?);",(an_id,cust_id,fost_date,due_date))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(an_id.get(), cust_id.get(), fost_date.get(), d_date.get()))
            sqDeleteFoster(values)
            values = tree.item(selected, 'values')
            sqInsertFoster(an_id.get(), cust_id.get(), fost_date.get(), d_date.get())
            

            # Clear entry boxes
            an_id.delete(0, END)
            cust_id.delete(0, END)
            fost_date.delete(0, END)
            d_date.delete(0, END)

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
    
   