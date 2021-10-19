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
    print("hej")
    filetypes = (('csv-files', '*.pdf'),('All files', '*.*'))
    print("filenames",filetypes)
    filename = fd.askopenfilename(title='Open a file',initialdir='documents/',filetypes=filetypes)
    print("fil")
    print(filename)

    file_info=Label(gui,text=filename).pack()

#denna del returnerar inget värde för "fil"
file = Button(gui, text='Browse file', command = lambda: select_file()).pack()
print(file)
print("hej")
#print(file)


#file = select_file
#with open(file,'r') as file:#
#    file = file.read()

my_label.pack()
gui.mainloop()
