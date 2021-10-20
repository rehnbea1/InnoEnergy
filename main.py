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

    while file_1 == 0:
        Label(gui, text="the file you wanted to read didn't work. Try again?")
        Choice = myfunctions.option_popup(gui)
        if Choice == False:
            file = Button(gui, text='Browse file', command = myfunctions.Select_file(gui)).pack()
        else:
            print("ok")
            file_2 = myfunctions.Select_file(gui)
            file_info = Label(gui,text="The file you chose is: " + file_1).pack()
            myfunctions.Read_file(filename,gui)
    print("ok")
    file_2 = myfunctions.Select_file(gui)
    file_info = Label(gui,text = "The file you chose is: " + file_1).pack()
    myfunctions.Read_file(filename,gui)

    while file_2 == False:
        Label(gui, text="the file you wanted to read didn't work. Try again?")
        Answer = tk.Entry(master)
        if Answer == "J":
            file = Button(gui, text='Browse file', command = myfunctions.Select_file(gui))
        else:
            file_2 = "Empty"


#Denna gör att filläsningsfunktionen kallas
file = Button(gui, text='Browse file', command = Delta)







file.pack()
my_label.pack()
gui.mainloop()
