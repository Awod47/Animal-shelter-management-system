import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openVolunteer():
    root_vol = Toplevel()
    root_vol.title("Animal")
    root_vol.minsize(width=400,height=400)
    root_vol.geometry("900x600")

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
    label = ttk.Label(root_vol, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_vol,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Animal data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_vol,text="Add Donation",bg='black', fg='white', command=registerVolunteer)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_vol,text="Remove Donation",bg='black', fg='white', command=removeVolunteer)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_vol,text="View Donations",bg='black', fg='white', command=viewVolunteers)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    btn4 = Button(root_vol,text="Search Donation",bg='black', fg='white', command=searchVolunteer)
    btn4.place(relx=0.52,rely=0.5, relwidth=0.25,relheight=0.05)
    root_vol.mainloop()



def registerVolunteer():
    pass

def removeVolunteer():
    pass

def viewVolunteers():
    pass

def searchVolunteer():
    pass