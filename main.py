#fil för att skriva python kod

import myfunctions
import tkinter as tk
from tkinter import *
from tkinter.ttk import *


gui = Tk()
gui.title("Energy management system 1.0")
gui.geometry("500x500")

my_label = Label(gui, text = "Welcome to read file")


#Läsa, skriva och ändra csv-filen sker inne i denna funktion
def Delta():
    file_1 = myfunctions.Select_file(gui)
    file_1 = myfunctions.Check_file(file_1,gui)
    file_info = Label(gui,text="Your selection for File_1: "+ file_1).pack()

    file_2 = myfunctions.Select_file(gui)
    file_2 = myfunctions.Check_file(file_2,gui)
    file_info = Label(gui,text="Your selection for File_2: "+ file_2).pack()

    myfunctions.Read_file(file_1,gui)
    myfunctions.Read_file(file_2,gui)


#Denna gör att filläsningsfunktionen kallas
file = Button(gui, text='Browse file', command = Delta)







file.pack()
my_label.pack()
gui.mainloop()
