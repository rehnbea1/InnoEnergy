#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida
import csv
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
import pandas as pd




#def Delta2(gui, DATA1):
    #file_2 = Select_file(gui)
    #file_2 = Check_file(file_2,gui)
    #file_info = Label(gui,text="Your selection for File_2: "+ file_2)
    #file_info.grid(row = 2, column = 1, pady = 5)

    #DATA2 = Read_file2(file_2,gui)
    #radera kanske?
    #disp_data2 = Button(gui, text='Display data', command = lambda:myfunctions.show_data(gui,DATA)).grid(row=3, column = 1)

    #ta fram före inlämning!!!!
    #House_data = Button(gui, text="calculate house data", command = lambda:House(gui,DATA1,DATA2)).grid(row=3, column = 0)
    #House_data = House(gui,DATA1,DATA2)

def select_file(gui):
    filetypes = (('csv-files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='downloads/',filetypes=filetypes)
    return filename

def read_file(filename,gui):

    file = pd.read_csv(filename, sep=';')
    #fucked up csv reader because formatting

    print("Entered: Read_file")
    return file

def read_file2(gui, filename):
    #For files without ; delimiter (normal csv)
    file = pd.read_csv(filename)
    print("Entered: Read_file2")
    return file
    #try:

    #except FileNotFoundError:
    #    Label(gui,text="Error! Could not read the file, make sure you selected the right file").pack()
    #    return False
    #except UnicodeDecodeError:
    #    Label(gui,text="Error! Could not decrypt the file, make sure you selected the right file").pack()
    #    return False
    return

def option_popup(gui):

    Choice = tk.messagebox.askyesno(title="Option", message="Your file is invalid. Do you want to try again?")
    return Choice

def Check_file(file,gui):

    #checks if the file selected is ok
    file=str(file)
    if file.endswith('csv'):
        return file
    else:
        print("this is not a csv file")
        file = False
        while file == False:
            Choice = option_popup(gui)
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

def show_data(gui,data):
    i=5
    a = len(data.keys())
    print("show_data")
    for x in range(a):

        Label(gui, text=data[x]).grid(row=i, column=0)
        i+=1
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

def House(gui, df1, df2):
    print("Entered: House function")

#Length(m)	Depth(m)	Height(m)	Uwalls(W/m2K)	Uwindows(W/m2K)	Awindow/Awall	Air Changes/hour (h^-1)	Tinside(ºC)	Twaterin(ºC)	Qpeople(W)	Window Solar Gain	Height Lights (m)
#10	5	3	1	2	0.2	0.5	2	20	120	0.25	1.May

    #print("df1")
    #print(df1)
    #print("df2")
    #print(df2)
    print("df1 & df2 read correctly")

    #funktion för att insert flera static values här?
    Static_values = {'Uvalue_roof' : 0.08,'Uvalue_floor': 0.14,'Water_in':20}

    Area    =   df2['Length(m)']*df2['Depth(m)']*2 + df2['Length(m)']*df2['Height(m)']*4
    Volume  =   df2['Length(m)']*df2['Depth(m)']*df2['Height(m)']
    WindowA =   Area - ((df2['Length(m)']*df2['Height(m)'])*4) * df2['Awindow/Awall']
    RnF     =   df2['Length(m)']*df2['Depth(m)']

    Static_values = {
    'Uvalue_roof' : 0.08,
    'Uvalue_floor': 0.14,
    'Area (m2)':Area,
    'Volume (m3)':Volume,
    'WindowA (m2)':WindowA,
    'RnF (m2)':RnF,
    'null_heat': 0

    }
    #Static_values = {'Uvalue_roof' : 0.08,'Uvalue_floor': 0.14,'Water_in':20,'Area':Area,'Volume':Volume, 'WindowA':WindowA, 'RnF':RnF, 'heat_loss_radiation': heat_loss_radiation}
    df2 = Add_par(df2, Static_values)
    heat_loss_radiation = df2['Area (m2)'] * df2['Uwalls(W/m2K)'] + df2['WindowA (m2)'] * df2['Uwindows(W/m2K)'] + df2['RnF (m2)']* df2['Uvalue_floor'] + df2['RnF (m2)'] *df2['Uvalue_roof']
    df2 = Add_par(df2, {'heat_loss_radiation W':heat_loss_radiation})

    #Dynamic values

    df1 = HLC(df1, df2, heat_loss_radiation)
    df1 = calc_heat_w_e(df1, df2)
    df1 = electricity_consumption(df1, df2)
    #df1 = electricity_demand(df1, df2)
    df1 = tot_energy_heating(df1, df2)




    #Dessa två ger en massa intressant statistik osv
    #print(df1.describe())
    #print(df2.describe())

    return df1, df2


def HLC(df1,df2, heat_loss_radiation):
    print("Entered function: HLC")
    #Calculate delta T
    #take delta T times U value
    temp_in = df2['Tinside(ºC)'][0]

    df1['DeltaT (°C)'] = df1['Temp']-temp_in
    df1['H_loss (kW)'] = df1['DeltaT (°C)']*heat_loss_radiation[0]/1000
    return df1

def Add_par(df2,static_values):
    #Function adds the static arguments from House function
    print("entered Add_par")
    for x in static_values:

        df2[x] = static_values[x]

    return df2

def calc_heat_w_e(df1,df2):
    print("entered heat water energy calculator")
    #funktion för att hitta temperaturen ur headern här?
    t_net=40-df2['Twaterin(ºC)'][0]

    #calculate energy to heat up hot water:
    df1['Water(kW)'] = df1['Hot Water @ 40 C'] * t_net*4.186
    return df1

def electricity_consumption(df1, df2):
    #df1 = fix_formatting(df1,df2)

    df1['Cooking (MJ)'] = (df1['Cooking (MJ)']/3.6)
    df1 = df1.rename(columns={'Cooking (MJ)': 'Cooking (kWh)'})
    df1['El.consumtion (kwh)'] = df1['Cooking (kWh)']+df1['Electrical Applainces (kWh)']

    return df1

def energy_supply(crit1, crit2):
    #Ändra så att denna läser maskinerna som kommer användas och kan plocka t.ex. den bästa härifrån

    print("Ändra så att denna läser maskinerna som kommer användas och kan plocka t.ex. den bästa härifrån")

    return 0,95

def tot_energy_heating(df1, df2):
    print("Entered tot_energy_heating function")
    OHPH = 100 #Wh, Occupation_heat_per_hour


    air_losses = calculate_air_heat_losses(df1,df2)

    df1['Heat_e (kWh)'] = ((df1['%AreaHeatingCooling']/100 * df2['Area (m2)'][0] - df1['Occupation'] * OHPH) /1000)-df1['H_loss (kW)'] - air_losses

    df1.loc[df1['Occupation'] == 0, 'Heat_e (kWh)'] = df2['null_heat'][0]

    return df1

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

def lighting_consumtion(df1,df2):


    #energy_supply(lighting,... )
    efficiency = 0.7
    selected_watt = 0
    sel_lumen = 60


    lumens = df1['Lighting (lux)']*(df2['Height Lights (m)'][0])**2
    A = lumens/df1['Total lapms'] #gives lumen demand per light bulb
    lum_max = A.max()
    #search for lightbulb with minimum Amax lumens
    #E_consumption =

    #b = A.max() is the highest required llumen for a lightbulb durring the day <-search for this one

    #read from excel lightbulbs that have the required lumen
    return df1

def solar_heat(self, files, method):
    print(files[0])
    print(files[2]['Solar Thermal'])
    print(type(files[2]))
    candidates=[]

    #print( files[2]['Solar PV']['Efficiency'].max())
    eff = float(files[2]['Solar Thermal']['Efficiency'].max())

    for index, row in files[2]['Solar Thermal'].iterrows():

        if row['Efficiency'] == eff:
            candidates.append((index,row['Name']))


    #panel_efficciency = energy_supply('solar_heat','efficiency')
    selection = Label(self, text = "Your Solar heat panel selection:" + str(candidates[0])).grid(row=11, column = 0)

    panel_efficiency = eff

    #panel_efficciency = energy_supply('solar_heat','efficiency')

    files[0]['sol_h_prod (kWh)'] = files[0]['Rad (W/m^2)'] * 0.5 * files[1]['RnF (m2)'][0] * panel_efficiency/1000


    return files

def solar_electricity(self,files, method):
    #print(files[0])
    #print(files[2]['Solar PV'])
    #print(type(files[2]))
    candidates=[]

    #print( files[2]['Solar PV']['Efficiency'].max())
    eff = float(files[2]['Solar PV']['Efficiency'].max())

    for index, row in files[2]['Solar PV'].iterrows():

        if row['Efficiency'] == eff:
            candidates.append((index,row['Name']))


    #panel_efficciency = energy_supply('solar_heat','efficiency')
    selection = Label(self, text = "Your Solar PV selection:" + str(candidates[0])).grid(row=10, column = 0)

    panel_efficiency = eff
    #changes to be made
    files[0]['sol_e_product (kWh)'] = files[0]['Rad (W/m^2)'] * 0.5 * files[1]['RnF (m2)'][0] * panel_efficiency/1000
    return files #Fixad 7.11


def H_storage(df1,df2):
        print("entered heat_storage")
        df1['Heat_storage'] = 0
        storage = {}

        storage['energy_shortage (kWh)'] = df1['Heat_e (kWh)']+df1['sol_h_prod (kWh)']

        #print(Storage['Demand (kWh)'][x])

        place_holder = []
        place_holder.append(0)
        #print("range",range(len(storage['Demand (kWh)'])))
        for x in range(len(storage['energy_shortage (kWh)'])):

            A = storage['energy_shortage (kWh)'][x]
            B = df1['Heat_storage'][x]
            C = B+A

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
                    D = place_holder[-1]+C
                    if D > 0:
            #            print("PH-2",place_holder)
                        place_holder.append(D)
                    elif D < 0 :
                        place_holder.append(0)
            #            print("more power still needed, this much is left: ", D)
                elif place_holder[-1] < 0:
                    place_holder.append(0)
            #        print("placeholder index is smaller than 0?")
                    pass
                elif place_holder[-1] == 0:
                    place_holder.append(0)
                    pass
            else:

                place_holder.append(0) == 0
            #print("place_holder", place_holder)
        place_holder.pop(0)
        df1['Heat_storage'] = place_holder

        df1['Heat_storage'].plot()

        return df1, df2

def test(gui, current_file1, current_file2):

    Lab1 = Label(gui, text = current_file1).grid(row = 6)
    Lab2 = Label(gui, text = current_file2).grid(row = 7)
    return

def import_databases(gui):
    print("entered import_databases")
    storage     =   pd.read_excel('/Users/albertrehnberg/Desktop/projekt/StorageTechnologies Database.xlsx', sheet_name =None)
    conversion  =   pd.read_excel('/Users/albertrehnberg/Desktop/projekt/Conversion Technologies Database.xlsx', sheet_name =None)
    end_use     =   pd.read_excel('/Users/albertrehnberg/Desktop/projekt/End-Use technologies DataBase.xlsx', sheet_name =None)

    return conversion, storage, end_use


def get_graph_options(FILE1, FILE2,DATABASE1,DATABASE2):
    print("entered get_graph_options")

    headers = FILE1.headers + FILE2.headers + DATABASE1.headers + DATABASE2.headers

    return headers




def analysis(files):
    print("entered new_funct")
    #print(files[3])

    Data = [files[0],files[1]]
    Databases = [files[2],files[3],files[4]]

    for items in Databases:
        print(items.keys())
    print(Data[1].columns)
    print("––––––––––––––––––––––––––––––––––––––")
    print("––––––––––––––––––––––––––––––––––––––")
    print("––––––––––––––––––––––––––––––––––––––")
    #print(files)

#    for items in files[4]:
#        print(items)
