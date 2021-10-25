#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida
import csv
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
import pandas as pd
#import math
import numpy as np
import matplotlib.pyplot as plt


def Delta2(gui, DATA1):
    file_2 = Select_file(gui)
    file_2 = Check_file(file_2,gui)
    file_info = Label(gui,text="Your selection for File_2: "+ file_2)
    file_info.grid(row = 2, column = 1, pady = 5)

    DATA2 = Read_file2(file_2,gui)

    #disp_data2 = Button(gui, text='Display data', command = lambda:myfunctions.show_data(gui,DATA)).grid(row=3, column = 1)

    House_data = Button(gui, text="calculate house data", command = lambda:House(gui,DATA1,DATA2)).grid(row=3, column = 0)


def Select_file(gui):
    filetypes = (('csv-files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='downloads/',filetypes=filetypes)
    return filename

def Read_file2(filename,gui):

    file = pd.read_csv(filename)
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

#Data1     Hour  Temp (ºC)  Wind speed  Rad\n (W/m2)  Occupation  Lighting (Lux) %Total Area Lighting %AreaHeatingCooling  Hot Water L at 40º  Cooking (MJ) Electrical Applainces (kWh)
#0      0      10.24        6.57          0.00           3               0                    0                 25%                   0             0


    #DATA 2 Length (m)  Depth (m)  Height (m)  UWalls (W/(m^2K)  UWindows (W/(m^2K)  Awindow/Awall ratio  Air Changes per Hour (h^-1)  Tinside (ÂºC)  Qpeople (W)  Window Solar Gain  Height Lights (m)
#0          10          5           3                 1                   2                  0.2                          0.5              2          120               0.25                1.5

    print("Data1",df1)
    print("data2",df2)
    #print("length",df['Length'])
    #print('height',df['Height'])
    Static_values = {'Uvalue_roof' : 8/100,'Uvalue_floor': 14/100}
    df2 = Add_par(df2, Static_values)
    Area = (df2['Length (m)']*df2['Depth (m)'])*2 + (df2['Length (m)']*df2['Height (m)'])*4
    Volume = df2['Length (m)']*df2['Depth (m)']*df2['Height (m)']
    WindowA = Area - ((df2['Length (m)']*df2['Height (m)'])*4) * df2['Awindow/Awall ratio']
    heat_loss_radiation = Area * df2['UWalls (W/(m^2K)'] + WindowA * df2['UWindows (W/(m^2K)']

    df1 = HLC(df1, df2, heat_loss_radiation)

    print(df1.describe())
    print(df2.describe())

    return

def HLC(df1,df2,heat_loss_radiation):

    print("HLR",heat_loss_radiation)
    #Calculate delta T
    #take delta T times U value
    print("HLC")

    temp_in = df2['Tinside (ÂºC)'][0]
    print('test',temp_in)

    for row in df1.iterrows():
        df1['DeltaT (°C)'] = df1['Temp (ºC)']-temp_in
    for row in df1.iterrows():
        df1['H_loss (kW)'] = df1['DeltaT (°C)']*heat_loss_radiation[0]/1000

    print('uppdaterad df1:')
    print(df1)
    return df1

def Add_par(df2,static_values):
        for x in static_values:
            print("item", x)
            print("svi", static_values[x])

            df2[x] = static_values[x]

        print(df2)
        return df2
