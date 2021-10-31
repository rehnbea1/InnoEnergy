#fil för att skriva python kod

import myfunctions
import mymanagement
import mygraphs
import tkinter as tk
from tkinter import *
from tkinter.ttk import *


import matplotlib
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.figure import Figure




LARGE_FONT = ("Verdana", 12)

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both",expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("500x500")

        self.frames = {}

        for F in (
        StartPage,
        PageOne,
        PageTwo
        ):

            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="StartPage", font= LARGE_FONT)
        label.grid(row=0,pady=10)

        file2 = Button(self,text="testknapp", command = lambda: myfunctions.select_file(gui)).grid(row=4)
        print(file2)
        file1 = Button(self, text='Browse file_1',
                        command = lambda: Delta1()).grid(row = 1)

        Page_two = Button(self, text="PageOne",
                        command = lambda: controller.show_frame(PageOne)).grid(row = 2)

        Graph_page = Button(self, text="GraphPage",
                        command = lambda: controller.show_frame(PageTwo)).grid(row = 3)


class PageOne(tk.Frame):

   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       label = tk.Label(self,text="PageOne", font= LARGE_FONT)
       label.grid(row=1,pady=10)

       Button1 = Button(self, text="Back to Home",
                        command = lambda: controller.show_frame(StartPage)).grid(row = 3)


class PageTwo(tk.Frame):

   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       label = tk.Label(self,text="GraphPage", font= LARGE_FONT)
       label.grid(row=1,pady=10)

       Button1 = Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage)).grid(row = 3)


#
#
#
#jobbar här, vill implementera ett sätt att plocka dynamic_file oberoende av class


   def plot_graph(self):

       #This function plots the input
       get_files = myfunctions.Get_file()
       f = Figure(figsize=(5,5),dpi=100)
       a = f.add_subplot(111)
       a.plot(df1['H_storage'])

       canvas = FigureCanvasTkAgg(f, self)
       canvas.draw()
       canvas.get_tk_widget().grid(row = 5)



def Delta1():
        #Ta fram efter testning!!!!!
        #file_1 = myfunctions.select_file(gui)
        #file_1 = myfunctions.Check_file(file_1,gui)
        #file_info = Label(gui, text="Your selection for File_1: "+ file_1)
        #file_info.grid(row = 1, column = 1, pady = 5)
        #DATA = myfunctions.Read_file2(file_1,gui)
        DATA1 = myfunctions.read_file2("/Users/albertrehnberg/Downloads/Dynamic_Data.csv",gui)

        #file2 = Button(gui, text='Browse file_2', command = lambda:myfunctions.Delta2(gui,DATA))
        #file2.grid(row = 2, column = 0, pady =10)
        DATA2 = myfunctions.read_file2("/Users/albertrehnberg/Downloads/Static_Data.csv",gui)
        House_data = myfunctions.House(gui,DATA1,DATA2)

        save_data = myfunctions.Get_file_info(House_data[0], House_data[1])


        management = mymanagement.main_action(House_data[0],House_data[1])


        #HALVFÄRDIGT STUFF
        #disp_data = Button(gui, text='Display data', command = lambda: myfunctions.show_data(gui,DATA))
        #disp_data.grid(row=3, column = 1)
        #Analysis = Button(gui, text="show graphs", command=lambda:myfunctions.analysis(gui, DATA))

        print("–––––Data1–––––")
        print(management[0])
        print("-----data2-----")
        print(management[1])



        #stänger fönstret automatiskt nu



        #gui.destroy()
        return


    #print("–––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***––––––")
    #print("–––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***–––––––––––––***––––––")
    #Läsa, skriva och ändra csv-filen sker inne i denna funktion




    #Denna gör att filläsningsfunktionen kallas


    #my_label.pack()
    #file1.pack()
    #file2.pack()
gui = Window()
gui.mainloop()



if __name__== '__main__':
    main()
