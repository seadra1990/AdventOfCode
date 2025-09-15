import re
import sys

class Point:
    def __init__(self,x,y):
        self.PosX = int(x)
        self.PosY = int(y)

class MapPoint: 
    def __init__(self):
        self.NumOfOverlap = 0   
    def MarkOverlaped(self):
        self.NumOfOverlap = self.NumOfOverlap+1     

class Line:
    def __init__(self,startpoint:Point,endpoint:Point):
        self.Start = startpoint
        self.End = endpoint
    def __init__(self,startX,startY,endX,endY):
        self.Start = Point(startX,startY)
        self.End = Point(endX,endY)
    def isHorizontalLine(self):
        if self.Start.PosX == self.End.PosX:
            return True
        else:
            return False
    def isVerticalLine(self):
        if self.Start.PosY == self.End.PosY:
            return True
        else:
            return False
    def isDiagonalLine(self):
        delta_x = abs(self.Start.PosX - self.End.PosX)
        delta_y = abs(self.Start.PosY - self.End.PosY)
        if delta_x == delta_y:
            return True
        else:
            return False
    def isDrawable(self):
        return self.isVerticalLine() or self.isHorizontalLine() or self.isDiagonalLine()

class Map:
    def __init__(self,size:int):
        self.PointList = [[MapPoint() for _ in range (size)] for _ in range (size)]

    def getPointBaseOnPos(self,X,Y):
        return self.PointList[X][Y]

    def drawHorizontal(self,line:Line):
        if line.isHorizontalLine():
            PosX = line.Start.PosX
            PosY = line.Start.PosY
            done = False
            while(done == False):
                self.getPointBaseOnPos(PosX,PosY).MarkOverlaped()
                # print("Overlap: ",PosX,PosY,self.getPointBaseOnPos(PosX,PosY).NumOfOverlap)
                if PosY!=line.End.PosY:                    
                    direction = (line.End.PosY-line.Start.PosY)/abs(line.End.PosY-line.Start.PosY)
                    PosY = PosY + int(direction)
                else:
                    done = True
    def drawVertical(self,line:Line):
        if line.isVerticalLine():
            PosX = line.Start.PosX
            PosY = line.Start.PosY
            done = False
            while(done == False):
                self.getPointBaseOnPos(PosX,PosY).MarkOverlaped()
                # print("Overlap: ",PosX,PosY,self.getPointBaseOnPos(PosX,PosY).NumOfOverlap)
                if PosX!=line.End.PosX:                    
                    direction = (line.End.PosX-line.Start.PosX)/abs(line.End.PosX-line.Start.PosX)
                    PosX = PosX + int(direction)
                else:
                    done = True
    def drawDiagonal(self,line:Line):
        if line.isDiagonalLine():
            PosX = line.Start.PosX
            PosY = line.Start.PosY
            done = False
            while(done == False):
                self.getPointBaseOnPos(PosX,PosY).MarkOverlaped()
                # print("Overlap: ",PosX,PosY,self.getPointBaseOnPos(PosX,PosY).NumOfOverlap)
                if PosX!=line.End.PosX:                    
                    directionX = (line.End.PosX-line.Start.PosX)/abs(line.End.PosX-line.Start.PosX)
                    PosX = PosX + int(directionX)
                    directionY = (line.End.PosY-line.Start.PosY)/abs(line.End.PosY-line.Start.PosY)
                    PosY = PosY + int(directionY)
                else:
                    done = True

    def drawLine(self,line:Line):
        if line.isDrawable():
            print("Line Drawable: ",line.Start.PosX, line.Start.PosY, line.End.PosX, line.End.PosY)
            self.drawHorizontal(line)
            self.drawVertical(line)
            self.drawDiagonal(line)

    def countNumberofManyOverlapedPoint(self):
        counter = 0
        for line in self.PointList:
            for mappoint in line:
                if mappoint.NumOfOverlap >= 2:
                    counter = counter +1
                    # print("found point #",counter,":", x,y)
        return counter


    


if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    line_seq = re.compile (r"(\d+),(\d+)\s->\s(\d+),(\d+)",re.MULTILINE)
    linelist = []
    size = 0
    for row in input_file:
        match = line_seq.findall(row)
        for value in match[0]:
            size = max(size,int(value))
        linelist.append(Line(match[0][0],match[0][1],match[0][2],match[0][3]))
        
    mapdata = Map(size+1)
    for line in linelist:
        mapdata.drawLine(line)
       
    print(len(mapdata.PointList))

    print(mapdata.countNumberofManyOverlapedPoint())

    input()