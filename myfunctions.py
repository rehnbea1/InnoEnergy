#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida
import csv
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
import pandas as pd

import matplotlib.pyplot as plt


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

def Select_file(gui):
    filetypes = (('csv-files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='downloads/',filetypes=filetypes)
    return filename

def Read_file2(filename,gui):

    file = pd.read_csv(filename, sep=';')
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


    print("df1",df1)
    print("df2",df2)

    #funktion för att insert flera static values här?
    Static_values = {'Uvalue_roof' : 0.08,'Uvalue_floor': 0.14,'Water_in':20}

    Area    =   df2['Length(m)']*df2['Depth(m)']*2 + df2['Length(m)']*df2['Height(m)']*4
    Volume  =   df2['Length(m)']*df2['Depth(m)']*df2['Height(m)']
    WindowA =   Area - ((df2['Length(m)']*df2['Height(m)'])*4) * df2['Awindow/Awall']
    RnF     =   df2['Length(m)']*df2['Depth(m)']

    Static_values = {'Uvalue_roof' : 0.08,'Uvalue_floor': 0.14,'Water_in':20, 'Area (m2)':Area,'Volume (m3)':Volume,'WindowA (m2)':WindowA,'RnF (m2)':RnF}
    #Static_values = {'Uvalue_roof' : 0.08,'Uvalue_floor': 0.14,'Water_in':20,'Area':Area,'Volume':Volume, 'WindowA':WindowA, 'RnF':RnF, 'heat_loss_radiation': heat_loss_radiation}
    df2 = Add_par(df2, Static_values)

    heat_loss_radiation = df2['Area (m2)'] * df2['Uwalls(W/m2K)'] + df2['WindowA (m2)'] * df2['Uwindows(W/m2K)'] + df2['RnF (m2)']* df2['Uvalue_floor'] + df2['RnF (m2)'] *df2['Uvalue_roof']

    df2 = Add_par(df2, {'heat_loss_radiation W':heat_loss_radiation})

    print(df2)
    df1 = HLC(df1, df2, heat_loss_radiation)
    df1 = calc_heat_w_e(df1, df2)
    df1 = electricity_consumption(df1, df2)
    #df1 = electricity_demand(df1, df2)
    df1 = tot_energy_heating(df1, df2)


    print("stat_V",Static_values)
    ES = energy_supply()
    #Dessa två ger en massa intressant statistik osv
    #print(df1.describe())
    #print(df2.describe())
    print("Data1",df1)
    print("data2",df2)
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
    t_net=40-df2['Water_in'][0]

    #calculate energy to heat up hot water:
    df1['Water(kW)'] = df1['Hot Water @ 40 C'] * t_net*4.186
    return df1

def electricity_consumption(df1, df2):
    #df1 = fix_formatting(df1,df2)

    df1['Cooking (MJ)'] = (df1['Cooking (MJ)']/3.6)
    df1 = df1.rename(columns={'Cooking (MJ)': 'Cooking (kWh)'})
    df1['El.energy (kwh)'] = df1['Cooking (kWh)']+df1['Electrical Applainces (kWh)']

    return df1

#def fix_formatting(df1,df2):
#    A = []
#    for row in df1['Electrical Applainces (kWh)']:
#        row=row.replace(',','.')
#        row = float(row)
#        A.append(row)
#    df1 = df1.drop(columns= ['Electrical Applainces (kWh)'])
#    df1['Electrical Applainces (kWh)'] = A
#    return df1

def energy_supply():
    #Ändra så att denna läser maskinerna som kommer användas och kan plocka t.ex. den bästa härifrån

    Technologies={
    'Solar':
    {'name': 'Savosolar SALO® 305-315W MONO',
    'power (W)' : 310,
    'area m2': 1.622912,
    'efficiency':0.191,
    'price': 1000
    },
    'thermal solar':{
    'name': 'Bosch',
    'tank_size (L)': 120,
    'efficiency':0.95,
    'price':1566,
      },

     }

    return Technologies

def tot_energy_heating(df1, df2):
    print("Entered tot_energy_heating function")
    OHPH = 100 #Wh, Occupation_heat_per_hour
    df1['Heat_e (Wh)'] = ((df1['%AreaHeatingCooling']/100 * df2['Area (m2)'][0] - df1['Occupation'] * OHPH) /1000)-df1['H_loss (kW)']

    df1.loc[df1['Occupation'] == 0, 'Heat_e (Wh)'] = 'm'


    print(df1)
    return df1
