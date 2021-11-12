#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
 #just nu bara en test-sida
import csv
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
import math




def delta2(self):
    file_2 = select_file()
    file_2 = check_file(self,file_2)
    file_info = self.text_entry("Your selection for File_2: "+ file_2)
    DATA2 = read_file(file_2)

    self.file2 = DATA2

    Button6 = Button(self.frame3, text="Start program", command = lambda: self.start_program()).grid(row=0,pady = 3)

    #ta fram före inlämning!!!!
    #House_data = Button(gui, text="calculate house data", command = lambda:House(gui,DATA1,DATA2)).grid(row=3, column = 0)
    #House_data = House(gui,DATA1,DATA2)  # läser fil 2 och startar programmet sen

def select_file():
    filetypes = (('csv-files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='downloads/',filetypes=filetypes)
    return filename

def read_file(filename):
    #fucked up csv reader because formatting
    try:
        file = pd.read_csv(filename, sep=';')
        return file


    except FileNotFoundError:
        self.text_entry("Error! Could not read the file, make sure you selected the right file")
        return False
    except UnicodeDecodeError:
        self.text_entry("Error! Could not decrypt the file, make sure you selected the right file")
        return False

def read_file2(filename):
    try:
        #For files without ; delimiter (normal csv)
        file = pd.read_csv(filename)
        return file

    except FileNotFoundError:
        self.text_entry("Error! Could not read the file, make sure you selected the right file")
        return False
    except UnicodeDecodeError:
        self.text_entry("Error! Could not decrypt the file, make sure you selected the right file")
        return False

def option_popup(self):

    Choice = tk.messagebox.askyesno(title="Option", message="Your file is invalid. Do you want to try again?")
    return Choice

def check_file(self, file):

    #checks if the file selected is ok
    file=str(file)
    if file.endswith('csv'):
        return file
    else:
        self.text_entry("Your selection is not a csv file")
        file = False
        while file == False:
            Choice = option_popup(self)
            if Choice == True:
                file = Select_file(gui)
                if file != '/.csv' :
                    file = False
                else:
                    file = file
            elif Choice == False:
                file = "Not selected"
                print("ok")
    return file

def import_databases(self):
    print("entered import_databases")

    if getattr(sys, 'frozen', False):
        self.DATABASE1 = pd.ExcelFile(
            os.path.join(sys._MEIPASS, "./Conversion Technologies Database.xlsx"))
        self.DATABASE2 = pd.ExcelFile(
            os.path.join(sys._MEIPASS, "./StorageTechnologies Database.xlsx"))
        self.DATABASE3 = pd.ExcelFile(os.path.join(sys._MEIPASS, "./End-Use technologies DataBase.xlsx"))
    else:
        self.DATABASE3 = pd.ExcelFile("./End-Use technologies DataBase.xlsx")
        self.DATABASE1 = pd.ExcelFile("./Conversion Technologies Database.xlsx")
        self.DATABASE2 = pd.ExcelFile("./StorageTechnologies Database.xlsx")


    #self.DATABASE1      =   pd.read_excel('/Users/albertrehnberg/Desktop/projekt/Conversion Technologies Database.xlsx'     ,sheet_name =None)
    #self.DATABASE2      =   pd.read_excel('/Users/albertrehnberg/Desktop/projekt/StorageTechnologies Database.xlsx'         ,sheet_name =None)
    #self.DATABASE3      =   pd.read_excel('/Users/albertrehnberg/Desktop/projekt/End-Use technologies DataBase.xlsx'        ,sheet_name =None)






    return

#def analysis(gui, data):
    print ("Analysis of:",data)
    Xaxis = []
    Yaxis = []
    for x in data:
        #print(data.get(x)[0])
        Xaxis.append(data.get(x)[0])
        Yaxis.append(data.get(x)[1])
    print("X", Xaxis)
    print("Y", Yaxis)
    plt.axis([0, 20, 0, 25]);
    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(Xaxis, Yaxis);
    #plt.plot(Xaxis,Yaxis)
    plt.show()

def House(self):
    print("---House---")
    df1 = self.file1
    df2 = self.file2
    DATABASE3 = self.DATABASE3


    print("df1 & df2 read correctly")

    #funktion för att insert flera static values här?
    Static_values = {'Uvalue_roof' : 0.08,'Uvalue_floor': 0.14}

    Area    =   df2['Length(m)']*df2['Depth(m)']*2 + df2['Length(m)']*df2['Height(m)']*2 + df2['Height(m)']*df2['Depth(m)']*2
    Volume  =   df2['Length(m)']*df2['Depth(m)']*df2['Height(m)']
    A_walls =   df2['Length(m)']*df2['Height(m)']*2 + df2['Height(m)']*df2['Depth(m)']*2
    WindowA =   A_walls * df2['Awindow/Awall']
    RnF     =   df2['Length(m)']*df2['Depth(m)']
    A_walls_no_win = A_walls - WindowA

    Static_values = {
    'Uvalue_roof' : 0.08,
    'Uvalue_floor': 0.14,
    'Area (m2)':Area,
    'Volume (m3)':Volume,
    'WindowA (m2)':WindowA,
    'RnF (m2)':RnF,
    'null_heat': 0

    }

    df2 = Add_par(df2, Static_values)
    heat_loss_radiation = A_walls_no_win * df2['Uwalls(W/m2K)'] + df2['WindowA (m2)'] * df2['Uwindows(W/m2K)'] + df2['RnF (m2)']* df2['Uvalue_floor'] + df2['RnF (m2)'] *df2['Uvalue_roof']
    df2 = Add_par(df2, {'heat_loss_radiation W':heat_loss_radiation})

    #Dynamic values

    df1 = HLC(df1, df2, heat_loss_radiation)
    df1 = calc_heat_w_e(self,df1, df2, DATABASE3)
    df1 = electricity_consumption(df1, df2)
    df1 = tot_energy_heating(df1, df2)
    df1 = cooling_need(df1,df2)
    df1 = heating_need(df1,df2)


    self.file1 = df1
    self.file2 = df2



    return

def Add_par(df2,static_values):
    #Function adds the static arguments from House function
    print("entered Add_par")
    for x in static_values:

        df2[x] = static_values[x]

    return df2
def HLC(df1,df2, heat_loss_radiation): #Negative means that it will need cooling!
    print("Entered function: HLC")
    #Calculate delta T
    #take delta T times U value
    temp_in = df2['Tinside(ºC)'][0]

    df1['DeltaT (°C)'] = df1['Temp'] - temp_in
    df1['H_loss (kW)'] = df1['DeltaT (°C)']*heat_loss_radiation[0]/1000
    return df1



def calc_heat_w_e(self,df1,df2, DATABASE3):

    print("entered heat water energy calculator")
    #funktion för att hitta temperaturen ur headern här?
    delta_t=40-df2['Twaterin(ºC)'][0]

    #calculate energy to heat up hot water:
    df1['Water(kWh)'] = df1['Hot Water @ 40 C'] * delta_t*4.186/3600

    eff = (df1['Water(kWh)']*1000).max()

    list =[]
    for index, row in DATABASE3['HotWater'].iterrows():

        if row['Power (W)'] >= eff and str(row['Final Energy']) == "Electricity":
            list.append(row)
        else:
            print("heater Error")
    print(list)
    list2 =[]
    for item in list:
        list2.append(item[4])

    minst = min(list2)

    for item in list:
        if item[4] == minst:
            print("Dennarad", item)

    df2['Waterheater'] = item[0]
    self.text_entry("Selected hot water heater: \n")
    self.text_entry(item)

    return df1

def electricity_consumption(df1, df2):
    #df1 = fix_formatting(df1,df2)

    df1['Cooking (MJ)'] = (df1['Cooking (MJ)']/3.6)
    df1 = df1.rename(columns={'Cooking (MJ)': 'Cooking_useful_e (kWh)'})
    df1['El.consumtion (kwh)'] = df1['Cooking_useful_e (kWh)']+df1['Electrical Applainces (kWh)']

    return df1   #Sums together cooking and electrical appliances!

def tot_energy_heating(df1, df2):
    print("Entered tot_energy_heating function")

    OHPH = int(df2['Qpeople(W)']) #Wh, Occupation_heat_per_hour

    air_losses = calculate_air_heat_losses(df1,df2)
    print("Air_losses", air_losses)
    df1['Heat_e (kWh)'] = ((df1['%AreaHeatingCooling']/100 * df2['Area (m2)'][0] + df1['Occupation'] * OHPH) /1000)-df1['H_loss (kW)'] - air_losses

    #df1.loc[df1['Occupation'] == 0, 'Heat_e (kWh)'] = df1['Heat_e (kWh)'][0]*0,5

    return df1 #Fixed 8.11

def calculate_air_heat_losses(df1,df2):
    Volume_per_hour = df2['Air Changes/hour (h^-1)'][0] * df2['Volume (m3)'][0]
    list = []
    Air_heat_capacity = 1.012/1000 #*10^-3 kJ/kgK
    thermal_recovery = 0.8 #%of heat
    Air_density = 1.2

    for index, row in df1.iterrows():
        delta_t = abs(df2['Tinside(ºC)'][0] - row['Temp'])

        Air_heating = Volume_per_hour * (1-thermal_recovery) * delta_t * Air_heat_capacity * Air_density

        list.append(Air_heating)
    return list

def cooling_need(df1,df2):
    df1["Cooling (kWh)"] = df1['Heat_e (kWh)']

    df1.loc[df1["Cooling (kWh)"] > 0, "Cooling (kWh)"] = 0
    return df1

def heating_need(df1,df2):
    df1["Heating (kWh)"] = df1['Heat_e (kWh)']

    df1.loc[df1["Heating (kWh)"] < 0, "Heating (kWh)"] = 0
    return df1

def lighting_consumtion(self):

    lumens = self.file1['Lighting (lux)'] * self.file2['Height Lights (m)'][0] ** 2
    A = lumens/self.file1['Total lapms'] #gives lumen demand per light bulb

    lum_max = A.max()

    list =[]
    for index, row in self.DATABASE3['Lighting'].iterrows():
        if row['Lumens (lm)'] >= A.max():
            list.append((index, row))
    print(list)

    label1 = self.text_entry("Found following suitable lamps: \n")
    for item in list:
        label3 = self.text_entry( str(item) + "\n")


    self.text_entry("Select your lighting application \n")
    entry = StringVar()
    label_box   = Label(self.frame6, text="insert lamp selection (choose the index)").grid(row=1,column=0)
    box         = Entry(self.frame6, textvariable = entry).grid(row=1,column=1)
    confirm     = Button(self.frame6, text= "Submit", command = lambda : submit(self,entry, list)).grid(row=1,column=2)
    return


def submit(self,entry, list):

    print("Entered submit")
    a = int(entry.get())
    print("a-----",a)
    self.text_entry("Select your lighting application2 \n")
    x = 0
    for i in range(len(list)):
        print("item",list[i][0])
        if list[i][0]== a:
            item = list[i]
            #print("item[0]",list[item])
            label4 = self.text_entry(("Submitted: \n" + str(item)))

            self.file2['lighting_var']=item[1]
            power = item[1][3]


            self.file1 = self.file1.rename(columns={'Lighting (lux)':'Lighting (kWh)'})
            self.file1['Lighting (kWh)'] = self.file1['Total lapms']*power/1000
            print(self.file1)
            x = 1

    if x ==0:
        self.text_entry("Could not find your selection\n")




def solar_heat(self, method):
    print("---method----", method)

    if int(self.file2['Solar heat panels'])==1:
        if method == "Efficiency":
            if int(self.file2['Solar PV']) == 1:
                Roof_area = 0.4
            else:
                Roof_area = 0.8

            candidates=[]

            eff = float(self.DATABASE1['Solar Thermal']['Efficiency'].max())

            for index, row in self.DATABASE1['Solar Thermal'].iterrows():

                if row['Efficiency'] == eff:
                    candidates.append((index,row['Name']))


            panel_efficiency = eff

            #self.file1['sol_h_prod (kWh)'] = self.file1['Rad (W/m^2)'] * Roof_area * self.file2['RnF (m2)'][0] * panel_efficiency/1000

            self.text_entry("Select your Solar thermal colector \n")
            for item in candidates:
                label3 = self.text_entry( str(item) + "\n")

            entry1 = StringVar()
            lbl = Label(self.frame7,text = "Solar heat panel selection (choose index from the list)")
            lbl.grid(row=0,column=0,sticky="W")
            box = Entry(self.frame7, textvariable = entry1).grid(row =0,column=1 ,sticky="E")
            confirm2 = Button(self.frame7, text= "Submit", command = lambda : submit_heate(self,entry1, candidates, Roof_area))
            confirm2.grid(row=0,column=2,sticky="E")

            return  #Fixed 7.11


        elif method == "Price":
            print("Entered price")

            if int(self.file2['Solar PV']) == 1:

                Roof_area = 0.4
            else:
                Roof_area = 0.8


            list=[]
            eff = self.DATABASE1['Solar Thermal']['Price (€)'].min()

            for index, row in self.DATABASE1['Solar Thermal'].iterrows():
                if row['Price (€)'] == eff:
                    list.append((index, row))

            self.text_entry("----- Select your Solar thermal colector  ----- \n")
            self.text_entry("                              \n")
            for item in list:
                label3 = self.text_entry( str(item) + "\n")

            entry1 = StringVar()
            lbl = Label(self.frame7,text = "Solar heat panel selection (choose index form the list)")
            lbl.grid(row=0,column=0,sticky="W")
            box = Entry(self.frame7, textvariable = entry1).grid(row =0,column=1 ,sticky="E")
            confirm2 = Button(self.frame7, text= "Submit", command = lambda : submit_heate(self,entry1, list, Roof_area))
            confirm2.grid(row=0,column=2,sticky="E")



        elif method =="Default":

            if int(self.file2['Solar PV']) == 1:

                Roof_area = 0.4
            else:
                Roof_area = 0.8

            list=[]
            eff = float(self.DATABASE1['Solar Thermal']['Efficiency'].max())
            for index, row in self.DATABASE1['Solar Thermal'].iterrows():
                if row['Efficiency'] == eff:
                    print("---------",row)
                    list.append((index, row['Name'],row['Efficiency']))

            label2 = self.text_entry("Your Solar Thermal panel selection")
            label3 = self.text_entry( str(list[0]) + "\n")

            panel_efficiency = eff

            #panel_efficciency = energy_supply('solar_heat','efficiency')

            self.file1['sol_h_prod (kWh)'] = self.file1['Rad (W/m^2)'] * Roof_area * self.file2['RnF (m2)'][0] * panel_efficiency/1000

        else:
            print("-Error with method-")
    else:
        print("Error with method")
        return



def submit_heate(self,entry1, list, Roof_area):
    print("entered submit heate")
    a = int(entry1.get())
    for item in list:
        print("a",a)
        print("item",item)
        if item[0] == a:
            label4 = self.text_entry(("Submitted: \n" + str(item)))

            panel_efficiency = item[3]
            self.file2['Heat_panel'] = list[0][0]
            self.file1['sol_h_prod (kWh)'] = self.file1['Rad (W/m^2)'] * Roof_area * self.file2['RnF (m2)'][0] * panel_efficiency/1000

    return



def solar_electricity(self, method):

    if int(self.file2['Solar PV'])==1:

        if method == "Efficiency":

            if int(self.file2['Solar heat panels']) == 1:
                Area_var = 0.4
            else:
                Area_var = 0.8
            #print(files[0])
            #print(self.DATABASE1['Solar PV'])
            #print(type(self.DATABASE1))
            candidates=[]
            eff = float(self.DATABASE1['Solar PV']['Efficiency'].max())

            for index, row in self.DATABASE1['Solar PV'].iterrows():

                if row['Efficiency'] == eff:
                    candidates.append((index,row['Name']))

            selection = self.text_entry("Your Solar PV selection:\n" + str(candidates[0]) + "\n")

            panel_efficiency = eff
            self.file1['sol_e_product (kWh)'] = self.file1['Rad (W/m^2)'] * self.file2['RnF (m2)'][0] * Area_var * panel_efficiency/1000

            return  #Fixed 7.11

        elif method =="Price":

            if int(self.file2['Solar heat panels']) == 1:
                Area_var = 0.4
            else:
                Area_var = 0.8

            candidates=[]
            eff = []
            price = float(self.DATABASE1['Solar PV']['Price (€)'].min())

            for index, row in self.DATABASE1['Solar PV'].iterrows():

                if row['Price (€)'] == price:
                    candidates.append((index,row['Name']))
                    eff.append(row['Efficiency'])

            selection = self.text_entry("Your Solar PV selection: \n" + str(candidates[0])+"\n")

            panel_efficiency = eff
            self.file1['sol_e_product (kWh)'] = self.file1['Rad (W/m^2)'] * self.file2['RnF (m2)'][0] * Area_var * float(eff[0])/1000
            return

        elif method == "Default":

            if int(self.file2['Solar PV']) == 1:
                Area_var = 0.4
            else:
                Area_var = 0.8


            candidates=[]
            eff = float(self.DATABASE1['Solar PV']['Efficiency'].max())

            for index, row in self.DATABASE1['Solar PV'].iterrows():

                if row['Efficiency'] == eff:
                    candidates.append((index,row['Name']))

            selection = self.text_entry("Your Solar PV selection: \n" + str(candidates[0])+"\n")

            panel_efficiency = eff
            self.file1['sol_e_product (kWh)'] = self.file1['Rad (W/m^2)'] * self.file2['RnF (m2)'][0] * Area_var * panel_efficiency/1000 #
            return #Fixed 7.11
        else:
            return
            print("eller fel här")

    else:
        print("Fel här")
        return


def wind_energy(self, method):
    #finds the wind generator with the closest max speed to the cut of speed, in other words the one with a peak capacity that is most optimised to the current wind

    if int(self.file2['Wind power'])==1:

        print(self.file2)
        print(self.DATABASE1)
        #print(files[0])
        #print(type(self.DATABASE1))
        candidates={}

        #print( self.DATABASE1['Solar PV']['Efficiency'].max())
        wind_max = float(self.file2['Wind speed'].max())
        wind_min = float(self.file2['Wind speed'].min())

        for index, row in self.DATABASE1['Wind Turbine'].iterrows():
            print("-----------------")

            cut_of_ratio = wind_max/int(row['Cut-off speed (m/s)'])

            if cut_of_ratio < 1.0 and float(row['Initial speed (m/s)']) < float(wind_min):
                candidates[index] = cut_of_ratio
                print("cor", cut_of_ratio)



                best = max(candidates.values())

                print(candidates)



                for item in candidates.items():

                    if item[1] == best:
                        selection = self.DATABASE1['Wind Turbine'].iloc[item[0]]['Name']

                    else:
                        pass

                selection = self.text_entry("Your Wind power selection:" + str(selection))

                Air_density = 1.2 #kg/m3
                efficiency = 0.5
                Area = 3.14*1.5**2 #pi*1,5m

                self.file2['Wind_e_prod (kWh)'] = Air_density * 0.5 * (self.file2['Wind speed'])**3 * efficiency * Area/1000


            else:
                print("no suitable wind power alternatives")
                return

            return
         #Fixed 7.11

    else:
        return



def H_storage(self):

    if int(self.file2['Solar heat panels']) == 1 and int(self.file2['Ground_heat']) == 1 :

        print("entered heat_storage")

        self.file1['Heat_storage (kWh)'] = 0
        storage = {}

        storage['energy_shortage (kWh)'] = self.file1['Heat_e (kWh)']+self.file1['sol_h_prod (kWh)']

        place_holder = []
        place_holder.append(0)
        #print("range",range(len(storage['Demand (kWh)'])))
        for x in range(len(storage['energy_shortage (kWh)'])):

            A = storage['energy_shortage (kWh)'][x]
            B = self.file1['Heat_storage (kWh)'][x]
            C = B+A
            print(C)

            if  C > 0:
                #adds value to storage
            #    print("PH minus1",place_holder[-1])
                c = place_holder[-1]+C
            #    print("this is smol C", c)
                place_holder.append(c)
            #    print("PH+",place_holder)

            elif C < 0:
            #    print("c mindre än noll")
                #withdraws maximum amount from storage
                if place_holder[-1] > 0:
            #        print("PH-1",place_holder)
                    D = place_holder[-1]+2*C
                    #effekt 0,5 alltså dubbel stress på batteriet
                    if D > 0:
            #            print("PH-2",place_holder)
                        place_holder.append(D)
                    elif D < 0 :
                        place_holder.append(0)
            #            print("more power still needed, this much is left: ", D)
                elif place_holder[-1] < 0:
                    place_holder.append(0)
            #        print("placeholder index is smaller than 0?")

                elif place_holder[-1] == 0:
                    place_holder.append(0)

            else:
                place_holder.append(0) == 0
            #print("place_holder", place_holder)
        place_holder.pop(0)
        self.file1['Heat_storage (kWh)'] = place_holder


        return
    else:
        print("No heat production available to store!")
        return  #Fixed 8.11



def get_graph_options(self):
    print("entered get_graph_options")
    print(self.file1.columns)
    print(self.file2.columns)


    headers = self.file1.columns, self.file2.columns, self.DATABASE1.keys(), self.DATABASE2.keys(), self.DATABASE3.keys()
    print(headers)
    return headers
def show3(self):
    #for row in self.file1.iterrows():
    self.text_entry(self.file1)
    #print(self.file1)
    return
def show2(self):
    self.text_entry("––––––––––––––––––––––––––––––––––––––")
    self.text_entry(self.file2)
    return

def analysis(self, method):
    print("entered analysis")
    print("––––––––––––––––––––––––––––––––––––––")

    Data = [self.file1,self.file2]
    Databases = [self.DATABASE1,self.DATABASE2,self.DATABASE3]

    cooking_application(self, method)
    heating_solution(self,method)
    total_electricity(self)
    print("––––––––––––––––––––––––––––––––––––––")

def cooking_application(self, method):
    if method == "Efficiency":
        A_max = float(self.DATABASE3['Cooking']['Efficiency'].max())
        list =[]

        for index, row in self.DATABASE3['Cooking'].iterrows():

            if row['Efficiency'] == A_max and str(row['Final Energy']) == 'Electricity':
                list.append((index,row))


        self.text_entry("Your Cooking device: \n")
        self.text_entry(list[0][1])
        cooker_eff = list[0][1][4]


        print("cooceff",cooker_eff)
        print("--------------------------------")

        self.file1['Cooker_final_e'] = self.file1['Cooking_useful_e (kWh)']/cooker_eff
        self.file2['Cooker'] = list[0][0]

    if method == "Price":
        A_max = float(self.DATABASE3['Cooking']['Price (€)'].min())
        list =[]
        print(self.DATABASE3['Cooking'])
        for index, row in self.DATABASE3['Cooking'].iterrows():

            if row['Price (€)'] == A_max and str(row['Final Energy']) == 'Electricity':
                list.append((index,row))

        self.text_entry("Your Cooking device: \n")
        self.text_entry(list[0][1])
        cooker_eff = list[0][1][4]


        print("list",list)[4]




        self.file1['Cooker_final_e'] = self.file1['Cooking_useful_e (kWh)']/cooker_eff
        self.file2['Cooker'] = list[0][0]

    if method == "Default":
        A_max = float(self.DATABASE3['Cooking']['Efficiency'].max())
        list =[]
        print(self.DATABASE3['Cooking'])

        for index, row in self.DATABASE3['Cooking'].iterrows():

            if row['Efficiency'] == A_max and str(row['Final Energy']) == 'Electricity':
                list.append((index,row))


        self.text_entry("Your Cooking device: \n")
        self.text_entry(list[0][1])
        cooker_eff = list[0][1][4]

        self.file1['Cooking_final_e'] = self.file1['Cooking_useful_e (kWh)']/cooker_eff
        self.file2['Cooking'] = list[0][0]

def heating_solution(self,method):

    A       = self.DATABASE3['SpaceHeatingCooling']['Thermal PowerHeating (W)']
    A_COP   = A.max()
    B       = self.DATABASE3['SpaceHeatingCooling']['Efficiency Heating']
    Watt_H  = A/B
    C       = self.DATABASE3['SpaceHeatingCooling']['Thermal PowerCooling (W)']
    C_COP   = C.max()
    D       = self.DATABASE3['SpaceHeatingCooling']['Efficiency Cooling']
    Watt_C  = C/D
    heat_best = max(Watt_H)/1000
    cool_best = max(Watt_C)/1000

    print("HB",heat_best) #COP HB 2.444

    print("CB",cool_best) #CB 2.115


    E = 0
    F = 0
    for i in range(len(Watt_H)):
        if Watt_H[i]==heat_best:
            E = i
    for j in range(len(Watt_C)):
        if Watt_C[i]==cool_best:
            F = j

    #Implement controll for heating and cooling depending on sign if time left
    #for row in self.file1['Heat_e (kWh)']:
        #if row < 0:
            #print(row)

    if self.file2['Solar heat panels'][0] == 1 and self.file2['Ground_heat'][0] == 0:
        list=[]
        E_from_panels =[]

        heat_need = self.file1['Heating (kWh)']

        for q in range(len(heat_need)):
            print(heat_need[q])
            row = heat_need[q]
            panel = self.file1.iloc[q]['sol_e_product (kWh)']
            if row > 0 and panel>0:
                    row1 = row - panel

                    if row1 < 0 :
                        E_from_panels.append(panel-row)
                        list.append(0)
                    elif row1 > 0 :
                        E_from_panels.append(row1)
                        list.append(row1)
                    else:
                        E_from_panels.append(0)
                        list.append(0)
            else:
                list.append(0)
                E_from_panels.append(0)
        for item in list:
            kWhs_needed = item/A_COP
            item = kWhs_needed * heat_best

        self.file1["Heater_e_consumpt"] = list
        self.file1['Energy_from_panels'] = E_from_panels

        selection = self.DATABASE3['SpaceHeatingCooling'].iloc[i]
        self.file2['Heating_solution']= E

        self.text_entry('Your selection for heating and cooling is:')
        self.text_entry(selection)


    elif self.file2['Solar heat panels'][0] == 0 and self.file2['Ground_heat'][0] == 0:
        list =[]
        tot_heat = self.file1['Heating (kWh)']
        for row in tot_heat:
            kWhs_needed = row/A_COP
            row = kWhs_needed * heat_best
            list.append(row)

        print("list här", list)
        self.file1["Heater_e_consumpt"] = list

        selection = self.DATABASE3['SpaceHeatingCooling'].iloc[i]
        self.file2['Heating_solution']= E

        self.text_entry('Your selection for heating and cooling is:')
        self.text_entry(selection)


    elif self.file2['Solar heat panels'][0] == 1 and self.file2['Ground_heat'][0] == 1:
        list =[]
        E_from_battery = []


        heat_need = self.file1['Heating (kWh)']

        for q in range(len(heat_need)):
            print(heat_need[q])
            row = heat_need[q]
            battery = self.file1.iloc[q]['Heat_storage (kWh)']
            if row > 0 and panel>0:
                    row1 = row - panel

                    if row1 < 0 :
                        E_from_battery.append(panel-row)
                        list.append(0)
                    elif row1 > 0 :
                        E_from_battery.append(row1)
                        list.append(row1)
                    else:
                        list.append(0)
                        E_from_battery.append(0)
            else:
                list.append(0)
                E_from_battery.append(0)

        for item in list:
            kWhs_needed = item/A_COP
            item = kWhs_needed * heat_best

        self.file1["Heater_e_consumpt"] = list
        self.file1['Energy_from_battery'] = E_from_battery

        selection = self.DATABASE3['SpaceHeatingCooling'].iloc[i]
        self.file2['Heating_solution']= E

        self.text_entry('Your selection for heating and cooling is:')
        self.text_entry(selection)

    elif self.file2['Solar heat panels'][0] == 0 and self.file2['Ground_heat'][0] == 1:

        list =[]
        tot_heat = self.file1['Heating (kWh)']
        for row in tot_heat:
            kWhs_needed = row/A_COP
            row = kWhs_needed * heat_best
            list.append(row)

        print("list här", list)
        self.file1["Heater_e_consumpt"] = list

        selection = self.DATABASE3['SpaceHeatingCooling'].iloc[i]
        self.file2['Heating_solution']= E

        self.text_entry('Your selection for heating and cooling is:')
        self.text_entry(selection)


                #Användbar kod
                #i = self.DATABASE3['SpaceHeatingCooling']['Efficiency Heating'].argmax()
                #selection = self.DATABASE3['SpaceHeatingCooling'].iloc[i]['Name']
    else:
        print("unexpected error")



def total_electricity(self):
    print(self.file2)
    p_energies = [self.file2['Wind power'], self.file2['Solar PV'], self.file2['Solar heat panels'], self.file2['Nuclear'], self.file2['Ground_heat']]

    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')
    Total1 = self.file1['El.consumtion (kwh)'].sum()

    self.text_entry('Heating needs (kWh/day)                      :')
    tot_heat = self.file1['Heating (kWh)'].sum()
    self.text_entry(tot_heat)

    self.text_entry('Total electricity use for electric appliances:')
    tot_el_app = self.file1['Electrical Applainces (kWh)'].sum()
    self.text_entry(tot_el_app)

    self.text_entry(':Cooling needs (kWh/day)                     :')
    tot_cool = self.file1['Cooling (kWh)'].sum()
    self.text_entry(tot_cool)

    self.text_entry(':Hot Water needs (kWh/day)                    :')
    tot_w_heat = self.file1['Water(kWh)'].sum()
    self.text_entry(tot_w_heat)

    tot_heat_cool_e_prim = self.file1['Heat_e (kWh)'].sum()

    self.text_entry(':Cooking needs (kWh/day                      :')
    tot_cooking = self.file1['Cooking_useful_e (kWh)'].sum()
    self.text_entry(tot_cooking)

    self.text_entry(':Lighting (kWh/day                           :')
    tot_light = self.file1['Lighting (kWh)'].sum()
    self.text_entry(tot_light)

    self.text_entry(':Total Final Energy (gas/day)                :')
    self.text_entry(0)

    self.text_entry(':Total Final Biomass (gas/day)               :')
    self.text_entry(0)
    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')

    self.text_entry(':Total Primary Energy (in kWh/day)           :')
    tot_prim_e = tot_cooking + tot_light + tot_el_app+ tot_heat_cool_e_prim + tot_w_heat
    self.text_entry(tot_prim_e)
    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')
    self.text_entry(':Total Cost (in €/day)                       :')


    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')
    self.text_entry(':Total Final Energy (electricity/day)        :')
    tot_final_e = tot_cooking + tot_light + tot_el_app+ + tot_heat + tot_cool + tot_w_heat
    self.text_entry(tot_final_e)

    #Dessa två ger en massa intressant statistik osv
    #print(df1.describe())
    #print(df2.describe())

    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')
    self.text_entry(':                                            :')
    self.text_entry('Total electricity use for heating            :')
    tot_e_for_heat = self.file1['Heater_e_consumpt'].sum()
    self.text_entry(tot_e_for_heat)
    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')

    self.text_entry(':                                            :')
    self.text_entry('Total energy in total                        :')
    tot_tot = tot_cooking + tot_light+tot_el_app+tot_w_heat+tot_heat_cool_e_prim
    self.text_entry(tot_tot)
    self.text_entry(':––––––––––––––––––––––––––––––––––––––––––––:')
