import re
import sys

class Pattern:
    def __init__(self):
        self.data = ""
    def setdata(self,input:str):
        self.data = list(input)
    def sortdata(self):
        templist = list(self.data)
        for i in range (len(templist)):
            for j in range(i+1,len(templist)):
                if templist[i] > templist[j]:
                    temp = templist[i]
                    templist[i] = templist[j]
                    templist[j] = temp
        self.data = "".join(templist)
    def __len__(self):
        return (len(self.data))
    def print(self):
        print(self.data)
    def setpattern(self,other):
        self.data = other.data
    def __eq__(self, other):
        return self.data == other.data
    def iscontainedin(self,other):
        templist = list(self.data)
        templistcmp = list(other.data)
        count = 0
        for char in templist:
            for key in templistcmp:
                if char == key:
                    count = count +1
                    break
        if count == len(templist):
            return True
        else:
            return False
    def __add__(self,other):
        tempstr = "".join(list(set(list(self.data) + list(other.data))))
        tempPattern = Pattern()
        tempPattern.setdata(tempstr)
        tempPattern.sortdata()
        return tempPattern
    def countnotmatchin(self,other):
        templist = list(self.data)
        templistcmp = list(other.data)
        count = 0
        for char in templist:
            found = False
            for key in templistcmp:
                if char == key:
                    found = True
                    break
            if found == False:
                # print(char)
                count = count+1
        return count

class Entry:
    def __init__(self):
        self.patterns = [Pattern() for _ in range (10)]
        self.decoded_patterns = [Pattern() for _ in range (10)]
        self.outputpatterns = [ Pattern() for _ in range (4)]
        self.decoded_outputdigits = [ 10 for _ in range (4)]
        self.segmentdecodekey = dict(a='a',b='b',c='c',d='d',e='e',f='f',g='g')
        self.patterndecoded = [False for _ in range (10)]
    def setpatterns(self,inputlist):
        for index,pattern in enumerate(self.patterns):
            pattern.setdata(str(inputlist[index]))
            pattern.sortdata()
    def setoutputs(self,inputlist):
        for index,pattern in enumerate(self.outputpatterns):
            pattern.setdata(str(inputlist[index]))
            pattern.sortdata()
    def decodepatternsStep1(self):
        found = 0        
        for index,pattern in enumerate(self.patterns):
            if len(pattern) != len(pattern.data):
                raise Exception("Len function not work")
            if len(pattern.data) == 2 and found != 4:
                found = found+1
                self.decoded_patterns[1].setpattern(pattern)
                self.patterndecoded[index] = True
            elif len(pattern.data) == 3 and found != 4:
                found = found+1
                self.decoded_patterns[7].setpattern(pattern)
                self.patterndecoded[index] = True
            elif len(pattern.data) == 4 and found != 4:
                found = found+1
                self.decoded_patterns[4].setpattern(pattern)
                self.patterndecoded[index] = True
            elif len(pattern.data) == 7 and found != 4:
                found = found+1
                self.decoded_patterns[8].setpattern(pattern)
                self.patterndecoded[index] = True
            elif found == 4:
                break
        if (found !=4):
            print("we found only ",found,"pattern number")
            raise Exception ("Decode part 1 error")
    def countOutputStep1(self):
        counter = 0
        if len(self.decoded_patterns) == 0:
            raise Exception ("Decode something wrong")
        for pattern in self.outputpatterns:
            if pattern.data != "" and pattern in self.decoded_patterns:
                counter = counter+1
                # print(pattern.data)
        return counter
    def decodepatternsStep2(self):
        keytofind = Pattern()
        keytofind.setpattern(self.decoded_patterns[1]+self.decoded_patterns[4]+self.decoded_patterns[7])
        #find #9,0,3        
        for index,pattern in enumerate(self.patterns):
            if self.patterndecoded[index] == False:
                #find #9,0,3
                if (self.patterndecoded[index] == False) and (len(pattern.data) == 6) and (self.decoded_patterns[4].iscontainedin(pattern)) and (self.decoded_patterns[7].iscontainedin(pattern)):
                    #find a #9
                    self.decoded_patterns[9] = pattern
                    self.patterndecoded[index] = True
                elif (self.patterndecoded[index] == False) and (len(pattern.data) == 6) and (not self.decoded_patterns[4].iscontainedin(pattern))and (self.decoded_patterns[7].iscontainedin(pattern)):
                    #found a #0
                    self.decoded_patterns[0] = pattern
                    self.patterndecoded[index] = True
                elif (self.patterndecoded[index] == False) and (len(pattern.data) == 5) and (self.decoded_patterns[7].iscontainedin(pattern)):
                    #found a #3
                    self.decoded_patterns[3] = pattern
                    self.patterndecoded[index] = True
                #find #2,6
                elif(self.patterndecoded[index] == False) and (len(pattern.data) == 5) and (pattern.countnotmatchin(keytofind) == 2):
                    #found 2
                    self.decoded_patterns[2] = pattern
                    self.patterndecoded[index] = True
                elif(self.patterndecoded[index] == False) and (len(pattern.data) == 5) and (pattern.countnotmatchin(keytofind) == 1):
                    #found 5
                    self.decoded_patterns[5] = pattern
                    self.patterndecoded[index] = True
                elif(self.patterndecoded[index] == False) and (len(pattern.data) == 6) and (pattern.countnotmatchin(keytofind) == 2):
                    #found 6
                    self.decoded_patterns[6] = pattern
                    self.patterndecoded[index] = True
                elif (self.patterndecoded[index] == False):
                    for index,data in enumerate(self.decoded_patterns):
                        print(index,"|",data.data,"\t",end="")          
                    raise Exception ("Cannot decode the pattern",pattern.data)
        valueoutput = 0
        power = 1000
        for pattern in self.outputpatterns:            
            for index, key in enumerate(self.decoded_patterns):
                if pattern.data == key.data:
                    print(index*power)
                    valueoutput = valueoutput + index*power
                    power = power/10
                    break
        return int(valueoutput)

