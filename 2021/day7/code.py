import re
import sys

class Crab:
    def __init__(self,PosX:int):
        self.HozPos = PosX       
    def getPos(self):
        return int(self.HozPos)

class SwarmCrab:
    def __init__(self):
        self.Crabs = []     
        self.CrabsWithOrder = []   
        self.listPosition = []
        self.sumPosition = 0
    def addCrab(self,crab:Crab):
        self.Crabs.append(crab)
    def checkvalidity(self):
        if (len(self.Crabs) == 0):
            raise Exception ("Swarm is empty")
    def calSumPos(self):        
        self.checkvalidity()
        if self.CrabsWithOrder == []:       
            for crab in self.Crabs:
                self.sumPosition = self.sumPosition + crab.getPos()
            return self.sumPosition
        else:
            totalcrabs = 0
            for cluster in self.CrabsWithOrder:
                totalcrabs = totalcrabs + cluster[1]
                self.sumPosition = self.sumPosition + cluster[0]*cluster[1]
            return self.sumPosition
    def calculateListOfPosition(self):
        self.checkvalidity()
        templistPosition = []
        for crab in self.Crabs:
            templistPosition.append(crab.getPos())
        self.listPosition = list(set(templistPosition))
        #sort the order min->max, hopefully, it's help :)
        for i in range (len(self.listPosition)):
            for j in range (i+1,len(self.listPosition)):
                if (self.listPosition[i] > self.listPosition[j]):
                    temp = self.listPosition[i]
                    self.listPosition[i] = self.listPosition[j]
                    self.listPosition[j] = temp
        self.TargetPositionList = list(range(min(self.listPosition),max(self.listPosition)))
    def updateCrabsOrder(self):
        numberofPosition = len(self.listPosition)
        if numberofPosition == 0:
            self.calculateListOfPosition()
        if self.CrabsWithOrder == []:             
            for crabposition in self.listPosition:
                self.CrabsWithOrder.append([crabposition,0])
            for cluster in self.CrabsWithOrder:
                for crab in self.Crabs:
                    if crab.getPos() == cluster[0]:
                        cluster[1] = cluster[1] + 1
    def calTotalFueltoOptimizationPoint(self):
        self.checkvalidity()
        self.updateCrabsOrder()
        OptPos = 0
        OptFuel = []
        for position in self.TargetPositionList:
            temp1 = 0
            for cluster in self.CrabsWithOrder:
                temp1 = temp1 + abs(cluster[0]-position)*cluster[1]
            OptFuel.append(temp1)
            if temp1 == min(OptFuel):
                OptPos = position
        return OptPos,min(OptFuel)
    def calTotalFueltoOptimizationPointPart2(self):
        self.checkvalidity()
        self.updateCrabsOrder()
        OptPos = 0
        OptFuel = []
        for position in self.TargetPositionList:
            totalfuelestimation = 0 
            for cluster in self.CrabsWithOrder:
                onecrabfuel = 0
                clusterfuel = 0
                for step in range(abs(cluster[0]-position)):
                    onecrabfuel = onecrabfuel + step+1
                clusterfuel = onecrabfuel*cluster[1]
                totalfuelestimation = totalfuelestimation + clusterfuel
            # print("total fuel for target position",position, "is :",totalfuelestimation)
            OptFuel.append(totalfuelestimation)
            if totalfuelestimation == min(OptFuel):
                OptPos = position
        return OptPos,min(OptFuel)


    
if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    pos_seq = re.compile (r"(\d+),",re.MULTILINE)
    matchs = pos_seq.finditer (input_file.read())
    
    swarm = SwarmCrab()
    for position in matchs:
        swarm.addCrab((Crab(position[1])))
    
    expectation1 = 2,37
    expectation2 = 5,168
    output1 = swarm.calTotalFueltoOptimizationPoint()

    if (file_name == "input_test.txt"):
        if expectation1 == output1:
            print("Example Part 1 is correct")
            print("Output:",output1)
        else:
            print("Example Part 1 is NOT correct")
            print("expectation:",expectation1)
            print("Output:",output1)

    output2 = swarm.calTotalFueltoOptimizationPointPart2()
    if (file_name == "input_test.txt"):
        if expectation2 == output2:
            print("Example Part 2 is correct")
            print("Output:",output2)
        else:
            print("Example Part 2 is NOT correct")
            print("expectation:",expectation2)
            print("Output:",output2)
    input()