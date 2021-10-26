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
        #Ta fram efter testning!!!!!
        #file_1 = myfunctions.Select_file(gui)
        #file_1 = myfunctions.Check_file(file_1,gui)
        #file_info = Label(gui, text="Your selection for File_1: "+ file_1)
        #file_info.grid(row = 1, column = 1, pady = 5)
        #DATA = myfunctions.Read_file2(file_1,gui)
        DATA1 = myfunctions.Read_file2("/Users/albertrehnberg/Downloads/Dynamic_InputFile_Example.csv",gui)



        #file2 = Button(gui, text='Browse file_2', command = lambda:myfunctions.Delta2(gui,DATA))
        #file2.grid(row = 2, column = 0, pady =10)
        DATA2 = myfunctions.Read_file2("/Users/albertrehnberg/Downloads/Static_InputFile_Example.csv",gui)
        House_data = myfunctions.House(gui,DATA1,DATA2)



        #HALVFÄRDIGT STUFF
        #disp_data = Button(gui, text='Display data', command = lambda: myfunctions.show_data(gui,DATA))
        #disp_data.grid(row=3, column = 1)
        #Analysis = Button(gui, text="show graphs", command=lambda:myfunctions.analysis(gui, DATA))

        gui.destroy()
        return


    #Denna gör att filläsningsfunktionen kallas
    file1 = Button(gui, text='Browse file_1', command = Delta1)


    file1.grid(row = 1, column = 0, pady=10)


    #my_label.pack()
    #file1.pack()
    #file2.pack()
    gui.mainloop()
if __name__== '__main__':
    main()