class Puzzle:
    def __init__(self):
        self.entry = Entry()
    def setEntry(self,entry:Entry):
        self.entry = entry
    def calcPart1(self):
        return 0
    def calcPart2(self):
        return 0

def regexcreator():
    seq = ""
    for i in range (10):
        seq = seq+"(\w+)\s"
    seq = seq+"|"
    for i in range (4):
        seq = seq+"(\w+)\s"
    return seq

if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    entry_seq = re.compile(r"(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s\|\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s",re.MULTILINE)
    puzzle = Puzzle()
    outputpart1 = 0
    outputpart2 = 0
    linecounter = 0
    for line in input_file:     
        linecounter = linecounter+1   
        entrydata = (entry_seq.findall(line))
        temp_entry = Entry()
        patterns = list(entrydata[0][0:10])
        outputs = list(entrydata[0][10:15])
        temp_entry.setpatterns(patterns)
        temp_entry.setoutputs(outputs)
        puzzle.setEntry(temp_entry)
        puzzle.entry.decodepatternsStep1()
        entryout = puzzle.entry.countOutputStep1()
        outputpart1 = outputpart1 + entryout
        entryout2 = puzzle.entry.decodepatternsStep2()
        outputpart2 = outputpart2 + entryout2
    
    exampleexpectation1 = 26    
    output1 = outputpart1

    print("Output1:",output1)
    
    exampleexpectation2 = 61229
    output2 = outputpart2
    print("Output2:",output2)

    if (file_name == "input_test.txt"):
        if exampleexpectation1 == output1:
            print("Example Part 1 is correct")
        else:
            print("Example Part 1 is NOT correct")
            print("expectation:",exampleexpectation1)


    if (file_name == "input_test.txt"):
        if exampleexpectation2 == output2:
            print("Example Part 2 is correct")
        else:
            print("Example Part 2 is NOT correct")
            print("expectation:",exampleexpectation2)
    input()