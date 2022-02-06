import sqlite3
from tkinter import *
from tkinter import font
from PIL import ImageTk,Image 
from tkinter.font import nametofont
from tkinter import messagebox, ttk

from spending import viewSpendings

def openDonations():
    root_don = Toplevel()
    root_don.title("Donations")
    root_don.minsize(width=400,height=400)
    root_don.geometry("1920x1800")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('shelter-donation.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_don, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_don,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Donations Menu", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_don,text="Add Donation",bg='black', fg='white', command=registerDonation)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_don,text="Remove Donation",bg='black', fg='white', command=removeDonation)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_don,text="View Donations",bg='black', fg='white', command=viewDonations)
    btn3.place(relx=0.37,rely=0.5, relwidth=0.25,relheight=0.05)

    btn7 = Button(root_don,text="Spendings records",bg='black', fg='white', command=viewSpendings)
    btn7.place(relx=0.37,rely=0.70, relwidth=0.25,relheight=0.05)

    headingLabel.config(font=('Times New Roman',22))
    btn1.config(font=('Times New Roman',15))
    btn2.config(font=('Times New Roman',15))
    btn3.config(font=('Times New Roman',15))
    btn7.config(font=('Times New Roman',15))

    root_don.mainloop()



def registerDonation():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Add Donation")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    DonationsTable = "donations" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Donations", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # # Donor ID
    # lb1 = Label(labelFrame,text="Donor ID : ", bg='black', fg='white')
    # lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    # don_id = Entry(labelFrame)
    # don_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # resource
    lb2 = Label(labelFrame,text="Resource donated : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    resource = Entry(labelFrame)
    resource.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # amount
    lb3 = Label(labelFrame,text="Amount donated : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    amount = Entry(labelFrame)
    amount.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # date
    lb4 = Label(labelFrame,text="date donated (yyyy-mm-dd): ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    don_date = Entry(labelFrame)
    don_date.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # availability
    lb4 = Label(labelFrame,text="Resource availability : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.6, relheight=0.08)
        
    availability = Entry(labelFrame)
    availability.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   
    def sqInsertDonations(resource,amount,don_date,availability):
        cur.execute("SELECT DONOR_ID from DONATIONS")
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
            newidstr = "d000" + str(newid)
        elif newid<100 :
            newidstr = "d00" + str(newid)
        elif newid<1000 :
            newidstr = "d0" + str(newid)
        else :
            newidstr = "d" +str(newid)
        cur.execute("INSERT INTO DONATIONS VALUES(?,?,?,?,?);",(newidstr,resource,amount,don_date,availability))
        con.commit()
        return newidstr

    def AddDonation():
        #donor_id = don_id.get()
        donor_resource = resource.get()
        resource_amount = amount.get()
        donor_date = don_date.get()
        resource_availability = availability.get()

        #insertDonation = "insert into "+DonationsTable +" values('"+donor_id+"', '"+donor_resource+"', '"+resource_amount+"' , '"+donor_date+"', '"+resource_availability+"');"
        try:
            #cur.execute(insertDonation)
            #con.commit()
            donor_id = sqInsertDonations(donor_resource, resource_amount, donor_date, resource_availability)
            messagebox.showinfo('Success', "Donation added")
        except:
            messagebox.showerror('Error', "Something went wrong")
        
        print(donor_id)
        print(donor_resource)
        print(resource_amount)
        print(donor_date)
        print(resource_availability)
        root.destroy()


    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=AddDonation)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',15))
    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))
    
    root.mainloop()




def removeDonation():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove Donation")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    DonationsTable = "donations"


    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Donation", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="Donor ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    don_id = Entry(labelFrame)
    don_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    def sqDeleteDonations(did):
        cur.execute("DELETE FROM SPENDING WHERE AN_ID IS NULL AND DONOR_ID=?;",(did,))
        cur.execute("DELETE FROM DONATIONS WHERE DONOR_ID=?;",(did,))
        con.commit()

    def deleteDonation():
        donor_id = don_id.get()

        try:
            sqDeleteDonations(donor_id)
            messagebox.showinfo("Success", "Donation record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        print(donor_id)
        don_id.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteDonation)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',15))
    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))
    
    root.mainloop()


