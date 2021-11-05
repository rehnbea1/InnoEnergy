#This file is for managing and analysing the data recieved from myfunctions
import myfunctions
import pandas as pd



def main_action(gui,df1,df2,FILE1,FILE2):

    print("Entered mymanagement_main_action")


    return



def read_application_database(gui, file):

    #This is only for testning, remove root in final version
    file = "/Users/albertrehnberg/Desktop/"+file
    file = myfunctions.read_file2(gui,file)
    return file


    #conversion_database_wind = read_application_database(gui, "projekt/Conversion Technologies Database - Solar PV.csv")
    #conversion_database_solar_h = read_application_database(gui, "projekt/Conversion Technologies Database - Solar Thermal.csv")
    #conversion_database_solar_e = read_application_database(gui, "projekt/Conversion Technologies Database - Wind Turbine.csv")

    #end_use_tech_database_SH = read_application_database(gui,"projekt/End-Use technologies DataBase - SpaceHeating.csv")
    #end_use_tech_database_SHW = read_application_database(gui,"projekt/End-Use technologies DataBase - SpaceHeatingWater.csv")
    #end_use_tech_database_SHC = read_application_database(gui,"projekt/End-Use technologies DataBase - SpaceHeatingCooling.csv")
    #end_use_tech_database_HW = read_application_database(gui,"projekt/End-Use technologies DataBase - HotWater.csv")
    #end_use_tech_database_C = read_application_database(gui,"projekt/End-Use technologies DataBase - Cooking.csv")
    #end_use_tech_database_L =  read_application_database(gui,"projekt/End-Use technologies DataBase - Lighting.csv")

    #storage_tech_database_Batteries = read_application_database(gui,"projekt/StorageTechnologies Database - Batteries.csv")
    #storage_tech_database_Tank = read_application_database(gui,"projekt/StorageTechnologies Database - Tank.csv")
    #storage_tech_database_Hydrogen = read_application_database(gui,"projekt/StorageTechnologies Database - Hydrogen.csv")

    return
    #lägg in funktionerna hit, de som behandlar denna data2
