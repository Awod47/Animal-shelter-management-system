import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openFoster():
    root_fos = Tk()
    root_fos.title("Foster")
    root_fos.minsize(width=400,height=400)
    root_fos.geometry("900x600")