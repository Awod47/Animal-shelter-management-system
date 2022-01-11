import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk


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
    image = Image.open('pup.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root_an, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    # heading label
    headingFrame1 = Frame(root_an,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Animal data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #buttons for different tables
    btn1 = Button(root_an,text="Add Animal",bg='black', fg='white', command=registerAnimal)
    btn1.place(relx=0.23,rely=0.4, relwidth=0.25,relheight=0.05)
        
    btn2 = Button(root_an,text="Remove",bg='black', fg='white', command=removeAnimal)
    btn2.place(relx=0.52,rely=0.4, relwidth=0.25,relheight=0.05)

    btn3 = Button(root_an,text="View Animals",bg='black', fg='white', command=viewAnimal)
    btn3.place(relx=0.23,rely=0.5, relwidth=0.25,relheight=0.05)

    btn4 = Button(root_an,text="Search animal",bg='black', fg='white', command=searchAnimal)
    btn4.place(relx=0.52,rely=0.5, relwidth=0.25,relheight=0.05)
    root_an.mainloop()


def registerAnimal():

    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
    except Exception as e:
        print("error during connection: "+str(e))
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("900x700")

    AnimalTable = "Animal" # Animal Table
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Animal ID
    lb1 = Label(labelFrame,text="Animal ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    an_id = Entry(labelFrame)
    an_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
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
    lb4 = Label(labelFrame,text="Status(neutured/aggression) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.7, relheight=0.08)
        
    details = Entry(labelFrame)
    details.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)
    

    def AddAnimal():
        animal_id = an_id.get()
        animal_name = an_name.get()
        animal_age = an_age.get()
        animal_breed = breed.get()
        animal_species = species.get()
        animal_details = details.get()

        insertAnimal = "insert into "+AnimalTable +" values('"+animal_id+"', '"+animal_name+"', '"+animal_age+"' , '"+animal_breed+"', '"+animal_species+"' , '"+animal_details+"');"
        try:
            cur.execute(insertAnimal)
            con.commit()
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
    
    root.mainloop()

    


def removeAnimal():
    try:
        con = sqlite3.connect("shelter.db")
        cur = con.cursor()
    except Exception as e:
        print("error during connection: "+str(e))

    root = Tk()
    root.title("Library")
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


    def deleteAnimal():
        animal_id = an_id.get()
        removeCommand = 'delete from ' +AnimalTable+ " where an_id = '"+animal_id+"'"

        try:
            cur.execute(removeCommand)
            con.commit()
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
    
    root.mainloop()




def viewAnimal():
    pass


def searchAnimal():
    pass



