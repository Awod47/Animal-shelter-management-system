import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openVolunteerTimings():
    root_volt = Toplevel()
    root_volt.title("Animal")
    root_volt.minsize(width=400,height=400)
    root_volt.geometry("900x600")