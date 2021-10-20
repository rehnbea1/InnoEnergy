#fil för att skriva python kod
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *


gui = Tk()
gui.title("Energy management system 1.0")
gui.geometry("500x500")

my_label = Label(gui, text = "Welcome to read file")

def Delta():
    filename = Select_file()
    print("ok")
    Read_file(filename)

#Denna gör att filläsningsfunktionen kallas
file = Button(gui, text='Browse file', command = Delta)


file.pack()
my_label.pack()
gui.mainloop()
