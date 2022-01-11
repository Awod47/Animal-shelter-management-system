import sqlite3
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox, ttk

def openAdopt():
    root_adopt = Tk()
    root_adopt.title("Adopt")
    root_adopt.minsize(width=400,height=400)
    root_adopt.geometry("900x600")