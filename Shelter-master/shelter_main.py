from operator import ge
import sqlite3
from tkinter import *
from tkinter import font
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk
from Animal import *
from Customer import *
from Foster import *
from Adopt import *
from Injury import *
from donations import *
from spending import *
from volunteer import *
from takes_care import *
from volunteer_timings import *

try:
    con = sqlite3.connect("shelter.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    print("connection successful")
except Exception as e:
    print("error during connection: "+str(e))


def create_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS Animal(an_id TEXT PRIMARY KEY, an_name TEXT, an_age INT CHECK (typeof(an_age) = 'integer'), breed TEXT, species TEXT, details TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS Customer(cust_id TEXT PRIMARY KEY, cust_name TEXT, phone INT CHECK (typeof(phone) = 'integer'), DOB TEXT, address TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS foster(an_id TEXT, cust_id TEXT, fost_date TEXT, due_date TEXT, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS adopt(an_id TEXT, cust_id TEXT, ad_date TEXT, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(cust_id) REFERENCES Customer(cust_id) ON DELETE CASCADE, PRIMARY KEY(an_id, cust_id));")
    cur.execute("CREATE TABLE IF NOT EXISTS injury(an_id TEXT, in_date TEXT, body_part TEXT, injury_status TEXT, PRIMARY KEY(an_id, in_date, body_part), FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS donations(donor_id TEXT PRIMARY KEY, resource TEXT, amount INT, don_date TEXT, availability TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS spending(an_id TEXT, donor_id TEXT, resource TEXT, amount INT, time TEXT, sp_date TEXT , FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(donor_id) REFERENCES donations(donor_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer(vol_id TEXT PRIMARY KEY, vol_name TEXT, vol_dob TEXT, vol_phone INT CHECK (typeof(vol_phone) = 'integer'), vol_address TEXT);")
    # cur.execute("CREATE TABLE IF NOT EXISTS takes_care(vol_id TEXT, an_id TEXT, tc_date TEXT, tcStart_time TEXT, tcEnd_time TEXT, FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer_timings(vol_id TEXT, an_id TEXT, vol_date TEXT, vStart_time TEXT, vEnd_time TEXT,  FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS Password(pass TEXT );")
    con.commit()
    cur.close()
    con.close()

create_tables()


# Main page
def MainPage():
    root = Tk()
    root.title("Shelter")
    root.minsize(width=400,height=400)
    root.geometry("1920x1080")

    # Adding a background image and resizing it
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    image = Image.open('pups2.jfif')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to ABC Animal shelter", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root,text="Animal",bg='black', fg='white', command=openAnimal)
    btn1.place(relx=0.3,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root,text="Customer",bg='black', fg='white', command=openCustomer)
    btn2.place(relx=0.45,rely=0.5, relwidth=0.25,relheight=0.05)

    btn6 = Button(root,text="Donations",bg='black', fg='white', command=openDonations)
    btn6.place(relx=0.45,rely=0.7, relwidth=0.25,relheight=0.05)

    btn8 = Button(root,text="Volunteer",bg='black', fg='white', command=openVolunteer)
    btn8.place(relx=0.3,rely=0.6, relwidth=0.25,relheight=0.05)

    headingLabel.config(font=('Times New Roman',22))
    btn1.config(font=('Times New Roman',16))
    btn2.config(font=('Times New Roman',16))
    btn6.config(font=('Times New Roman',16))
    btn8.config(font=('Times New Roman',16))

        
    root.mainloop()


try:
    con1 = sqlite3.connect("shelter.db")
    cur1 = con1.cursor()
    cur1.execute("PRAGMA foreign_keys = ON;")
    print("connection successful")
except Exception as e:
    print("error during connection: "+str(e))



def sqSetPassword(psw):

    def sqIsPassCreated():
        cur1.execute("SELECT COUNT(*) from Password")
        L=cur1.fetchall()
        if L[0][0]==1 :
            return True
        else :
            return False

    if sqIsPassCreated() == False :
        cur1.execute("INSERT INTO Password VALUES(?); ",(psw,))
        con1.commit()  


def Authenticate():
    #to authenticate username and password
    def sqGetPassword():
        cur1.execute("SELECT * FROM PASSWORD")
        L=cur1.fetchall()
        return L[0][0]  
        
    password_entered = pass_word.get()
    password_saved = sqGetPassword()
    if password_entered == password_saved:
        root_login.destroy()
        MainPage()
    elif password_entered == '':
        messagebox.showerror("Error", "Password cannot be blank", parent = root_login)
    else:
        messagebox.showerror("Error", "invalid password, try again", parent=root_login)


def newPass():
    root_chpass = Tk()
    root_chpass.title("Change password")
    root_chpass.minsize(width=400,height=400)
    root_chpass.geometry("800x500")

    Canvas1 = Canvas(root_chpass)
        
    Canvas1.config(bg="#222222")
    Canvas1.pack(expand=True,fill=BOTH) 

    headingFrame1 = Frame(root_chpass,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Password change", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root_chpass,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # lb1 = Label(labelFrame,text="Enter new password:", bg='black', fg='white')
    # lb1.place(relx=0.29,rely=0.15, relheight=0.12)

    # lb1.config(font=('Times New Roman',16))
        
    # user_name = Entry(labelFrame)
    # user_name.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.12)

    #old password    
    lb1 = Label(labelFrame,text="Old Password : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.35, relheight=0.12)
        
    old_pass_word = Entry(labelFrame)
    old_pass_word.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.12)

    # Password
    lb2 = Label(labelFrame,text="New Password : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.48, relheight=0.12)
        
    pass_word = Entry(labelFrame)
    pass_word.place(relx=0.3,rely=0.48, relwidth=0.62, relheight=0.12)

    #confirm password
    lb3 = Label(labelFrame,text="Confirm Password : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.61, relheight=0.12)
        
    confirm = Entry(labelFrame)
    confirm.place(relx=0.3,rely=0.61, relwidth=0.62, relheight=0.12)

    def changePass():
        def sqGetPassword():
            cur1.execute("SELECT * FROM PASSWORD")
            L=cur1.fetchall()
            return L[0][0] 

        saved_pass = sqGetPassword()
        new_pass = pass_word.get()
        confirm_pass = confirm.get()
        oldPass = old_pass_word.get()

        try:
            if oldPass == saved_pass and new_pass == confirm_pass:
                cur1.execute("DELETE FROM PASSWORD WHERE PASS=?;",(oldPass,))
                sqSetPassword(new_pass)
                messagebox.showinfo("Success", "Password updated", parent = root_login)
                root_chpass.destroy()
            
            else:
                messagebox.showerror("Error", "Old password is incorrect or the new passwords do not match", parent = root_chpass)

        except:
            messagebox.showerror("Error", "Something went wrong", parent = root_chpass)

            
        
    # Submit Button
    SubmitBtn = Button(root_chpass,text="SUBMIT",bg='#d1ccc0', fg='black',command=changePass)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.06)

    # Quit button
    quitBtn = Button(root_chpass,text="Quit",bg='#f7f1e3', fg='black',command=root_chpass.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.06)
    root_login.mainloop()

# login form
root_login = Tk()
root_login.title("Shelter login")
root_login.minsize(width=400,height=400)
root_login.geometry("800x500")

Canvas1 = Canvas(root_login)
    
Canvas1.config(bg="#222222")
Canvas1.pack(expand=True,fill=BOTH) 

headingFrame1 = Frame(root_login,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
headingLabel = Label(headingFrame1, text="LOGIN TO CONTINUE", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
labelFrame = Frame(root_login,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    

# lb1 = Label(labelFrame,text="Enter registered Password for ABC shelter:", bg='black', fg='white')
# lb1.place(relx=0.22,rely=0.15, relheight=0.12)

# lb1.config(font=('Times New Roman',16))
    
    
# Password
lb1 = Label(labelFrame,text="Password : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.35, relheight=0.12)
    
pass_word = Entry(labelFrame, show='*')
pass_word.place(relx=0.2,rely=0.35, relwidth=0.62, relheight=0.12)
    
# Submit Button
SubmitBtn = Button(root_login,text="Submit",bg='#d1ccc0', fg='black',command=Authenticate)
SubmitBtn.place(relx=0.18,rely=0.84, relwidth=0.18,relheight=0.06)

# Quit button
quitBtn = Button(root_login,text="Quit",bg='#f7f1e3', fg='black',command=root_login.destroy)
quitBtn.place(relx=0.63,rely=0.84, relwidth=0.18,relheight=0.06)

#change password button
chPassBtn = Button(root_login,text="Change password",bg='#f7f1e3', fg='black',command=newPass)
chPassBtn.place(relx=0.40,rely=0.84, relwidth=0.18,relheight=0.06)

root_login.mainloop()


