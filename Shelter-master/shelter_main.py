import sqlite3
from tkinter import *
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
    cur.execute("CREATE TABLE IF NOT EXISTS donations(donor_id TEXT PRIMARY KEY, resource TEXT, amount INT CHECK (typeof(amount) = 'integer'), don_date TEXT, availability TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS spending(an_id TEXT, donor_id TEXT, resource TEXT, amount INT CHECK (typeof(amount) = 'integer'), time TEXT, sp_date TEXT , FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE, FOREIGN KEY(donor_id) REFERENCES Donotions(donor_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer(vol_id TEXT PRIMARY KEY, vol_name TEXT, vol_dob TEXT, vol_phone INT CHECK (typeof(vol_phone) = 'integer'), vol_address TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS takes_care(vol_id TEXT, an_id TEXT, tc_date TEXT, tcStart_time TEXT, tcEnd_time TEXT, FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE, FOREIGN KEY(an_id) REFERENCES Animal(an_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS volunteer_timings(vol_id TEXT, vol_date TEXT, vStart_time TEXT, vEnd_time TEXT,  FOREIGN KEY(vol_id) REFERENCES Volunteer(vol_id) ON DELETE CASCADE);")
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
    image = Image.open('pup.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to XXX Animal shelter", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root,text="Animal",bg='black', fg='white', command=openAnimal)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root,text="Customer",bg='black', fg='white', command=openCustomer)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root,text="Issue Foster",bg='black', fg='white', command=openFoster)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    btn4 = Button(root,text="Issue Adoption",bg='black', fg='white', command=openAdopt)
    btn4.place(relx=0.52,rely=0.5, relwidth=0.25,relheight=0.05)

    btn5 = Button(root,text="Report Injury",bg='black', fg='white', command=openInjury)
    btn5.place(relx=0.23,rely=0.6, relwidth=0.25,relheight=0.05)

    btn6 = Button(root,text="Donations",bg='black', fg='white', command=openDonations)
    btn6.place(relx=0.52,rely=0.6, relwidth=0.25,relheight=0.05)

    btn7 = Button(root,text="Report spending",bg='black', fg='white', command=openSpending)
    btn7.place(relx=0.23,rely=0.7, relwidth=0.25,relheight=0.05)

    btn8 = Button(root,text="Volunteer",bg='black', fg='white', command=openVolunteer)
    btn8.place(relx=0.52,rely=0.7, relwidth=0.25,relheight=0.05)

    btn9 = Button(root,text="Caring for",bg='black', fg='white', command=openTakesCare)
    btn9.place(relx=0.23,rely=0.8, relwidth=0.25,relheight=0.05)

    btn10 = Button(root,text="Volunteer timings",bg='black', fg='white', command=openVolunteerTimings)
    btn10.place(relx=0.52,rely=0.8, relwidth=0.25,relheight=0.05)
        
    root.mainloop()



def Authenticate():
    #to authenticate username and password
    user = user_name.get()
    password = pass_word.get()
    if user =='' and password=='':
        root_login.destroy()
        MainPage()
    elif user=='s' or password == 's':
        messagebox.showerror("Error", "Username and/or Password cannot be blank", parent = root_login)
    else:
        messagebox.showerror("Error", "invalid user, try again", parent=root_login)
        

# login form
root_login = Tk()
root_login.title("Shelter login")
root_login.minsize(width=400,height=400)
root_login.geometry("800x500")
headingFrame1 = Frame(root_login,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
headingLabel = Label(headingFrame1, text="LOGIN TO CONTINUE", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
labelFrame = Frame(root_login,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
# Username
lb1 = Label(labelFrame,text="Username : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.2, relheight=0.12)
    
user_name = Entry(labelFrame)
user_name.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.12)
    
# Password
lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.35, relheight=0.12)
    
pass_word = Entry(labelFrame, show='*')
pass_word.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.12)
    
# Submit Button
SubmitBtn = Button(root_login,text="SUBMIT",bg='#d1ccc0', fg='black',command=Authenticate)
SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Quit button
quitBtn = Button(root_login,text="Quit",bg='#f7f1e3', fg='black',command=root_login.destroy)
quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
root_login.mainloop()



