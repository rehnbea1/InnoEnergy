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
LARGE_FONT = ("Verdana", 8)




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

        self.geometry("350x350")


        self.shared_data = {'file1':StringVar(), 'file2': StringVar(), 'DATABASE1': StringVar(), 'DATABASE2':StringVar(),'DATABASE3':StringVar(), 'options':StringVar()}

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


        self.file1 = controller.shared_data['file1']
        self.file2 = controller.shared_data['file2']
        self.DATABASE1 = controller.shared_data['DATABASE1']
        self.DATABASE2 = controller.shared_data['DATABASE2']
        self.DATABASE3 = controller.shared_data['DATABASE3']
        self.options = controller.shared_data['options']


        #controller.shared_data.update({'options':options})



        file1 = Button(self, text='Browse file_1',
                        command = lambda: self.Delta1()).grid(row = 1)

        Page_two = Button(self, text="PageOne",
                        command = lambda: controller.show_frame(PageOne)).grid(row = 2)

        Graph_page = Button(self, text="GraphPage",
                        command = lambda: controller.show_frame(GraphPage)).grid(row = 4)

        destroy = Button(self,text="testknapp",
                        command = lambda: gui.destroy()).grid(row=5)



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
        df = myfunctions.House(gui,DATA1,DATA2)

        #save_data = myfunctions.Get_file_info(House_data[0], House_data[1])


        DATABASES = myfunctions.import_databases(gui)

        #HALVFÄRDIGT STUFF
        #disp_data = Button(gui, text='Display data', command = lambda: myfunctions.show_data(gui,DATA))
        #disp_data.grid(row=3, column = 1)
        #Analysis = Button(gui, text="show graphs", command=lambda:myfunctions.analysis(gui, DATA))

        #stänger fönstret automatiskt nu

        files  = [df[0],df[1],DATABASES[0],DATABASES[1],DATABASES[2]]

        FILE1 = File(df[0])
        FILE2 = File(df[1])

        DATABASE1 = File(DATABASES[0])
        DATABASE2 = File(DATABASES[1])
        DATABASE3 = File(DATABASES[2])


        print(FILE1.file.columns)
        options = myfunctions.get_graph_options(FILE1,FILE2, DATABASE1,DATABASE2)


        self.file1.set(FILE1.file)
        self.file2.set(FILE2.file)
        self.DATABASE1.set(DATABASE1.file)
        self.DATABASE2.set(DATABASE2.file)
        self.DATABASE3.set(DATABASE3.file)
        self.options.set(options)



        clicked = StringVar()
        clicked.set("Select item")
        drop = OptionMenu(self, clicked, *options).grid(row=6, column = 0)
        mybutton = Button(self,text ='selection', command = lambda: StartPage.show(self,clicked)).grid(row=6,column =1)


        method = StringVar()
        list = ["energy","Other","Cost2"]
        drop = OptionMenu(self, method, *list).grid(row=7,column=0)
        confirm = Button(self, text= "confirm", command = lambda : self.display(method,files)).grid(row=7,column=1)


        #Graph_page = Button(self, text="GraphPage",
        #                command = lambda: Window.show_frame(self,GraphPage)).grid(row = 4)
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
    def show(self,clicked):
        print(clicked.get())
        selection1 = clicked.get()
        return


    def show1(self, files, method, var1,var2,var3,var4,var5):

        textA = Label(self, text = "Wind power: " + str(var1.get())).grid(row=8, column=3)
        textb = Label(self, text = "Solar PV: " + str(var2.get())).grid(row=9, column=3)
        textc = Label(self, text = "Solar Heat panels: " + str(var3.get())).grid(row=10, column=3)
        textd = Label(self, text = "Nuclear: " + str(var4.get())).grid(row=11, column=3)
        texte = Label(self, text = "Ground heat: " + str(var5.get())).grid(row=11, column=3)


        #list = {'Wind power': var1.get(), 'Solar PV':var2.get(),'Solar Heat panels':var3.get(),'Nuclear':var4.get()}
        print(files[1])
        files[1]['Wind power']= var1.get()
        files[1]['Solar PV']= var2.get()
        files[1]['Solar heat panels'] = var3.get()
        files[1]['Nuclear']= var4.get()
        files[1]['Ground_heat'] = var5.get()

        #{'Wind power': var1.get()}, {'Solar PV':var2.get()},{'Solar Heat panels':var3.get()},{'Nuclear':var4.get()})
        print(files[1])

        print('method', method.get())
        files = myfunctions.solar_electricity(self,files, method)
        files = myfunctions.solar_heat(self, files, method)
        files = myfunctions.H_storage(files)
        files = myfunctions.wind_energy(self,files,method)


        A = myfunctions.analysis(files)


    def display(self,method,files):

        self.selection = method.get()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()


        L = Label(self, text="What primary energies are there available?").grid(row = 3, column = 3)
        wind        = Checkbutton(self, text = "Wind power",        variable = var1).grid(row = 4, column = 3)
        solar_pv    = Checkbutton(self, text = "Solar PV",          variable = var2).grid(row = 4, column = 4)
        solar_heat  = Checkbutton(self, text = "Solar Heat panels", variable = var3).grid(row = 5, column = 3)
        nuclear     = Checkbutton(self, text = "Nuclear",           variable = var4).grid(row = 5, column = 4)
        Ground_heat = Checkbutton(self, text = "Ground heat",       variable = var5).grid(row = 6, column = 3)

        print("-----------------------------------")

        Save = Button(self, text = "Save selection", command = lambda: StartPage.show1(self, files, method,var1,var2,var3,var4,var5)).grid(row = 7, column = 3)





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
        self.file1 = controller.shared_data['file1']
        self.file2 = controller.shared_data['file2']
        self.options = controller.shared_data['options']
        #tk.Label(self, text = "selected file : ").grid(row=10) # text assigns a permanent value


        Back_to_home_btn = Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage)).grid(row = 3)



    def show(self):
        pass


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
