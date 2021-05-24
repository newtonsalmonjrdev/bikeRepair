
class bikeClass:
    # "todo: figure out how to set inheritance for opening the repairwheeltxt file"

    def __init__(self, wheels, problem, valve):
        self.wheels = wheels
        self.problem = problem
        self.valve = valve
        with open("repairWheelScr.txt", "r") as file:
            self.flatTireList = file.readlines()

    def tireText(self):
        print(self.flatTireList[0])

    def repairWheel(self):
        if self.wheels == 2:
            if self.problem == "flat tire":
                if self.valve == "scr":
                    with open("repairWheelScr.txt", "r") as file:
                        flatTireList = file.readlines()
                        print(flatTireList[0])

                elif self.valve == "pres":
                    print(self.flatTireList[1])


            if self.problem == "adjusting brakes": # "TODO: pg 205 adjusting brakes"
                pass
            if self.problem == "replacing shift cables": # "TODO: pg 95 cables"
                pass
            if self.problem == "wheel building": # "TODO: pg 379 wheel building"
                pass


    #             print("How To remove front wheel:")
    #         elif problem == "remove back wheel":
    #             print("How to remove rear wheel")
    #     elif wheels == 3:
    #         print("How to remove wheel on tricycle")
    #     else:
    #         print("Please input correct number of wheels")
    #
    # def shiftingCable:
    #     if problem = "change shifting cable":
    #         print("How to change shifting cable:")
    # def brakingCable:
    #     if problem == "change braking cable":
    #         print("How to change breaking cable:")
    # # def slippedChain:

bike = bikeClass(2, "flat tire", "pres")

bike.repairWheel()
