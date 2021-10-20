#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox

def Select_file(gui):
    print("hej")
    filetypes = (('csv-files', '*.pdf'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='documents/',filetypes=filetypes)
    if filename != '*.csv' :
        print("this is not a csv file")
        return 0

    return filename

def Read_file(filename,gui):
    #try:
    with open(filename,'r') as file:
        file = file.read()


    #except FileNotFoundError:
    #    Label(gui,text="Error! Could not read the file, make sure you selected the right file").pack()
    #    return False
    #except UnicodeDecodeError:
    #    Label(gui,text="Error! Could not decrypt the file, make sure you selected the right file").pack()
    #    return False

def option_popup(gui):
    tk.messagebox.askyesno(title="Option", message="Your file is invalid. Do you want to try again?")
    return
