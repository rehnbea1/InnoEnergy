#This file is for managing and analysing the data recieved from myfunctions
import myfunctions
import pandas

def main_action(df1,df2):

    storage = {}

    storage['energy_shortage (kWh)'] = df1['Heat_e (kWh)']+df1['sol_h_prod (kWh)']

    print(storage)
    #print(Storage['Demand (kWh)'][x])

    place_holder = []
    place_holder.append(0)
    #print("range",range(len(storage['Demand (kWh)'])))
    for x in range(len(storage['energy_shortage (kWh)'])):


        A = storage['energy_shortage (kWh)'][x]
        #print("A", A)
        B = df1['storage'][x]
        #print("B", B)
        C = B+A
        #print("C", C)
        #print(place_holder)
        #print("this is C", C)
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
        #        print("placeholder is 0")
                pass
        else:
        #    print("storage and production in balance")
            place_holder.append(0) == 0
        print("place_holder", place_holder)
    place_holder.pop(0)
    df1['storage'] = place_holder

    print(df1)

















    #    if x == 0:

    #        df1['storage'][x]
    #        print("df1iloc", df1['storage'][x])


    #    else:
    #        pass
    #        storage_old = df1['storage'][x-1]
    #        print("storage_old", storage_old)
    #        df1['storage'][x] = A + storage_old



    #    if x < 0:
    #        discharge = myfunctions.storage(df1,df2,x)
#
    #        if x < 0 :
    #            print("storage was not sufficient, more energy is still needed")
    #        else:
        #        print("storage fixed the deal")
#
#
        #if x > 0:
        #    print("there is excess heat produced, sending to storage:")
        #    charge = myfunctions.storage(df1,df2,x)

    return
