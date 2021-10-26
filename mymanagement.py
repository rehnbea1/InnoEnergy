#This file is for managing and analysing the data recieved from myfunctions


def main_action(dynamic,static):

    #kolla enheterna här, något skumt med Heate
    print("dynamic[heat_e]", dynamic['Hour'], dynamic['Heat_e'])
    delta = dynamic['H_loss (kW)']*3600 + dynamic['Heat_e']

    for x in delta:
        if x > 0:
            print("heating demand is: ", x)

        elif x < 0 :
            print("cooling demand is:", x)

        else:
            print("probably heating and cooling is in balance")
