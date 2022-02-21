import datetime
import time
import threading
import random


class my_task():
    name = None
    priority = -1
    period = -1
    execution_time = -1
    last_execution_time = None
    nbrewhell=0

    ############################################################################
    def __init__(self, name, priority, period, execution_time, last_execution):
        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time


    def sauvegarde(self):
        global reservoir
        global stock1
        global stock2



        

    ############################################################################
    def run(self):
        global temps_ecoule
        global reservoir
        global stock1
        global stock2
        global nbrewhell
        global nbremotors

        # Update last_execution_time
        self.last_execution_time = datetime.datetime.now()

        print(self.name + " : Starting task (" + self.last_execution_time.strftime(
            "%H:%M:%S") + ") : execution time = " + str(self.execution_time))


        while (1):
            
            if self.name == "Pump 1" and self.period % 5 != 0:
                return
            if self.name == "Pump 2" and self.period % 5 != 0:
                return

            if (self.name == "Pump 1" or self.name == "Pump 2") and reservoir == 50:
                print("Pump bloqué car reservoir est plein")
                return
            elif (self.name == "Pump 1" and reservoir + 10 > 50) or (self.name == "Pump 2" and reservoir + 20 > 50) :
                print("Pump bloqué car l'ajout d'huile impliquera un excés de stockage")
                return
            elif self.name == "Pump 1":
                reservoir = reservoir + 10
            elif self.name == "Pump 2":
                reservoir = reservoir + 20

            self.execution_time -= 1
            
            temps_ecoule += 1
            
            time.sleep(1)

            if self.execution_time <= 0:
                if self.name == "Pump 1":
                    print("Pump 1 : Produce 10 oil")
                    # nbrewhell=nbrewhell+1
                elif self.name == "Pump 2":
                    print("Pump 2 : Produce 20 Oil")
                    # nbremotors=nbremotors+1
                elif self.name == "Machine 1":
                    print("Machine 1 : Produce 1 motor")
                elif self.name == "Machine 2":
                    print("Machine 2 : Produce 1 wheel")

                print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
                return


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':
    # Init and instanciation of watchdog

    # global watchdog
    # watchdog = False
    temps_ecoule = 0
    reservoir = 0
    stock1 = 0
    stock2 = 0


    last_execution = datetime.datetime.now()

    # Instanciation of task objects
    task_list = [
        my_task(name="Pump 1", priority=1, period=5, execution_time=2, last_execution=last_execution),
        my_task(name="Pump 2", priority=1, period=15, execution_time=3, last_execution=last_execution),
        my_task(name="Machine 1", priority=1, period=5, execution_time=5, last_execution=last_execution),
        my_task(name="Machine 2 ", priority=1, period=5, execution_time=3, last_execution=last_execution)
    ]

    # Global scheduling loop
    incrementation = 0
    while (1):
        print("\nScheduler tick " + str(incrementation) + " : " + datetime.datetime.now().strftime("%H:%M:%S"))
        incrementation += 1



        for task_to_run in task_list:
            print("The current time is: "+str(temps_ecoule));
            print()


            task_to_run.run()
