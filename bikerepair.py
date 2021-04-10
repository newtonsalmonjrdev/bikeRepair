
class bikeClass:
    "todo: figure out how to set inheritance for opening the repairwheeltxt file"
    def tireText(self):
        with open("repairWheelScr.txt", "r") as file:
            flatTireList = file.readlines()

    def repairWheel(self, wheels, problem, valve):
        if wheels == 2:
            if problem == "flat tire" and valve == "scr":
                with open("repairWheelScr.txt", "r") as file:
                    flatTireList = file.readlines()
                    print(flatTireList[0])

            elif problem == "flat tire" and valve == "pres":
                print("How to fix a flat tire: ")
            elif problem == "remove front wheel":
                print("How to remove front wheel:")
            elif problem == "remove back wheel":
                print("How to remove rear wheel")
        elif wheels == 3:
            print("How to remove wheel on tricycle")
        else:
            print("Please input correct number of wheels")

    def shiftingCable:
        if problem = "change shifting cable":
            print("How to change shifting cable")
    def brakingCable:
        if problem == "change braking cable":
            print("How to change breaking cable:")
    # def slippedChain:

bike = bikeClass

print(bike.repairWheel("",2, "flat tire", "scr"))
