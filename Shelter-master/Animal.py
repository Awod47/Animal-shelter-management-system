import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk
from tkinter.font import nametofont
from Adopt import *
from Injury import *
from Foster import *
from spending import *



def openAnimal():
    root_an = Toplevel()
    root_an.title("Animal")
    root_an.minsize(width=400,height=400)
    root_an.geometry("1920x1800")


    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('shelter-animal.jfif')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_an, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_an,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Animal Menu", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_an,text="Add Animal",bg='black', fg='white', command=registerAnimal)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_an,text="Remove",bg='black', fg='white', command=removeAnimal)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_an,text="View Animals",bg='black', fg='white', command=viewAnimal)
    btn3.place(relx=0.37,rely=0.5, relwidth=0.25,relheight=0.05)

    btn5 = Button(root_an,text="Injury record",bg='black', fg='white', command=viewInjury)
    btn5.place(relx=0.70,rely=0.78, relwidth=0.25,relheight=0.05)

    btn7 = Button(root_an,text="Foster",bg='black', fg='white', command=openFoster)
    btn7.place(relx=0.05,rely=0.70, relwidth=0.25,relheight=0.05)

    btn8 = Button(root_an,text="Issue Adopt",bg='black', fg='white', command=openAdopt)
    btn8.place(relx=0.70,rely=0.70, relwidth=0.25,relheight=0.05)

    btn9 = Button(root_an,text="return Animal",bg='black', fg='white', command=ReturnAnimal)
    btn9.place(relx=0.05,rely=0.78, relwidth=0.25,relheight=0.05)

    headingLabel.config(font=('Times New Roman',22))
    btn1.config(font=('Times New Roman',15))
    btn2.config(font=('Times New Roman',15))
    btn3.config(font=('Times New Roman',15))
    btn7.config(font=('Times New Roman',15))
    btn8.config(font=('Times New Roman',15))
    btn5.config(font=('Times New Roman',15))
    btn9.config(font=('Times New Roman',15))

    root_an.mainloop()


def registerAnimal():

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

    AnimalTable = "Animal" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Animal", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # # Animal ID
    # lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    # lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    # an_id = Entry(labelFrame)
    # an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Animal name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    an_name = Entry(labelFrame)
    an_name.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Animal age
    lb3 = Label(labelFrame,text="Age : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    an_age = Entry(labelFrame)
    an_age.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # Animal breed
    lb4 = Label(labelFrame,text="breed : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
        
    breed = Entry(labelFrame)
    breed.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    # Animal species
    lb4 = Label(labelFrame,text="Species : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.6, relheight=0.08)
        
    species = Entry(labelFrame)
    species.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    # Animal details
    lb4 = Label(labelFrame,text="Status(avail/IFC/Adopted) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.7, relheight=0.08)
        
    details = Entry(labelFrame)
    details.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)
    
    
    def sqInsertAnimal(aname,aage,breed,species,details):
        cur.execute("SELECT an_id from Animal")
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
            newidstr = "a000" + str(newid)
        elif newid<100 :
            newidstr = "a00" + str(newid)
        elif newid<1000 :
            newidstr = "a0" + str(newid)
        else :
            newidstr = "a" +str(newid)
        cur.execute("INSERT INTO ANIMAL VALUES(?,?,?,?,?,?);",(newidstr,aname,aage,breed,species,details))
        con.commit()
        return newidstr


    def AddAnimal():
        #animal_id = an_id.get()
        animal_name = an_name.get()
        animal_age = int(an_age.get())
        animal_breed = breed.get()
        animal_species = species.get()
        animal_details = details.get()

        
        #insertAnimal = "insert into "+AnimalTable +" values('"+animal_id+"', '"+animal_name+"', '"+animal_age+"' , '"+animal_breed+"', '"+animal_species+"' , '"+animal_details+"');"
        try:
            #cur.execute(insertAnimal)
            #con.commit()
            animal_id=sqInsertAnimal(animal_name,animal_age,animal_breed,animal_species,animal_details)
            messagebox.showinfo('Success', "animal added")
        except:
            messagebox.showerror('Error', "Something went wrong")

        
        print(animal_id)
        print(animal_name)
        print(animal_age)
        print(animal_breed)
        print(animal_species)
        print(animal_details)
        root.destroy()



    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=AddAnimal)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',15))
    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))
    
    root.mainloop()

    


