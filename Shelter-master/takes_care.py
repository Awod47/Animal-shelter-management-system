import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openTakesCare():
    root_tc = Toplevel()
    root_tc.title("Animal")
    root_tc.minsize(width=400,height=400)
    root_tc.geometry("900x600")