#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida
import csv
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt



def Select_file(gui):

    filetypes = (('csv-files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='documents/',filetypes=filetypes)
    return filename


def Read_file(filename,gui):

    #try:
    with open(filename,'r') as file:
        Data ={}
        i=0
        file_reader = csv.reader(file)
        #header = next(file_reader)
        for line in file_reader:
            Data.update({i:line})
            i=i+1

        print("YOUR DICTIONARY LOOKS LIKE THIS:", Data)
        #x = Label(gui,text="Read following data:")
        #y = Label(gui, text=List)
        file.close()
        return Data


def Read_file2(filename,gui):

    #try:
    df = pd.read_csv(filename)
    #for index in df.iterrows():
#    Length (m)  Depth (m)  Height (m)  UWalls (W/(m^2K)  UWindows (W/(m^2K)  Awindow/Awall ratio  Air Changes per Hour (h^-1)  Tinside (ÂºC)  Qpeople (W)  Window Solar Gain  Height Lights (m)
#0          10          5           3                 1                   2                  0.2                          0.5              2          120               0.25                1.5


    print(df)
    #print("length",df['Length'])
    #print('height',df['Height'])
    Area = (df['Length (m)']*df['Depth (m)'])*2 + (df['Length (m)']*df['Height (m)'])*4
    Volume = df['Length (m)']*df['Depth (m)']*df['Height (m)']
    WindowA = Area - ((df['Length (m)']*df['Height (m)'])*4) * df['Awindow/Awall ratio']

    Heat_loss = Area * df['UWalls (W/(m^2K)'] + WindowA * df['UWindows (W/(m^2K)']
    print(Area)




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

def analysis(gui, data):
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

def house(gui, data):
    pass
