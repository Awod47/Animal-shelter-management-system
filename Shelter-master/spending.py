import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter.font import nametofont
from tkinter import messagebox, ttk

def openSpending():
    root_sp = Toplevel()
    root_sp.title("Spending")
    root_sp.minsize(width=400,height=400)
    root_sp.geometry("1920x1800")

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
    label = ttk.Label(root_sp, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_sp,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Spending data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_sp,text="Add Spending",bg='black', fg='white', command=registerSpending)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_sp,text="Remove Spending",bg='black', fg='white', command=removeSpending)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_sp,text="View Spendings",bg='black', fg='white', command=viewSpendings)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    root_sp.mainloop()


def registerSpending():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Add volunteer")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    SpendingTable = "spending" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Spending", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Donor ID
    lb2 = Label(labelFrame,text="Donor ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    don_id = Entry(labelFrame)
    don_id.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # resource
    lb3 = Label(labelFrame,text="Resource : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    resource = Entry(labelFrame)
    resource.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # amount
    lb4 = Label(labelFrame,text="Amount : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    amount = Entry(labelFrame)
    amount.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # time
    lb5 = Label(labelFrame,text="Time (hh:mm:ss): ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.6, relheight=0.08)
        
    time = Entry(labelFrame)
    time.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    # date
    lb6 = Label(labelFrame,text="Date (yyyy-mm-dd): ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.7, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)
    
    def sqInsertSpending(an_id,donor_id,resource,amount,time,sp_date):
        cur.execute("INSERT INTO SPENDING VALUES(?,?,?,?,?);",(an_id,donor_id,resource,amount,time,sp_date))
        con.commit()

    def AddSpending():
        animal_id = an_id.get()
        donor_id = don_id.get()
        spend_resource = resource.get()
        spend_amount = amount.get()
        spend_time = time.get()
        spend_date = date.get()

        # insertSpending = "insert into "+SpendingTable +" values('"+animal_id+"', '"+donor_id+"', '"+spend_resource+"' , '"+spend_amount+"', '"+spend_time+"', '"+spend_date+"');"
        try:
            # cur.execute(insertSpending)
            # con.commit()
            sqInsertSpending(animal_id, donor_id, spend_resource, spend_amount, spend_time, spend_date)
            messagebox.showinfo('Success', "Spending reported")
        except:
            messagebox.showerror('Error', "Something went wrong")
        
        print(animal_id)
        print(donor_id)
        print(spend_resource)
        print(spend_amount)
        print(spend_time)
        print(spend_date)
        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=AddSpending)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

    

def removeSpending():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove Spending")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    VolunteerTable = "volunteer"


    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Volunteer", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Donor ID
    lb2 = Label(labelFrame,text="Donor ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    don_id = Entry(labelFrame)
    don_id.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame,text="Resouce : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    resource = Entry(labelFrame)
    resource.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # amount
    lb4 = Label(labelFrame,text="Amount : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    amount = Entry(labelFrame)
    amount.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # time
    lb5 = Label(labelFrame,text="Time (hh:mm:ss): ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.6, relheight=0.08)
        
    time = Entry(labelFrame)
    time.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    # date
    lb6 = Label(labelFrame,text="Date (yyyy-mm-dd): ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.7, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)


    def sqDeleteSpending(an_id, don_id, resource, amount, time, sp_date):
        cur.execute("DELETE FROM SPENDING WHERE AN_ID =? AND DONOR_ID=? AND AMOUNT=? AND TIME=? AND SP_DATE=?;",(an_id, don_id, resource, amount, time, sp_date))
        con.commit()

    def deleteSpending():
        animal_id = an_id.get()
        donor_id = don_id.get()
        spend_resource = resource.get()
        spend_amount = amount.get()
        spend_time = time.get()
        spend_date = date.get()

        try:
            sqDeleteSpending(animal_id, donor_id, spend_resource, spend_amount, spend_time, spend_date)
            messagebox.showinfo("Success", "Volunteer record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        an_id.delete(0, END)
        don_id.delete(0, END)
        resource.delete(0, END)
        amount.delete(0, END)
        time.delete(0, END)
        date.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteSpending)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


def viewSpendings():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Spendings")
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

        def sqSearchSpending(key):
            cur.execute("SELECT * FROM SPENDING WHERE AN_ID LIKE ? OR DONOR_ID LIKE ? OR AMOUNT LIKE ? OR TIME LIKE ? OR SP_DATE LIKE ?;",(key,key,key,key,key))
            splist=cur.fetchall()
            return splist


        def search_records():
            lookup_record = search_entry.get()
            search.destroy()
            
            for record in tree.get_children():
                tree.delete(record)
            
            try:
                con = sqlite3.connect("shelter.db")
                cur = con.cursor()
                cur.execute("PRAGMA foreign_keys = ON;")
            except Exception as e:
                print("error during connection: "+str(e))

            records = sqSearchSpending(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4], r[5]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)


    records = cur.execute("SELECT * FROM spending")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("an_id", "donor_id", "resource", "amount", "time", "sp_date")
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

    nametofont("TkDefaultFont").configure(size=13)

    tree.column("an_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("donor_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("resource", width=150, minwidth=50, anchor=CENTER)
    tree.column("amount", width=250, minwidth=50, anchor=CENTER)
    tree.column("time", width=200, minwidth=50, anchor=CENTER)
    tree.column("sp_date", width=200, minwidth=50, anchor=CENTER)

    tree.heading("an_id", text="Animal Id", anchor=CENTER)
    tree.heading("donor_id", text="Donor ID", anchor=CENTER)
    tree.heading("resource", text="Resource", anchor=CENTER)
    tree.heading("amount", text="Amount", anchor=CENTER)
    tree.heading("time", text="Time", anchor=CENTER)
    tree.heading("sp_date", text="Date", anchor=CENTER)

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4], r[5]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels
    lb1 = Label(add_frame, text="Animal ID")
    lb1.grid(row=0, column=0,  padx=95, pady=10)

    lb2 = Label(add_frame, text="Donor ID")
    lb2.grid(row=0, column=1,  padx=95, pady=10)

    lb3 = Label(add_frame, text="Resource")
    lb3.grid(row=0, column=2, padx=95, pady=10)

    lb4 = Label(add_frame, text="Amount")
    lb4.grid(row=0, column=3, padx=95, pady=10)

    lb5 = Label(add_frame, text="time")
    lb5.grid(row=0, column=4, padx=95, pady=10)

    lb6 = Label(add_frame, text="Date")
    lb6.grid(row=0, column=5, padx=95, pady=10)

    lb1.config(font=('Times New Roman',13))
    lb2.config(font=('Times New Roman',13))
    lb3.config(font=('Times New Roman',13))
    lb4.config(font=('Times New Roman',13))
    lb5.config(font=('Times New Roman',13))
    lb6.config(font=('Times New Roman',13))


    #Entry boxes
    an_id = Entry(add_frame)
    an_id.grid(row=1, column=0)

    don_id = Entry(add_frame)
    don_id.grid(row=1, column=1)

    resource = Entry(add_frame)
    resource.grid(row=1, column=2)

    amount = Entry(add_frame)
    amount.grid(row=1, column=3)

    time = Entry(add_frame)
    time.grid(row=1, column=4)

    sp_date = Entry(add_frame)
    sp_date.grid(row=1, column=5)


    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertSpending(an_id,donor_id,resource,amount,time,sp_date):
            cur.execute("INSERT INTO SPENDING VALUES(?,?,?,?,?,?);",(an_id,donor_id,resource,amount,time,sp_date))
            con.commit()

        try:
            sqInsertSpending(an_id.get(), don_id.get(), resource.get(), amount.get(), time.get(), sp_date.get())
            tree.insert(parent='', index='end', text="", values=(an_id.get(), don_id.get(), resource.get(), amount.get(), time.get(), sp_date.get()))
           
            # Clear the boxes
            an_id.delete(0, END)
            don_id.delete(0, END)
            resource.delete(0, END)
            amount.delete(0, END)
            time.delete(0, END)
            sp_date.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteSpending(sptuple):
            cur.execute("DELETE FROM SPENDING WHERE AN_ID =? AND DONOR_ID=? AND RESOURCE=? AND AMOUNT=? AND TIME=? AND SP_DATE=?;",(sptuple[0], sptuple[1], sptuple[2], sptuple[3], sptuple[4], sptuple[5]))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteSpending(values)

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        an_id.delete(0, END)
        don_id.delete(0, END)
        resource.delete(0, END)
        amount.delete(0, END)
        time.delete(0, END)
        sp_date.delete(0, END)

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        an_id.insert(0, values[0])
        don_id.insert(0, values[1])
        resource.insert(0, values[2])
        amount.insert(0, values[3])
        time.insert(0, values[4])
        sp_date.insert(0, values[5])

    
    def update_record():

        def sqDeleteSpending(sptuple):
            cur.execute("DELETE FROM SPENDING WHERE AN_ID =? AND DONOR_ID=? AND RESOURCE=? AND AMOUNT=? AND TIME=? AND SP_DATE=?;",(sptuple[0], sptuple[1], sptuple[2], sptuple[3], sptuple[4], sptuple[5]))
            con.commit()

        def sqInsertSpending(an_id,donor_id,resource,amount,time,sp_date):
            cur.execute("INSERT INTO SPENDING VALUES(?,?,?,?,?,?);",(an_id,donor_id,resource,amount,time,sp_date))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(an_id.get(),don_id.get(), resource.get(), amount.get(), time.get(), sp_date.get()))
            sqDeleteSpending(values)
            values = tree.item(selected, 'values')
            sqInsertSpending(an_id.get(),don_id.get(), resource.get(), amount.get(), time.get(), sp_date.get())
            

            # Clear entry boxes
            an_id.delete(0, END)
            don_id.delete(0, END)
            resource.delete(0, END)
            amount.delete(0, END)
            time.delete(0, END)
            sp_date.delete(0, END)

        except:
            messagebox.showerror("Error", "Something went wrong", parent=root_new)

        
    button_frame = LabelFrame(root_new, bg = "orange", text = "Commands")
    button_frame.pack(fill= "x", expand = "yes", padx = 20)

    #add new record
    add_button = Button(button_frame, text="Add Record", command=add_record)
    add_button.grid(row=0, column=0, padx=140, pady=10)

    #select record to edit
    edit_button = Button(button_frame, text="Edit Record", command=edit_record)
    edit_button.grid(row=0, column=1, padx=140, pady=10)

    #update selected
    update_button = Button(button_frame, text="Save Record", command=update_record)
    update_button.grid(row=0, column=2, padx=140, pady=10)

    # Remove Selected
    remove_one = Button(button_frame, text="Remove Selected Record", command=remove_record)
    remove_one.grid(row=0, column=3, padx=140, pady=10)

    add_button.config(font=('Times New Roman',13))
    edit_button.config(font=('Times New Roman',13))
    update_button.config(font=('Times New Roman',13))
    remove_one.config(font=('Times New Roman',13))

    root_new.mainloop()
    
   


