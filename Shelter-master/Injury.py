import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openInjury():
    root_in = Tk()
    root_in.title("Injury")
    root_in.minsize(width=400,height=400)
    root_in.geometry("900x600")