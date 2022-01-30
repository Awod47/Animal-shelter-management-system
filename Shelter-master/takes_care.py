import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openTakesCare():
    root_tc = Toplevel()
    root_tc.title("Animal")
    root_tc.minsize(width=400,height=400)
    root_tc.geometry("1920x1800")

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
    label = ttk.Label(root_tc, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_tc,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Care given data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_tc,text="Add Care Giver Info",bg='black', fg='white', command=registerCare)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_tc,text="Remove Info",bg='black', fg='white', command=removeCare)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_tc,text="View Care given",bg='black', fg='white', command=viewCare)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    root_tc.mainloop()

def registerCare():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Register Care given")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    TakesCareTable = "takes_care" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Volunteers", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

        
    # Volunteer ID
    lb2 = Label(labelFrame,text="Volunteer ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    vol_id = Entry(labelFrame)
    vol_id.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    
    # date
    lb3 = Label(labelFrame,text="date (yyyy-mm-dd) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # start time
    lb4 = Label(labelFrame,text="time (hh : mm) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    start_time = Entry(labelFrame)
    start_time.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # end time
    lb4 = Label(labelFrame,text="time finished (hh : mm) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.6, relheight=0.08)
        
    end_time = Entry(labelFrame)
    end_time.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    def sqInsertTakes_Care(vol_id,an_id,vol_date,tstart_time,tend_time):
        cur.execute("INSERT INTO TAKES_CARE VALUES(?,?,?,?,?);",(vol_id,an_id,vol_date,tstart_time,tend_time))
        con.commit()

    def AddTakescare():
        volunteer_id = vol_id.get()
        animal_id = an_id.get()
        tcDate = date.get()
        tcStartTime = start_time.get()
        tcEndTime = end_time.get()

        try:
            # cur.execute(insertVolunteer)
            # con.commit()
            sqInsertTakes_Care(volunteer_id, animal_id, tcDate, tcStartTime, tcEndTime)
            messagebox.showinfo('Success', "Care Taker Info added")
        except:
            messagebox.showerror('Error', "Something went wrong")
        
        print(volunteer_id)
        print(animal_id)
        print(tcDate)
        print(tcStartTime)
        print(tcEndTime)
        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=AddTakescare)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

    

def removeCare():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove Care Record")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Takes care record", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Volunteer ID
    lb1 = Label(labelFrame,text="Volunteer ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    vol_id = Entry(labelFrame)
    vol_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Animal ID
    lb2 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

    # date
    lb3 = Label(labelFrame,text="Date : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # start time
    lb4 = Label(labelFrame,text="Start Time (hh : mm): ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    startTime = Entry(labelFrame)
    startTime.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # end time
    lb5 = Label(labelFrame,text="End Time (hh : mm): ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.6, relheight=0.08)
        
    endTime = Entry(labelFrame)
    endTime.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)



    def sqDeleteTakes_Care(vol_id, an_id, tc_date, TcStartTime, tcEndTime):
        cur.execute("DELETE FROM TAKES_CARE WHERE VOL_ID=? AND AN_ID=? AND TC_DATE=? AND TSTART_TIME=? AND TEND_TIME=?;",(vol_id, an_id, tc_date, TcStartTime, tcEndTime))
        con.commit()

    def deleteTakesCare():
        volunteer_id = vol_id.get()
        animal_id = an_id.get()
        tc_date = date.get()
        tcStartTime = startTime.get()
        tcEndTime = endTime.get()

        try:
            sqDeleteTakes_Care(volunteer_id, animal_id, tc_date, tcStartTime, tcEndTime)
            messagebox.showinfo("Success", "Volunteer record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        vol_id.delete(0, END)
        an_id.delete(0, END)
        date.delete(0, END)
        startTime.delete(0, END)
        endTime.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteTakesCare)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


def viewCare():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Takes Care")
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

        def sqSearchTakes_Care(key):
            cur.execute("SELECT * FROM TAKES_CARE WHERE VOL_ID LIKE ? OR AN_ID LIKE ? OR TC_DATE LIKE ? OR TCSTART_TIME LIKE ? OR TCEND_TIME LIKE ?;",(key,key,key,key,key))
            tclist = cur.fetchall()
            return tclist       


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

            records = sqSearchTakes_Care(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)


    records = cur.execute("SELECT * FROM takes_care")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("vol_id", "an_id", "tc_date", "tcStart_time", "tcEnd_time")
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


    tree.column("vol_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("an_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("tc_date", width=150, minwidth=50, anchor=CENTER)
    tree.column("tcStart_time", width=250, minwidth=50, anchor=CENTER)
    tree.column("tcEnd_time", width=200, minwidth=50, anchor=CENTER)

    tree.heading("vol_id", text="Volunteer Id", anchor=CENTER)
    tree.heading("an_id", text="Animal ID", anchor=CENTER)
    tree.heading("tc_date", text="Date", anchor=CENTER)
    tree.heading("tcStart_time", text="Start Time", anchor=CENTER)
    tree.heading("tcEnd_time", text="End Time", anchor=CENTER)

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels
    lb1 = Label(add_frame, text="Volunteer ID")
    lb1.grid(row=0, column=0,  padx=120, pady=10)

    lb2 = Label(add_frame, text="Animal ID")
    lb2.grid(row=0, column=1,  padx=120, pady=10)

    lb3 = Label(add_frame, text="Date")
    lb3.grid(row=0, column=2, padx=120, pady=10)

    lb4 = Label(add_frame, text="Start Time")
    lb4.grid(row=0, column=3, padx=120, pady=10)

    lb5 = Label(add_frame, text="End Time")
    lb5.grid(row=0, column=4, padx=120, pady=10)


    #Entry boxes
    vol_id = Entry(add_frame)
    vol_id.grid(row=1, column=0)

    an_id = Entry(add_frame)
    an_id.grid(row=1, column=1)

    tc_date = Entry(add_frame)
    tc_date.grid(row=1, column=2)

    startTime = Entry(add_frame)
    startTime.grid(row=1, column=3)

    endTime = Entry(add_frame)
    endTime.grid(row=1, column=4)



    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertTakes_Care(vol_id,an_id,tc_date,tstart_time,tend_time):
            cur.execute("INSERT INTO TAKES_CARE VALUES(?,?,?,?,?);",(vol_id,an_id,tc_date,tstart_time,tend_time))
            con.commit()

        try:
            sqInsertTakes_Care(vol_id.get(), an_id.get(), tc_date.get(), startTime.get(), endTime.get())
            tree.insert(parent='', index='end', text="", values=(vol_id.get(), an_id.get(), tc_date.get(), startTime.get(), endTime.get()))
           
            # Clear the boxes
            vol_id.delete(0, END)
            an_id.delete(0, END)
            tc_date.delete(0, END)
            startTime.delete(0, END)
            endTime.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteTakes_Care(tctuple):
            cur.execute("DELETE FROM TAKES_CARE WHERE VOL_ID=? AND AN_ID=? AND TC_DATE=? AND TCSTART_TIME=? AND TCEND_TIME=?;",(tctuple[0], tctuple[1], tctuple[2], tctuple[3], tctuple[4]))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteTakes_Care(values)

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        vol_id.delete(0, END)
        an_id.delete(0, END)
        tc_date.delete(0, END)
        startTime.delete(0, END)
        endTime.delete(0, END)

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        vol_id.insert(0, values[0])
        an_id.insert(0, values[1])
        tc_date.insert(0, values[2])
        startTime.insert(0, values[3])
        endTime.insert(0, values[4])

    
    def update_record():

        def sqDeleteTakes_Care(tctuple):
            cur.execute("DELETE FROM TAKES_CARE WHERE VOL_ID=? AND AN_ID=? AND TC_DATE=? AND TCSTART_TIME=? AND TCEND_TIME=?;",(tctuple[0], tctuple[1], tctuple[2], tctuple[3], tctuple[4]))
            con.commit()

        def sqInsertTakes_Care(vol_id,an_id,tc_date,tstart_time,tend_time):
            cur.execute("INSERT INTO TAKES_CARE VALUES(?,?,?,?,?);",(vol_id,an_id,tc_date,tstart_time,tend_time))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(vol_id.get(),an_id.get(), tc_date.get(), startTime.get(), endTime.get()))
            sqDeleteTakes_Care(values)
            values = tree.item(selected, 'values')
            sqInsertTakes_Care(vol_id.get(),an_id.get(), tc_date.get(), startTime.get(), endTime.get())
            

            # Clear entry boxes
            vol_id.delete(0, END)
            an_id.delete(0, END)
            tc_date.delete(0, END)
            startTime.delete(0, END)
            endTime.delete(0, END)

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
    
   