def removeAnimal():
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

    AnimalTable = "Animal"


    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Remove Animal", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    def sqDeleteAnimal(aid):
        cur.execute("DELETE FROM SPENDING WHERE DONOR_ID IS NULL AND AN_ID=?;",(aid,))
        cur.execute("DELETE FROM TAKES_CARE WHERE VOL_ID IS NULL AND AN_ID=?;",(aid,))
        cur.execute("DELETE FROM ANIMAL WHERE AN_ID=?;",(aid,))
        con.commit()

    def deleteAnimal():
        animal_id = an_id.get()

        try:
            sqDeleteAnimal(animal_id)
            messagebox.showinfo("Success", "Animal record deleted")
        except:
            messagebox.showerror("Error", "something went wrong")

        print(animal_id)
        an_id.delete(0, END)
        root.destroy()

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteAnimal)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    headingLabel.config(font=('Times New Roman',15))
    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))
    
    root.mainloop()




def viewAnimal():

    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))


    root_new = Toplevel()
    root_new.title("Animal")
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

        def sqSearchAnimal(key):
            cur.execute("SELECT * FROM ANIMAL WHERE an_id like ? or an_name like ? or an_age like ? or breed like ? or species like ? or details like ?;",(key,key,key,key,key,key))
            anlist=cur.fetchall()
            return anlist


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

            records = sqSearchAnimal(lookup_record)
            
            i=0
            for r in records:
                tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4], r[5]))
                i+= 1
                
        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)


    records = cur.execute("SELECT * FROM animal")
    
    tree = ttk.Treeview(root_new)
    tree["columns"]=("an_id", "an_name", "an_age", "breed", "species", "details")
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
    tree.column("an_name", width=200, minwidth=50, anchor=CENTER)
    tree.column("an_age", width=150, minwidth=50, anchor=CENTER)
    tree.column("breed", width=250, minwidth=50, anchor=CENTER)
    tree.column("species", width=200, minwidth=50, anchor=CENTER)
    tree.column("details", width=200, minwidth=50, anchor=CENTER)

    tree.heading("an_id", text="Animal Id", anchor=CENTER)
    tree.heading("an_name", text="Name", anchor=CENTER)
    tree.heading("an_age", text="Age", anchor=CENTER)
    tree.heading("breed", text="Breed", anchor=CENTER)
    tree.heading("species", text="Species", anchor=CENTER)
    tree.heading("details", text="Status", anchor=CENTER)

    i=0
    for r in records:
        tree.insert('', i, text = "", values = (r[0], r[1], r[2], r[3], r[4], r[5]))
        i+= 1

    tree.pack(pady=30)
    tree['show'] =  'headings'

    add_frame = LabelFrame(root_new, bg="black" )
    add_frame.pack(fill= "x", expand = "yes", padx = 20)

    #Labels

    lb2 = Label(add_frame, text="Name")
    lb2.grid(row=0, column=0,  padx=125, pady=10)

    lb3 = Label(add_frame, text="Age")
    lb3.grid(row=0, column=1, padx=125, pady=10)

    lb4 = Label(add_frame, text="Breed")
    lb4.grid(row=0, column=2, padx=125, pady=10)

    lb5 = Label(add_frame, text="Species")
    lb5.grid(row=0, column=3, padx=125, pady=10)

    lb6 = Label(add_frame, text="Status")
    lb6.grid(row=0, column=4, padx=125, pady=10)

    lb2.config(font=('Times New Roman',15))
    lb3.config(font=('Times New Roman',15))
    lb4.config(font=('Times New Roman',15))
    lb5.config(font=('Times New Roman',15))
    lb6.config(font=('Times New Roman',15))

    #Entry boxes

    an_name = Entry(add_frame)
    an_name.grid(row=1, column=0)

    an_age = Entry(add_frame)
    an_age.grid(row=1, column=1)

    breed = Entry(add_frame)
    breed.grid(row=1, column=2)

    species = Entry(add_frame)
    species.grid(row=1, column=3)

    details = Entry(add_frame)
    details.grid(row=1, column=4)


    def add_record():

        try:
            con = sqlite3.connect("shelter.db")
            cur = con.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print("error during connection: "+str(e))

        def sqInsertAnimal(aname,aage,breed,species,details):
            cur.execute("SELECT an_id from Animal")
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
                newidstr = "a000" + str(newid)
            elif newid<100 :
                newidstr = "a00" + str(newid)
            elif newid<1000 :
                newidstr = "a0" + str(newid)
            else :
                newidstr = "a" +str(newid)
            cur.execute("INSERT INTO ANIMAL VALUES(?,?,?,?,?,?);",(newidstr,aname,aage,breed,species,details))
            con.commit()
            return newidstr

        try:
            animal_id = sqInsertAnimal(an_name.get(), an_age.get(), breed.get(), species.get(), details.get())
            tree.insert(parent='', index='end', text="", values=(animal_id, an_name.get(), an_age.get(), breed.get(), species.get(), details.get()))
           
            # Clear the boxes
            an_name.delete(0, END)
            an_age.delete(0, END)
            breed.delete(0, END)
            species.delete(0, END)
            details.delete(0, END)

        except:
            messagebox.showerror("Error","Something went wrong", parent= root_new)



    def remove_record():
        
        def sqDeleteAnimal(aid):
            cur.execute("DELETE FROM SPENDING WHERE AN_ID=?;",(aid,))
            cur.execute("DELETE FROM TAKES_CARE WHERE AN_ID=?;",(aid,))
            cur.execute("DELETE FROM ANIMAL WHERE AN_ID=?;",(aid,))
            con.commit()

        selected = tree.focus()
        values = tree.item(selected, 'values')
        sqDeleteAnimal(values[0])

        x = tree.selection()
        tree.delete(x)


    def edit_record():
        an_name.delete(0, END)
        an_age.delete(0, END)
        breed.delete(0, END)
        species.delete(0, END)
        details.delete(0, END)

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        an_name.insert(0, values[1])
        an_age.insert(0, values[2])
        breed.insert(0, values[3])
        species.insert(0, values[4])
        details.insert(0, values[5])

    
    def update_record():

        def sqModifyAnimal(atuple):
            cur.execute("UPDATE ANIMAL SET AN_NAME=?,AN_AGE=?,BREED=?,SPECIES=?,DETAILS=? WHERE AN_ID=?;",(atuple[1],atuple[2],atuple[3],atuple[4],atuple[5],atuple[0]))
            con.commit()

        # Grab record number
        selected = tree.focus()
        # Grab record values
        values = tree.item(selected, 'values')
        
        try:
            tree.item(selected, text="", values=(values[0],an_name.get(), an_age.get(), breed.get(), species.get(), details.get()))
            values = tree.item(selected, 'values')
            sqModifyAnimal(values)

            # Clear entry boxes
            an_name.delete(0, END)
            an_age.delete(0, END)
            breed.delete(0, END)
            species.delete(0, END)
            details.delete(0, END)

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
    
   


