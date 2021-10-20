#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox

def Select_file(gui):
    filetypes = (('csv-files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='documents/',filetypes=filetypes)
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
    Choice = tk.messagebox.askyesno(title="Option", message="Your file is invalid. Do you want to try again?")
    return Choice

def Check_file(file,gui):
    #checks if the file selected is ok
    file=str(file)
    if file.endswith('csv'):
        return file
    else:
        print("this is not a csv file")
        file = False
        while file == False:
            Choice = option_popup(gui)
            if Choice == True:
                file = Select_file(gui)
                if file != '/.csv' :
                    file = False
                else:
                    file = file
            elif Choice == False:
                file = "Not selected"
                print("ok")
        return file
