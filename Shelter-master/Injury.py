import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter.font import nametofont
from tkinter import messagebox, ttk

def openInjury():
    root_in = Toplevel()
    root_in.title("Injury")
    root_in.minsize(width=400,height=400)
    root_in.geometry("1920x1800")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('shelter-injury.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_in, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_in,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Inury data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_in,text="Register Volunteer Timings",bg='black', fg='white', command=reportInjury)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_in,text="Remove Info",bg='black', fg='white', command=removeInjury)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_in,text="View Volunteer Timings",bg='black', fg='white', command=viewInjury)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    root_in.mainloop()


def reportInjury():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Report Injury")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    InjuryTable = 'injury' # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Injury", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Date
    lb2 = Label(labelFrame,text="Date : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Body Part
    lb3 = Label(labelFrame,text="Body Part : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    body_part = Entry(labelFrame)
    body_part.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # Injury Status
    lb4 = Label(labelFrame,text="Injury Status (cured/ prevails) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    status = Entry(labelFrame)
    status.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    def sqInsertInjury(an_id,in_date,body_part,injury_status):
        cur.execute("INSERT INTO Injury VALUES(?,?,?,?);",(an_id,in_date,body_part,injury_status))
        con.commit()


    def AddInjury():
        animal_id = an_id.get()
        injury_date = date.get()
        injury_bodypart = body_part.get()
        injury_status = status.get()

        #insertSpending = "insert into "+InjuryTable +" values('"+animal_id+"', '"+injury_date+"', '"+injury_bodypart+"' , '"+injury_status+"');"
        try:
            # cur.execute(insertSpending)
            # con.commit()
            sqInsertInjury(animal_id, injury_date, injury_bodypart, injury_status)
            messagebox.showinfo('Success', "Spending reported")
        except:
            messagebox.showerror('Error', "Something went wrong")
        
        print(animal_id)
        print(injury_date)
        print(injury_bodypart)
        print(injury_status)
        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=AddInjury)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def removeInjury():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove Injury record")
    root.minsize(width=400,height=400)
    root.geometry("1920x1800")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Volunteer Timings record", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Volunteer ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Animal ID
    lb2 = Label(labelFrame,text="Date : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

    # start time
    lb3 = Label(labelFrame,text="Body Part: ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    bodypart = Entry(labelFrame)
    bodypart.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # end time
    lb4 = Label(labelFrame,text="Status : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    status = Entry(labelFrame)
    status.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)


    def sqDeleteInjury(an_id, date, bodypart, status):
        cur.execute("DELETE FROM INJURY WHERE AN_ID=? AND IN_DATE=? AND BODY_PART=? AND INJURY_STATUS=?",an_id, date, bodypart, status)
        con.commit()

    def deleteInjury():
        animal_id = an_id.get()
        in_date = date.get()
        in_bodypart = bodypart.get()
        in_status = status.get()

        try:
            sqDeleteInjury(animal_id, in_date, in_bodypart, in_status)
            messagebox.showinfo("Success", "Volunteer record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        an_id.delete(0, END)
        date.delete(0, END)
        bodypart.delete(0, END)
        status.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteInjury)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


def viewInjury():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Injury record")
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

        def sqSearchInjury(key):
            cur.execute("SELECT * FROM INJURY WHERE AN_ID LIKE ? OR IN_dATE LIKE ? OR BODY_PART LIKE ? OR INJURY_STATUS LIKE ?;",(key,key,key,key))
            inlist=cur.fetchall()
            return inlist 


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

            records = sqSearchInjury(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)


    records = cur.execute("SELECT * FROM injury")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("an_id", "in_date", "body_part", "injury_status")
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
    tree.column("in_date", width=150, minwidth=50, anchor=CENTER)
    tree.column("body_part", width=250, minwidth=50, anchor=CENTER)
    tree.column("injury_status", width=200, minwidth=50, anchor=CENTER)

    tree.heading("an_id", text="Animal Id", anchor=CENTER)
    tree.heading("in_date", text="Date", anchor=CENTER)
    tree.heading("body_part", text="Body Part", anchor=CENTER)
    tree.heading("injury_status", text="Injury Status", anchor=CENTER)

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

    lb2 = Label(add_frame, text="Date")
    lb2.grid(row=0, column=1,  padx=150, pady=10)

    lb3 = Label(add_frame, text="Body Part")
    lb3.grid(row=0, column=2, padx=150, pady=10)

    lb4 = Label(add_frame, text="Injury Status")
    lb4.grid(row=0, column=3, padx=150, pady=10)

    lb1.config(font=('Times New Roman',13))
    lb2.config(font=('Times New Roman',13))
    lb3.config(font=('Times New Roman',13))
    lb4.config(font=('Times New Roman',13))

    #Entry boxes
    an_id = Entry(add_frame)
    an_id.grid(row=1, column=0)

    date = Entry(add_frame)
    date.grid(row=1, column=1)

    bodypart = Entry(add_frame)
    bodypart.grid(row=1, column=2)

    status = Entry(add_frame)
    status.grid(row=1, column=3)



    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertInjury(an_id,in_date,body_part,injury_status):
            cur.execute("INSERT INTO Injury VALUES(?,?,?,?);",(an_id,in_date,body_part,injury_status))
            con.commit()    

        try:
            sqInsertInjury(an_id.get(), date.get(), bodypart.get(), status.get())
            tree.insert(parent='', index='end', text="", values=(an_id.get(), date.get(), bodypart.get(), status.get()))
           
            # Clear the boxes
            an_id.delete(0, END)
            date.delete(0, END)
            bodypart.delete(0, END)
            status.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteInjury(ituple):
            cur.execute("DELETE FROM INJURY WHERE AN_ID=? AND IN_DATE=? AND BODY_PART=? AND INJURY_STATUS=?",(ituple[0], ituple[1], ituple[2], ituple[3]))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteInjury(values)

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        an_id.delete(0, END)
        date.delete(0, END)
        bodypart.delete(0, END)
        status.delete(0, END)

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        an_id.insert(0, values[0])
        date.insert(0, values[1])
        bodypart.insert(0, values[2])
        status.insert(0, values[3])

    
    def update_record():

        def sqDeleteInjury(ituple):
            cur.execute("DELETE FROM INJURY WHERE AN_ID=? AND IN_DATE=? AND BODY_PART=? AND INJURY_STATUS=?",(ituple[0], ituple[1], ituple[2], ituple[3]))
            con.commit()

        def sqInsertInjury(an_id,in_date,body_part,injury_status):
            cur.execute("INSERT INTO Injury VALUES(?,?,?,?);",(an_id,in_date,body_part,injury_status))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(an_id.get(), date.get(), bodypart.get(), status.get()))
            sqDeleteInjury(values)
            values = tree.item(selected, 'values')
            sqInsertInjury(an_id.get(), date.get(), bodypart.get(), status.get())
            

            # Clear entry boxes
            an_id.delete(0, END)
            date.delete(0, END)
            bodypart.delete(0, END)
            status.delete(0, END)

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
    
   
