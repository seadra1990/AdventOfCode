import re
import sys

class Fish:
    def __init__(self,timer = 8):
        self.timer = int(timer)
    def passADay(self,school):
        if self.timer == 0:
            school.newFishBorn()
            self.timer = 6
        else:
            self.timer = self.timer - 1

class SchoolFish:
    def __init__(self):
        self.FishesGroup = []
        for i in range (9):
            self.FishesGroup.append(int(0))
        self.DailyNewFishes = 0
    def addFish(self,timer):
        self.FishesGroup[timer] = self.FishesGroup[timer]+1
    def reduceAllTimerAndCreateNewFish(self):
        temp = self.FishesGroup[0]
        for i in range (len(self.FishesGroup)-1):
            self.FishesGroup[i] = self.FishesGroup[i+1]
        self.FishesGroup[6] = temp + self.FishesGroup[6]
        self.FishesGroup[len(self.FishesGroup)-1] = temp
    def passADay(self):
        self.reduceAllTimerAndCreateNewFish()    
    def passMultiDays(self,numOfDay = 1):
        for i in range (numOfDay):
            print("Day #", i)
            self.passADay()
    def NumofFishes(self):
        sum = 0
        for groupcounter in (self.FishesGroup):
            sum = sum + groupcounter
        return sum
    
if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    timer_seq = re.compile (r"(\d),",re.MULTILINE)
    matchs = timer_seq.finditer (input_file.read())
    
    schoolfish = SchoolFish()
    for timer in matchs:
        schoolfish.addFish((int(timer[1])))
    
    schoolfish.passMultiDays(256)
    print(schoolfish.NumofFishes())
    # for fish in schoolfish.Fishes:
    #     print(fish.timer," ",end="")
    input()