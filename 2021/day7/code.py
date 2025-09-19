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
    def addCrab(self,crab:Crab):
        self.Crabs.append(crab)
    def genCrabPosListWithOrder(self):
        self.crabposlist = []
        self.PositionOrderAvailable = False
        for crab in self.Crabs:
            self.crabposlist.append(crab.getPos())
        for i in range(len(self.crabposlist)):
            for j in range (i+1,len(self.crabposlist)):
                if self.crabposlist[i] > self.crabposlist[j]:
                    temp = self.crabposlist[i]
                    self.crabposlist[i] = self.crabposlist[j]
                    self.crabposlist[j] = temp
        self.PositionOrderAvailable = True
    def getMedianValue(self):
        if self.PositionOrderAvailable == True:   
            if len(self.crabposlist)%2 ==1:
                Median_position = int((len(self.crabposlist)+1)/2)
            else:
                Median_position = int((len(self.crabposlist))/2)
            return self.crabposlist[Median_position]
        else:
            raise Exception ("please make Order available")
    def calTotalFueltoMedianValue(self):
        MedianValue = self.getMedianValue()
        totalfuel = 0
        for crabpos in self.crabposlist:
            totalfuel = totalfuel +abs(MedianValue - crabpos)
        return totalfuel
    def calAveragePos(self):
        if self.PositionOrderAvailable == True:   
            sum = 0
            for crab in self.crabposlist:
                sum = sum + crab
            return int(sum/len(self.crabposlist))
        else:
            raise Exception ("please make Order available")
    def calTotalFueltoAveragePoint(self):
        averagePos = self.calAveragePos()
        totalfuel = 0
        for crab in self.crabposlist:
            dist = abs(averagePos-crab)
            totalfuel = totalfuel + (dist*(dist+1))/2
        #calculate Total Fuel
        return int(totalfuel)

if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    pos_seq = re.compile (r"(\d+),",re.MULTILINE)
    matchs = pos_seq.finditer (input_file.read())
    
    swarm = SwarmCrab()
    for position in matchs:
        swarm.addCrab((Crab(position[1])))
    swarm.genCrabPosListWithOrder()
        
    exampleexpectation1 = 2,37
    exampleexpectation2 = 5,168

    realexpectation1 = 355150
    realexpectation2 = 98368490

    # Median Value is the Optimization Point for Part1
    # figure out, hmm, not by the definition of Median Value 
    # but by calculate derivative of function
    # Knowledge is valuable and sometimes you need
    # Math in real life :)
    output1 = swarm.calTotalFueltoMedianValue()
    
    if (file_name == "input_test.txt"):
        if exampleexpectation1 == output1:
            print("Example Part 1 is correct")
            print("Output:",output1)
        else:
            print("Example Part 1 is NOT correct")
            print("expectation:",exampleexpectation1)
            print("Output:",output1)
    else:
        if realexpectation1 ==output1:
            print("Part 1 is correct")
            print("Output:",output1)
        else:
            print("Part 1 is NOT correct")
            print("expectation:",realexpectation1)
            print("Output:",output1)

    # Average Value is the Optimization Point for Part1
    # figure out by calculate derivative of function
    output2 = swarm.calTotalFueltoAveragePoint()
    if (file_name == "input_test.txt"):
        if exampleexpectation2 == output2:
            print("Part 2 is correct")
            print("Output:",output2)
        else:
            print("Part 2 is NOT correct")
            print("expectation:",exampleexpectation2)
            print("Output:",output2)
    else:
        if realexpectation2 ==output2:
            print("Part 2 is correct")
            print("Output:",output2)
        else:
            print("Part 2 is NOT correct")
            print("expectation:",realexpectation2)
            print("Output:",output2)
    input()