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


FILE1 = None
FILE2 = None
DATABASE1 = None
DATABASE2 = None



LARGE_FONT = ("Verdana", 12)

class File:

    def __init__(self, file):
        self.file = file
        if str(type(file)) == "<class 'pandas.core.frame.DataFrame'>":
            list =[]
            for key in file.keys():
                list.append(key)
            self.headers = list
        else:
            list = []
            for dict in file:
                for key in file[dict].keys():
                    a = str(dict+" : "+key)
                    list.append(a)
            self.headers = list



class Window(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both",expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("120x150")



        self.frames = {}

        for F in (StartPage,PageOne,GraphPage):

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

        destroy = Button(self,text="testknapp", command = lambda: gui.destroy()).grid(row=4)

        file1 = Button(self, text='Browse file_1',
                        command = lambda: self.Delta1()).grid(row = 1)

        Page_two = Button(self, text="PageOne",
                        command = lambda: controller.show_frame(PageOne)).grid(row = 2)

        Graph_page = Button(self, text="GraphPage",
                        command = lambda: controller.show_frame(GraphPage)).grid(row = 4)

    def Delta1(self):

        #Ta fram efter testning!!!!!
        #file_1 = myfunctions.select_file(gui)
        #file_1 = myfunctions.Check_file(file_1,gui)
        #file_info = Label(gui, text="Your selection for File_1: "+ file_1)
        #file_info.grid(row = 1, column = 1, pady = 5)
        #DATA = myfunctions.Read_file2(file_1,gui)
        DATA1 = myfunctions.read_file("/Users/albertrehnberg/Downloads/Dynamic_Data.csv",gui)

        #file2 = Button(gui, text='Browse file_2', command = lambda:myfunctions.Delta2(gui,DATA))
        #file2.grid(row = 2, column = 0, pady =10)
        DATA2 = myfunctions.read_file("/Users/albertrehnberg/Downloads/Static_Data.csv",gui)
        House_data = myfunctions.House(gui,DATA1,DATA2)

        #save_data = myfunctions.Get_file_info(House_data[0], House_data[1])

        df = myfunctions.H_storage(House_data[0],House_data[1])
        DATABASES = myfunctions.import_databases(gui)

        #HALVFÄRDIGT STUFF
        #disp_data = Button(gui, text='Display data', command = lambda: myfunctions.show_data(gui,DATA))
        #disp_data.grid(row=3, column = 1)
        #Analysis = Button(gui, text="show graphs", command=lambda:myfunctions.analysis(gui, DATA))

        #stänger fönstret automatiskt nu
        FILE1 = File(df[0])

        FILE2 = File(df[1])

        DATABASE1 = File(DATABASES[0])

        DATABASE2 = File(DATABASES[1])

        management = myfunctions.get_graph_options(gui,FILE1,FILE2, DATABASE1,DATABASE2)

        #print("–––––FILE1–––––")
        #print(FILE1.file)
        #print("–––––FILE2–––––")
        #print(FILE2)
        #print("–––––DATABASE1–––––")
        #p#rint(DATABASE1)
        #print("–––––DATABASE2–––––")
        #print(DATABASE2)


        return FILE1, FILE2, DATABASE1, DATABASE2


        #Läsa, skriva och ändra csv-filen sker inne i denna funktion

        #Denna gör att filläsningsfunktionen kallas

        #my_label.pack()
        #file1.pack()
        #file2.pack()


class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="PageOne", font= LARGE_FONT)
        label.grid(row=1,pady=10)

        Button1 = Button(self, text="Back to Home",
                        command = lambda: controller.show_frame(StartPage)).grid(row = 3)



class GraphPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="GraphPage", font= LARGE_FONT)
        label.grid(row=1,pady=10)

        Button1 = Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage)).grid(row = 3)
        clicked = StringVar()
        clicked.set("Monday")

        options = Button(self,text= "press me", command = lambda: myfunctions.get_graph_options(FILE1, FILE2,DATABASE1,DATABASE2)).grid(row=4)
        #drop_down = OptionMenu(self, clicked, *options).pack()

       #myButton  = Button(self, text = "selection", command = show)



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


gui = Window()
gui.mainloop()



if __name__== '__main__':
    main()
