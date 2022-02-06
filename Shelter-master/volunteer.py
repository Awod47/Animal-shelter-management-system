import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk
from tkinter.font import nametofont
from volunteer_timings import *
from takes_care import *

def openVolunteer():
    root_vol = Toplevel()
    root_vol.title("Volunteers")
    root_vol.minsize(width=400,height=400)
    root_vol.geometry("1920x1800")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('shelter-care.jpeg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_vol, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_vol,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Volunteer Menu", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_vol,text="Add Volunteer",bg='black', fg='white', command=registerVolunteer)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_vol,text="Remove Volunteer",bg='black', fg='white', command=removeVolunteer)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_vol,text="View Volunteers",bg='black', fg='white', command=viewVolunteers)
    btn3.place(relx=0.37,rely=0.5, relwidth=0.25,relheight=0.05)

    btn7 = Button(root_vol,text="Timings records",bg='black', fg='white', command=viewVolTimings)
    btn7.place(relx=0.05,rely=0.70, relwidth=0.25,relheight=0.05)

    btn8 = Button(root_vol,text="Takes care records",bg='black', fg='white', command=viewCare)
    btn8.place(relx=0.70,rely=0.70, relwidth=0.25,relheight=0.05)

    headingLabel.config(font=('Times New Roman',22))
    btn1.config(font=('Times New Roman',13))
    btn2.config(font=('Times New Roman',13))
    btn3.config(font=('Times New Roman',13))
    btn7.config(font=('Times New Roman',13))
    btn8.config(font=('Times New Roman',13))

    root_vol.mainloop()



def registerVolunteer():
    
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

    VolunteerTable = "volunteer" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Volunteers", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # volunteer ID
    # lb1 = Label(labelFrame,text="Volunteer ID : ", bg='black', fg='white')
    # lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    # vol_id = Entry(labelFrame)
    # vol_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # volunteer name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    vol_name = Entry(labelFrame)
    vol_name.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # dob
    lb3 = Label(labelFrame,text="date of birth (yyyy-mm-dd) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    vol_dob = Entry(labelFrame)
    vol_dob.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # phone
    lb4 = Label(labelFrame,text="phone : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    vol_phone = Entry(labelFrame)
    vol_phone.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # address
    lb4 = Label(labelFrame,text="Resident Address : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.6, relheight=0.08)
        
    vol_address = Entry(labelFrame)
    vol_address.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   
    def sqInsertVolunteer(vname,dob,phone,address):
        cur.execute("SELECT vol_id from Volunteer")
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
            newidstr = "v000" + str(newid)
        elif newid<100 :
            newidstr = "v00" + str(newid)
        elif newid<1000 :
            newidstr = "v0" + str(newid)
        else :
            newidstr = "v" +str(newid)
        cur.execute("INSERT INTO Volunteer VALUES(?,?,?,?,?);",(newidstr,vname,dob,phone,address))
        con.commit()
        return newidstr

    def AddVolunteer():
        #volunteer_id = vol_id.get()
        volunteer_name = vol_name.get()
        volunteer_dob = vol_dob.get()
        volunteer_phone = int(vol_phone.get())
        volunteer_address = vol_address.get()

        #insertVolunteer = "insert into "+VolunteerTable +" values('"+volunteer_id+"', '"+volunteer_name+"', '"+volunteer_dob+"' , '"+volunteer_phone+"', '"+volunteer_address+"');"
        try:
            # cur.execute(insertVolunteer)
            # con.commit()
            volunteer_id = sqInsertVolunteer(volunteer_name, volunteer_dob, volunteer_phone, volunteer_address)
            messagebox.showinfo('Success', "Volunteer added")
        except:
            messagebox.showerror('Error', "Something went wrong")
        
        print(volunteer_id)
        print(volunteer_name)
        print(volunteer_dob)
        print(volunteer_phone)
        print(volunteer_address)
        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#d1ccc0', fg='black',command=AddVolunteer)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',13))
    SubmitBtn.config(font=('Times New Roman',13))
    quitBtn.config(font=('Times New Roman',13))
    
    root.mainloop()

    


def removeVolunteer():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Remove volunteer")
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

    lb1 = Label(labelFrame,text="Volunteer ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    vol_id = Entry(labelFrame)
    vol_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    def sqDeleteVolunteer(vid):
        cur.execute("DELETE FROM TAKES_cARE WHERE AN_ID IS NULL AND VOL_ID=?;",(vid,))
        cur.execute("DELETE FROM VOLUNTEER WHERE VOL_ID=?;",(vid,))
        con.commit()

    def deleteVolunteer():
        volunteer_id = vol_id.get()

        try:
            sqDeleteVolunteer(volunteer_id)
            messagebox.showinfo("Success", "Volunteer record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        print(volunteer_id)
        vol_id.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteVolunteer)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',13))
    SubmitBtn.config(font=('Times New Roman',13))
    quitBtn.config(font=('Times New Roman',13))
    
    root.mainloop()

    

def viewVolunteers():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Volunteer")
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

        def sqSearchVolunteer(key):
            cur.execute("SELECT * FROM VOLUNTEER WHERE VOL_ID LIKE ? OR VOL_NAME LIKE ? OR VOL_DOB LIKE ? OR VOL_PHONE LIKE ? OR VOL_ADDRESS LIKE ?;",(key,key,key,key,key))
            vollist = cur.fetchall()
            return vollist


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

            records = sqSearchVolunteer(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)


    records = cur.execute("SELECT * FROM volunteer")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("vol_id", "vol_name", "vol_dob", "vol_phone", "vol_address")
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

    tree.column("vol_id", width=200, minwidth=50, anchor=CENTER)
    tree.column("vol_name", width=200, minwidth=50, anchor=CENTER)
    tree.column("vol_dob", width=250, minwidth=50, anchor=CENTER)
    tree.column("vol_phone", width=200, minwidth=50, anchor=CENTER)
    tree.column("vol_address", width=350, minwidth=50, anchor=CENTER)
    

    tree.heading("vol_id", text="Volunteer Id", anchor=CENTER)
    tree.heading("vol_name", text="Name", anchor=CENTER)
    tree.heading("vol_dob", text="Date of birth", anchor=CENTER)
    tree.heading("vol_phone", text="Phone Number", anchor=CENTER)
    tree.heading("vol_address", text="Home Address", anchor=CENTER)
    

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels

    lb2 = Label(add_frame, text="Name")
    lb2.grid(row=0, column=0, padx=160, pady=10)

    lb3 = Label(add_frame, text="Date of birth")
    lb3.grid(row=0, column=1, padx=160, pady=10)

    lb4 = Label(add_frame, text="Phone")
    lb4.grid(row=0, column=2, padx=160, pady=10)

    lb5 = Label(add_frame, text="Address")
    lb5.grid(row=0, column=3, padx=160, pady=10)

    lb2.config(font=('Times New Roman',13))
    lb3.config(font=('Times New Roman',13))
    lb4.config(font=('Times New Roman',13))
    lb5.config(font=('Times New Roman',13))

    #Entry boxes

    vol_name = Entry(add_frame)
    vol_name.grid(row=1, column=0)

    vol_dob = Entry(add_frame)
    vol_dob.grid(row=1, column=1)

    vol_phone = Entry(add_frame)
    vol_phone.grid(row=1, column=2)

    vol_address = Entry(add_frame)
    vol_address.grid(row=1, column=3)



    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertVolunteer(vname,dob,phone,address):
            cur.execute("SELECT vol_id from Volunteer")
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
                newidstr = "v000" + str(newid)
            elif newid<100 :
                newidstr = "v00" + str(newid)
            elif newid<1000 :
                newidstr = "v0" + str(newid)
            else :
                newidstr = "v" +str(newid)
            cur.execute("INSERT INTO Volunteer VALUES(?,?,?,?,?);",(newidstr,vname,dob,phone,address))
            con.commit()
            return newidstr

        try:
            volunteer_id = sqInsertVolunteer(vol_name.get(), vol_dob.get(), vol_phone.get(), vol_address.get())
            tree.insert(parent='', index='end', text="", values=(volunteer_id, vol_name.get(), vol_dob.get(), vol_phone.get(), vol_address.get()))
           
            # Clear the boxes
            vol_name.delete(0, END)
            vol_dob.delete(0, END)
            vol_phone.delete(0, END)
            vol_address.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteVolunteer(vid):
            cur.execute("DELETE FROM TAKES_cARE WHERE AN_ID IS NULL AND VOL_ID=?;",(vid,))
            cur.execute("DELETE FROM VOLUNTEER WHERE VOL_ID=?;",(vid,))
            cur.execute("DELETE FROM volunteer_timings WHERE vol_id=?;",(vid,))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteVolunteer(values[0])

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        vol_name.delete(0, END)
        vol_dob.delete(0, END)
        vol_phone.delete(0, END)
        vol_address.delete(0, END)
        
        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        vol_name.insert(0, values[1])
        vol_dob.insert(0, values[2])
        vol_phone.insert(0, values[3])
        vol_address.insert(0, values[4])

    
    def update_record():

        def sqModifyVolunteer(vtuple):
            cur.execute("UPDATE VOLUNTEER SET VOL_NAME=?,VOL_DOB=?,VOL_PHONE=?,VOL_ADDRESS=? WHERE VOL_ID=?;",(vtuple[1],vtuple[2],vtuple[3],vtuple[4],vtuple[0]))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(values[0], vol_name.get(), vol_dob.get(), vol_phone.get(), vol_address.get()))
            values = tree.item(selected, 'values')
            sqModifyVolunteer(values)

            # Clear entry boxes
            vol_name.delete(0, END)
            vol_dob.delete(0, END)
            vol_phone.delete(0, END)
            vol_address.delete(0, END)

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
    
   



