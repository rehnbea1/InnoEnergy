#fil för att skriva python kod
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *



gui = Tk()
gui.title("Energy management system 1.0")
gui.geometry("500x500")

my_label = Label(gui, text = "Welcome to read file")



def select_file():
    filetypes = (('csv-files', '*.pdf'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    file_info=Label(gui,text=filename).pack()

open_button = Button(gui, text='Browse file',command = select_file)


open_button.pack()
my_label.pack()
gui.mainloop()
