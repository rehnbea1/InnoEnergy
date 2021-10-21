#fil för att skriva python kod

import myfunctions
import tkinter as tk
from tkinter import *
from tkinter.ttk import *


gui = Tk()
gui.title("Energy management system 1.0")
gui.geometry("500x500")

my_label = Label(gui, text = "Welcome to read file")
print("–––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***––––––")
print("–––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***––––––")
#Läsa, skriva och ändra csv-filen sker inne i denna funktion
def Delta1():
    file_1 = myfunctions.Select_file(gui)
    file_1 = myfunctions.Check_file(file_1,gui)
    file_info = Label(gui, text="Your selection for File_1: "+ file_1).pack()

    myfunctions.Read_file(file_1,gui)

def Delta2():
    file_2 = myfunctions.Select_file(gui)
    file_2 = myfunctions.Check_file(file_2,gui)
    file_info = Label(gui,text="Your selection for File_2: "+ file_2).pack()

    myfunctions.Read_file(file_2,gui)

#Denna gör att filläsningsfunktionen kallas
file1 = Button(gui, text='Browse file_1', command = Delta1)
file2 = Button(gui, text='Browse file_2', command = Delta2)

my_label.grid(row=0,  column=1)
file1.grid(row = 1, column = 0)
file2.grid(row = 1, column = 1)


my_label.pack()
file1.pack()
file2.pack()
gui.mainloop()