def viewDonations():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Donations")
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

        def sqSearchDonations(key):
            cur.execute("SELECT * FROM DONATIONS WHERE DONOR_ID LIKE ? OR RESOURCE LIKE ? OR AMOUNT LIKE ? OR DON_DATE LIKE ? OR AVAILABILITY LIKE ?;",(key,key,key,key,key))
            dlist=cur.fetchall()
            return dlist


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

            records = sqSearchDonations(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)

    records = cur.execute("SELECT * FROM donations")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("donor_id", "resource", "amount", "don_date", "availability")
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


    tree.column("donor_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("resource", width=200, minwidth=50, anchor=CENTER)
    tree.column("amount", width=150, minwidth=50, anchor=CENTER)
    tree.column("don_date", width=250, minwidth=50, anchor=CENTER)
    tree.column("availability", width=200, minwidth=50, anchor=CENTER)

    tree.heading("donor_id", text="Donor Id", anchor=CENTER)
    tree.heading("resource", text="Resource", anchor=CENTER)
    tree.heading("amount", text="Amount", anchor=CENTER)
    tree.heading("don_date", text="Donation Date", anchor=CENTER)
    tree.heading("availability", text="Avialability", anchor=CENTER)

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels

    lb2 = Label(add_frame, text="Resource")
    lb2.grid(row=0, column=0,  padx=145, pady=10)

    lb3 = Label(add_frame, text="Amount")
    lb3.grid(row=0, column=1, padx=145, pady=10)

    lb4 = Label(add_frame, text="Donation Date")
    lb4.grid(row=0, column=2, padx=145, pady=10)

    lb5 = Label(add_frame, text="Availability")
    lb5.grid(row=0, column=3, padx=145, pady=10)

    lb2.config(font=('Times New Roman',15))
    lb3.config(font=('Times New Roman',15))
    lb4.config(font=('Times New Roman',15))
    lb5.config(font=('Times New Roman',15))

    #Entry boxes

    don_resource = Entry(add_frame)
    don_resource.grid(row=1, column=0)

    don_amount = Entry(add_frame)
    don_amount.grid(row=1, column=1)

    don_date = Entry(add_frame)
    don_date.grid(row=1, column=2)

    availability= Entry(add_frame)
    availability.grid(row=1, column=3)


    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertDonations(resource,amount,don_date,availability):
            cur.execute("SELECT DONOR_ID from DONATIONS")
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
                newidstr = "d000" + str(newid)
            elif newid<100 :
                newidstr = "d00" + str(newid)
            elif newid<1000 :
                newidstr = "d0" + str(newid)
            else :
                newidstr = "d" +str(newid)
            cur.execute("INSERT INTO DONATIONS VALUES(?,?,?,?,?);",(newidstr,resource,amount,don_date,availability))
            con.commit()
            return newidstr

        try:
            donor_id = sqInsertDonations(don_resource.get(), don_amount.get(), don_date.get(), availability.get())
            tree.insert(parent='', index='end', text="", values=(donor_id,don_resource.get(), don_amount.get(), don_date.get(), availability.get()))
           
            # Clear the boxes
            don_resource.delete(0, END)
            don_amount.delete(0, END)
            don_date.delete(0, END)
            availability.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteDonations(did):
            cur.execute("DELETE FROM SPENDING WHERE DONOR_ID=?;",(did,))
            cur.execute("DELETE FROM DONATIONS WHERE DONOR_ID=?;",(did,))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteDonations(values[0])

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        don_resource.delete(0, END)
        don_amount.delete(0, END)
        don_date.delete(0, END)
        availability.delete(0, END)
        

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        don_resource.insert(0, values[1])
        don_amount.insert(0, values[2])
        don_date.insert(0, values[3])
        availability.insert(0, values[4])

    
    def update_record():

        def sqModifyDonations(dtuple):
            cur.execute("UPDATE DONATIONS SET RESOURCE=?, AMOUNT=?, DON_DATE=?, AVAILABILITY=? WHERE DONOR_ID=?;",(dtuple[1],dtuple[2],dtuple[3],dtuple[4],dtuple[0]))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(values[0], don_resource.get(), don_amount.get(), don_date.get(), availability.get()))
            values = tree.item(selected, 'values')
            sqModifyDonations(values)

            # Clear entry boxes
            don_resource.delete(0, END)
            don_amount.delete(0, END)
            don_date.delete(0, END)
            availability.delete(0, END)

        except:
            messagebox.showerror("Error", "Something went wrong", parent=root_new)

        
    button_frame = LabelFrame(root_new, bg = "orange", text = "Commands")
    button_frame.pack(fill= "x", expand = "yes", padx = 20)

    #add new record
    add_button = Button(button_frame, text="Add Record", command=add_record)
    add_button.grid(row=0, column=0, padx=125, pady=10)

    #select record to edit
    edit_button = Button(button_frame, text="Edit Record", command=edit_record)
    edit_button.grid(row=0, column=1, padx=125, pady=10)

    #update selected
    update_button = Button(button_frame, text="Save Record", command=update_record)
    update_button.grid(row=0, column=2, padx=125, pady=10)

    # Remove Selected
    remove_one = Button(button_frame, text="Remove Selected Record", command=remove_record)
    remove_one.grid(row=0, column=3, padx=125, pady=10)

    add_button.config(font=('Times New Roman',15))
    edit_button.config(font=('Times New Roman',15))
    update_button.config(font=('Times New Roman',15))
    remove_one.config(font=('Times New Roman',15))

    root_new.mainloop()
    
   

