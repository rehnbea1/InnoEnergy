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
from PIL import ImageTk, Image
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
        tk.Tk.wm_title(self,"Energy Management System ")

        container = tk.Frame(self, background = "grey", highlightbackground="black", highlightthickness=3)
        container.pack(side="bottom", fill="both",expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #my_canvas = Canvas(container)
        #my_canvas.pack(fill="both",expand=True)
        #my_scrollbar = ttk.Scrollbar(self, orient="vertical", command = my_canvas.yview)
        #my_scrollbar.pack(side=RIGHT,fill=Y)
        #my_canvas.configure(yscrollcommand=my_scrollbar.set)
        #my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        #second_frame = tk.Frame(my_canvas)
        #my_canvas.create_window((0,0),window=second_frame,anchor="nw")

#       my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command = my_canvas.yscrollcommand).pack(side=RIGHT,fill=Y)

        self.geometry("7000x700")


        self.image = Image.open('House.png')
        self.main_img = ImageTk.PhotoImage(self.image)
        label = Label(self, image = self.main_img)
        label.image = self.image
        label.pack(anchor = 'c')

        self.shared_data = {'file1':StringVar(), 'file2': StringVar(), 'DATABASE1': StringVar(), 'DATABASE2':StringVar(),'DATABASE3':StringVar(), 'options':StringVar(), 'Roof':StringVar()}

        self.frames = {}

        for F in (StartPage,PageOne,GraphPage):

            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew", padx=5, pady=5)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)


        label = tk.Label(self,text="StartPage", font= LARGE_FONT)
        label.grid(row=0,sticky="NW")

        Page_two = Button(self, text="PageOne",
                        command = lambda: controller.show_frame(PageOne)).grid(row =1,sticky='SW')

        Graph_page = Button(self, text="GraphPage",
                        command = lambda: controller.show_frame(GraphPage)).grid( sticky='SW')

        destroy = Button(self,text="Exit program",
                        command = lambda: gui.destroy()).grid( sticky='SW')

        #tk.Frame(self, highlightbackground="green", highlightcolor="green", highlightthickness=5)



        #controller.shared_data.update({'options':options})
        #geography =  sticky='NW', padx=5, pady=5









class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.text_box = Text(self,width=80, height=10, bg ="grey",)
        self.text_box.configure(state='disabled')
        self.text_box.grid()

        label = tk.Label(self,text="PageOne", font= LARGE_FONT)
        label.grid(sticky='NW', padx=2, pady=2)

        Button1 = Button(self, text="Back to Home",
                        command = lambda: controller.show_frame(StartPage)).grid(row = 1, sticky='NW', padx=2, pady=2)
        Button2 = Button(self, text='Browse file_1',
                        command = lambda: self.Delta1()).grid(sticky='SW', padx=2, pady=2)



        #self.file1 = controller.shared_data['file1']
        #self.file2 = controller.shared_data['file2']
        #self.DATABASE1 = controller.shared_data['DATABASE1']
        #self.DATABASE2 = controller.shared_data['DATABASE2']
        #self.DATABASE3 = controller.shared_data['DATABASE3']
        #self.options = controller.shared_data['options']
        #self.Roof = controller.shared_data['Roof']

    def text_entry(self,string):
        self.text_box.configure(state='normal')
        self.text_box.insert(END,str(string) + "\n")
        self.text_box.configure(state='disabled')
        return


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
        df[0]['spot-price €/kWh'] = [0.00213,0.00220,0.00217,0.0217,0.00222,0.00235,0.00421,0.001254,0.001451,0.001641,0.001650,0.001580,0.001490,0.001389,0.001439,0.001486,0.001611,0.002784,0.003543,0.003377,0.001559,0.001332,0.001288,0.001219]

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

        options = myfunctions.get_graph_options(FILE1,FILE2, DATABASE1,DATABASE2)

        self.file1 =FILE1.file
        self.file2 =FILE2.file
        self.DATABASE1 =DATABASE1.file
        self.DATABASE2 =DATABASE2.file
        self.DATABASE3 =DATABASE3.file
        self.options = options
        self.files = [self.file1,self.file2,self.DATABASE1,self.DATABASE2,self.DATABASE3]



        clicked = StringVar()
        clicked.set("Select item")
        drop = OptionMenu(self, clicked, *options).grid(row=6, column = 0, sticky="W")
        mybutton = Button(self,text ='selection', command = lambda: self.show(self,clicked)).grid(row=6,column =1)


        method = StringVar()
        list = ["Default","Efficiency","Price"]
        drop = OptionMenu(self, method, *list).grid(row=7,column=0, sticky="W")
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

    def display(self,method,files):

        self.selection = method.get()
        print("metoodju", self.selection)

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()


        L = self.text_entry("Select primary energy sources")
        #L = Label(self, text="What primary energies are there available?").grid(row = 10, column = 0, columnspan=3, sticky='W')
        wind        = Checkbutton(self, text = "Wind power",        variable = var1).grid(row = 11, column = 0, sticky='W')
        solar_pv    = Checkbutton(self, text = "Solar PV",          variable = var2).grid(row = 11, column = 1, sticky='W')
        solar_heat  = Checkbutton(self, text = "Solar Heat panels", variable = var3).grid(row = 11, column = 2, sticky='W')
        nuclear     = Checkbutton(self, text = "Nuclear",           variable = var4).grid(row = 11, column = 3, sticky='W')
        Ground_heat = Checkbutton(self, text = "Ground heat",       variable = var5).grid(row = 11, column = 4, sticky='W')


        print("-----------------------------------")

        Save = Button(self, text = "Save selection", command = lambda: self.show1(files, method,var1,var2,var3,var4,var5)).grid(row = 12, sticky="SE")

    def show1(self, files, method, var1,var2,var3,var4,var5):

        textA = self.text_entry("Wind power: " + str(var1.get())+"\n")
        textB = self.text_entry("Solar PV: " + str(var2.get())+"\n")
        textC = self.text_entry("Solar Heat panels: " + str(var3.get())+"\n")
        textD = self.text_entry("Nuclear: " + str(var4.get())+"\n")
        textE = self.text_entry("Ground heat: " + str(var5.get())+"\n")


        #list = {'Wind power': var1.get(), 'Solar PV':var2.get(),'Solar Heat panels':var3.get(),'Nuclear':var4.get()}
        print(files[1])
        files[1]["None"]= var4.get()
        files[1]['Wind power']= var1.get()
        files[1]['Solar PV']= var2.get()
        files[1]['Solar heat panels'] = var3.get()
        files[1]['Nuclear']= var4.get()
        files[1]['Ground_heat'] = var5.get()

        #{'Wind power': var1.get()}, {'Solar PV':var2.get()},{'Solar Heat panels':var3.get()},{'Nuclear':var4.get()})
        print(files[1])
        method = method.get()

        print("---––––––––––––––––––––––––")
        files = myfunctions.solar_electricity(self, method)
        myfunctions.solar_heat(self,method)
        myfunctions.H_storage(self)

        print("Files just nu")
        print(self.files)
        myfunctions.lighting_consumtion(self)
        myfunctions.analysis(self)




class GraphPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="GraphPage", font= LARGE_FONT)
        label.grid(row=1,pady=10)
        self.file1 = controller.shared_data['file1']
        self.file2 = controller.shared_data['file2']
        self.options = controller.shared_data['options']
        #tk.Label(self, text = "selected file : ").grid(row=10) # text assigns a permanent value


        Back_to_home_btn = Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage)).grid(sticky='NE', padx=2, pady=2)


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
