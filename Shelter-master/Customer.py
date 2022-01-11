import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openCustomer():
    root_cus = Tk()
    root_cus.title("Customer")
    root_cus.minsize(width=400,height=400)
    root_cus.geometry("900x600")