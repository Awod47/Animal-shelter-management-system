import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openDonations():
    root_don = Toplevel()
    root_don.title("Animal")
    root_don.minsize(width=400,height=400)
    root_don.geometry("1920x1800")

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
    label = ttk.Label(root_don, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_don,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Animal data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_don,text="Add Donation",bg='black', fg='white', command=registerDonation)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_don,text="Remove Donation",bg='black', fg='white', command=removeDonation)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_don,text="View Donations",bg='black', fg='white', command=viewDonations)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    btn4 = Button(root_don,text="Search Donation",bg='black', fg='white', command=searchDonation)
    btn4.place(relx=0.52,rely=0.5, relwidth=0.25,relheight=0.05)
    root_don.mainloop()



def registerDonation():
    pass

def removeDonation():
    pass

def viewDonations():
    pass

def searchDonation():
    pass