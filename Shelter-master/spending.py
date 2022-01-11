import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openSpending():
    root_sp = Toplevel()
    root_sp.title("Animal")
    root_sp.minsize(width=400,height=400)
    root_sp.geometry("900x600")

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
    headingLabel = Label(headingFrame1, text="Animal data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_sp,text="Add Donation",bg='black', fg='white', command=registerSpending)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_sp,text="Remove Donation",bg='black', fg='white', command=removeSpending)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_sp,text="View Donations",bg='black', fg='white', command=viewVolunteers)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    btn4 = Button(root_sp,text="Search Donation",bg='black', fg='white', command=searchVolunteer)
    btn4.place(relx=0.52,rely=0.5, relwidth=0.25,relheight=0.05)
    root_sp.mainloop()


def registerSpending():
    pass

def removeSpending():
    pass

def viewVolunteers():
    pass

def searchVolunteer():
    pass