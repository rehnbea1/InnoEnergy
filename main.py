#fil för att skriva python kod

import myfunctions
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import ImageTk, Image
LARGE_FONT = ("Verdana", 12)
import pandas as pd

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

        container = tk.Frame(self, highlightbackground="black", highlightthickness=2)
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



        if getattr(sys, 'frozen', False):
            head_img = Image.open(
                os.path.join(sys._MEIPASS, "./House.png'"))
        else:
            head_img = Image.open("./House.png")




        self.image = head_img
        self.main_img = ImageTk.PhotoImage(self.image)
        label = Label(self, image = self.main_img)
        label.image = self.image
        label.pack(anchor = 'c')

        self.shared_data = {'file1':StringVar(), 'file2': StringVar(), 'DATABASE1': StringVar(), 'DATABASE2':StringVar(),'DATABASE3':StringVar(), 'options':StringVar(), 'Roof':StringVar()}

        self.frames = {}

        for F in (StartPage,PageOne,GraphPage):

            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew", padx=2, pady=2)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    print("––––––––––––––––––––––––––––––––––––––––––––––––StartPage–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
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
        self.file1 = None
        self.file2 = None
        self.DATABASE1 =None
        self.DATABASE2 =None
        self.DATABASE3 =None

        self.lighting_var  = StringVar()

        frame_width = 500

        self.frame1 = tk.Frame(self, width = frame_width, padx=5, pady=5)
        self.frame1.grid(row=0)

        self.frame2 = tk.Frame(self, width = frame_width)
        self.frame2.grid(row=1)

        self.frame3 = tk.Frame(self, width = frame_width, height=20)
        self.frame3.grid(row=2,ipady =5, ipadx=0)

        self.frame4 = tk.Frame(self, width = frame_width, height=20)
        self.frame4.grid(row=3,ipady =5,ipadx=0)

        self.frame5 = tk.Frame(self, width = frame_width, height=20)
        self.frame5.grid(row=4,ipady =5,ipadx=0)

        self.frame6 = tk.Frame(self, width = frame_width, height=20)
        self.frame6.grid(row=5,ipady =5,ipadx=0)

        self.frame7 = tk.Frame(self, width = frame_width, height=20)
        self.frame7.grid(row=6,ipady =5,ipadx=0)

        self.frame7 = tk.Frame(self, width = frame_width, height=20)
        self.frame7.grid(row=7,ipady =5,ipadx=0)


        #Frame one
        label = tk.Label(self.frame1,text="PageOne", font= LARGE_FONT)
        label.grid(row=0, column =0)

        Button1 = Button(self.frame1, text="Back to Home",
                        command = lambda: controller.show_frame(StartPage)).grid(row=0,column =1)

        Button2 = Button(self.frame1, text='Browse dynamic file',
                        command = lambda: self.delta1()).grid(row=0,column =2)

        Button3 = Button(self.frame1, text='Browse static file',
                        command = lambda: myfunctions.delta2(self)).grid(row = 0, column = 3)

        Button4 = Button(self.frame1,text="Print file 1",
                        command = lambda: myfunctions.show3(self)).grid(row=0,column =4)

        Button5 = Button(self.frame1, text ="Print file 2", command=lambda:myfunctions.show2(self))
        Button5.grid(row=0,column =5)

        #Frame two
        xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.grid(sticky="S")

        # Vertical (y) Scroll Bar
        yscrollbar = Scrollbar(self)
        yscrollbar.grid(sticky="E")

        # Text Widget
        self.text_box = Text(self.frame2,height=30, bg ="grey", wrap=NONE, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        self.text_box.configure(state='disabled')
        self.text_box.grid(sticky="EW" )

        # Configure the scrollbars
        xscrollbar.config(command=self.text_box.xview)
        yscrollbar.config(command=self.text_box.yview)

        label = self.text_entry('Please select files to begin!')
        #self.file1 = controller.shared_data['file1']
        #self.file2 = controller.shared_data['file2']
        #self.DATABASE1 = controller.shared_data['DATABASE1']
        #self.DATABASE2 = controller.shared_data['DATABASE2']
        #self.DATABASE3 = controller.shared_data['DATABASE3']
        #self.options = controller.shared_data['options']
        #self.Roof = controller.shared_data['Roof']
    #    self.lighting_var = controller.shared_data['lighting_var']

    def text_entry(self,string):
        self.text_box.configure(state='normal')
        self.text_box.insert(END,str(string) + "\n")
        self.text_box.configure(state='disabled')
        return

    def delta1(self):

        #Ta fram efter testning!!!!!
        file_1 = myfunctions.select_file()
        file_1 = myfunctions.check_file(self, file_1)
        file_info = self.text_entry("Your selection for File_1: "+ file_1)

        self.file1 = myfunctions.read_file(file_1)

        #DATA2 = myfunctions.read_file("/Users/albertrehnberg/Downloads/Static_Data.csv",gui)
        DATABASES = myfunctions.import_databases(self)


    def start_program(self):

        df = myfunctions.House(self)
        self.file1['spot-price €/kWh'] = [0.00213,0.00220,0.00217,0.0217,0.00222,0.00235,0.00421,0.001254,0.001451,0.001641,0.001650,0.001580,0.001490,0.001389,0.001439,0.001486,0.001611,0.002784,0.003543,0.003377,0.001559,0.001332,0.001288,0.001219]

        print("initial data")
        print(self.file1)
        print(self.file2)

        #save_data = myfunctions.Get_file_info(House_data[0], House_data[1])
        #stänger fönstret automatiskt nu
        #files  = [df[0],df[1],DATABASES[0],DATABASES[1],DATABASES[2]]

        self.options = myfunctions.get_graph_options(self)
        #self.files = [self.file1,self.file2,self.DATABASE1,self.DATABASE2,self.DATABASE3]

        #clicked = StringVar()
        #clicked.set("Select item")
        #drop = OptionMenu(self, clicked, *options).grid(row=6, column = 0, sticky="W")
        #mybutton = Button(self,text ='selection', command = lambda: self.show(self,clicked)).grid(row=6,column =1)

        print("is data still ok")
        print(self.file1)
        print(self.file2)

        method = StringVar()
        list = ["Default","Efficiency","Price"]
        drop = OptionMenu(self.frame4, method, *list).grid(row=0,column=0, sticky="W")
        confirm = Button(self.frame4, text= "confirm", command = lambda : self.display(method)).grid(row=0, column=1)
        #Graph_page = Button(self, text="GraphPage",
        #                command = lambda: Window.show_frame(self,GraphPage)).grid(row = 4)
        return FILE1, FILE2, DATABASE1, DATABASE2


        #Denna gör att filläsningsfunktionen kallas

        #my_label.pack()
        #file1.pack()
        #file2.pack()

    #def show(self,clicked):
    #    print(clicked.get())
    #    selection1 = clicked.get()
    #    return

    def display(self,method):

        method = method.get()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()

        L = self.text_entry("Select primary energy conversion methods")
        #L = Label(self, text="What primary energies are there available?").grid(row = 10, column = 0, columnspan=3, sticky='W')
        wind        = Checkbutton(self.frame5, text = "Wind power",        variable = var1).grid(row = 0, column = 0, sticky='W')
        solar_pv    = Checkbutton(self.frame5, text = "Solar PV",          variable = var2).grid(row = 0, column = 1, sticky='W')
        solar_heat  = Checkbutton(self.frame5, text = "Solar Heat panels", variable = var3).grid(row = 0, column = 2, sticky='W')
        nuclear     = Checkbutton(self.frame5, text = "Nuclear",           variable = var4).grid(row = 0, column = 3, sticky='W')
        Ground_heat = Checkbutton(self.frame5, text = "Ground heat",       variable = var5).grid(row = 0, column = 4, sticky='W')


        print("-----------------------------------")

        Save = Button(self.frame5, text = "Save selection", command = lambda: self.show1( method,var1,var2,var3,var4,var5)).grid(row = 12, sticky="SW")

    def show1(self, method, var1,var2,var3,var4,var5):

        textA = self.text_entry("Wind power: " + str(var1.get())+"\n")
        textB = self.text_entry("Solar PV: " + str(var2.get())+"\n")
        textC = self.text_entry("Solar Heat panels: " + str(var3.get())+"\n")
        textD = self.text_entry("Nuclear: " + str(var4.get())+"\n")
        textE = self.text_entry("Ground heat: " + str(var5.get())+"\n")


        #list = {'Wind power': var1.get(), 'Solar PV':var2.get(),'Solar Heat panels':var3.get(),'Nuclear':var4.get()}
        self.file2["None"]= var4.get()
        self.file2['Wind power']= var1.get()
        self.file2['Solar PV']= var2.get()
        self.file2['Solar heat panels'] = var3.get()
        self.file2['Nuclear']= var4.get()
        self.file2['Ground_heat'] = var5.get()

        #{'Wind power': var1.get()}, {'Solar PV':var2.get()},{'Solar Heat panels':var3.get()},{'Nuclear':var4.get()})


        myfunctions.solar_electricity(self, method)
        myfunctions.solar_heat(self, method)

        myfunctions.H_storage(self)

        myfunctions.lighting_consumtion(self)
        #Funkar hittills

        btn = Button(self.frame7, text="See results", command= lambda: myfunctions.analysis(self, method))
        btn.grid(sticky="W")


class GraphPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #label = tk.Label(self,text="GraphPage", font= LARGE_FONT)
        #label.grid(row=1,pady=10)
        self.file1 = controller.shared_data['file1']
        self.file2 = controller.shared_data['file2']
        self.options = controller.shared_data['options']

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
