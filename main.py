#fil för att skriva python kod

import myfunctions
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def main():

    gui = Tk()
    gui.title("Energy management system 1.0")
    gui.geometry("500x500")


    my_label = Label(gui, text = "–––––––––––––––– Energy management system –––––––––––––––")
    my_label.grid(row=0,  column=1, pady = 10)
    print("–––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***––––––")
    print("–––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***––––––")
    #Läsa, skriva och ändra csv-filen sker inne i denna funktion
    def Delta1():
        file_1 = myfunctions.Select_file(gui)
        file_1 = myfunctions.Check_file(file_1,gui)
        file_info = Label(gui, text="Your selection for File_1: "+ file_1)
        file_info.grid(row = 1, column = 1, pady = 5)

        DATA = myfunctions.Read_file(file_1,gui)

        #disp_data = Button(gui, text='Display data', command = lambda: myfunctions.show_data(gui,DATA))
        #disp_data.grid(row=3, column = 1)
        #Analysis = Button(gui, text="show graphs", command=lambda:myfunctions.analysis(gui, DATA))

    def Delta2():
        file_2 = myfunctions.Select_file(gui)
        file_2 = myfunctions.Check_file(file_2,gui)
        file_info = Label(gui,text="Your selection for File_2: "+ file_2)
        file_info.grid(row = 2, column = 1, pady = 5)

        DATA = myfunctions.Read_file2(file_2,gui)

        #disp_data2 = Button(gui, text='Display data', command = lambda:myfunctions.show_data(gui,DATA)).grid(row=3, column = 1)

        House_data = Button(gui, text="calculate house data", command = lambda:myfunctions.house(gui,DATA)).grid(row=3, column = 2)

    #Denna gör att filläsningsfunktionen kallas
    file1 = Button(gui, text='Browse file_1', command = Delta1)
    file2 = Button(gui, text='Browse file_2', command = Delta2)

    file1.grid(row = 1, column = 0, pady=10)
    file2.grid(row = 2, column = 0, pady =10)


    #my_label.pack()
    #file1.pack()
    #file2.pack()
    gui.mainloop()
if __name__== '__main__':
    main()