def ReturnAnimal():

    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Returning Animal")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    FosterTable = "foster"
    AnimalTable = "animal"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Animal", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    def returnn():
        animal_id = an_id.get()
        extract_An_id = "select an_id from "+FosterTable
        all_An_id = []

        try:
            cur.execute(extract_An_id)
            con.commit()
            for i in cur:
                all_An_id.append(i[0])
            
            if animal_id in all_An_id:
                checkAvail = "select details from "+AnimalTable+" where an_id = '"+animal_id+"'"
                cur.execute(checkAvail)
                con.commit()
                for i in cur:
                    check = i[0]
                    
                if check == 'IFC':
                    status = True
                else:
                    status = False
            else:
                messagebox.showinfo("Error","Animal ID not present", parent = root)
        except:
            messagebox.showinfo("Error","Can't fetch Animal IDs")
        
        
        # removeFoster = "delete from "+FosterTable+" where an_id = '"+animal_id+"'"
        
        print(animal_id in all_An_id)
        print(status)

        updateAnimalDetails = "update "+AnimalTable+" set details = 'avail' where an_id = '"+animal_id+"'"
        try:
            if animal_id in all_An_id and status == True:
                # cur.execute(removeFoster)
                # con.commit()
                cur.execute(updateAnimalDetails)
                con.commit()
                messagebox.showinfo('Success',"Animal Returned Successfully")
            else:
                all_An_id.clear()
                messagebox.showinfo('Message',"Please check the Animal ID")
                root.destroy()
                return
        except:
            messagebox.showinfo("Search Error","The value entered is wrong, Try again")
        
        all_An_id.clear()
        root.destroy()


    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    SubmitBtn.config(font=('Times New Roman',15))
    quitBtn.config(font=('Times New Roman',15))

    root.mainloop()