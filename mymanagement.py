#This file is for managing and analysing the data recieved from myfunctions


def main_action(dyn,stat):


    #kolla enheterna här, något skumt med Heate
    def heating (dyn, stat):
        print("dyn[heat_e]", dyn['Hour'], dyn['Heat_e'])
        delta = dyn['H_loss (kW)']*3600 + dyn['Heat_e']

        for x in delta:
            if x > 0:
                print("heating demand is: ", x)

            elif x < 0 :
                print("cooling demand is:", x)

            else:
                print("probably heating and cooling is in balance")
    return
