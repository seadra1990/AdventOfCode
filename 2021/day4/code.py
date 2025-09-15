import re
import sys

class BingoBoardCell:
    def __init__(self,value):
        self.number = value
        self.marked = False
    def setnumber(self,value):
        self.number = value
    def setmarked(self,val):
        self.marked = val
    def ismarked(self):
        return self.marked
    def print(self):
        print("\t",str(self.number),str(self.marked), sep="|",end="")

class BingoBoard:
    def __init__(self, number_arr):
        self.board = [[BingoBoardCell(100) for _ in range (5)] for _ in range (5)] #Init as Zero Matrix
        for i in range(5):
            for j in range (5):
                self.board[i][j].setnumber(number_arr[5*i+j])
        self.Bingo = False
    def check_number_mark(self, number):
        for i in range(5):
            for j in range (5):
                if (number == self.board[i][j].number):
                    self.board[i][j].setmarked(True)
                    return True
        return False
    def hasarowmark(self):
        for i in range(5):
            markcounter = 0
            for j in range (5):
                if self.board[i][j].ismarked():
                    markcounter = markcounter + 1
            if markcounter == 5:
                print("Bingo in row :",i)
                return True
        # print("markcounter in row",markcounter)
        return False       
    def hasacolumnmark(self):
        for j in range(5):
            markcounter = 0
            for i in range (5):
                if self.board[i][j].ismarked():
                    markcounter = markcounter + 1
            if markcounter == 5:
                print("Bingo in column :",i)
                return True
        # print("markcounter in column",markcounter)
        return False       
    def isBINGO(self):
        if (self.Bingo == False):
            if self.hasarowmark() or self.hasacolumnmark():
                self.Bingo = True
                return True
            else:
                return False   
        else:
            return self.Bingo
    def sumofunmarked(self):
        sum = 0
        for i in range(5):
            for j in range (5):
                if (self.board[i][j].ismarked() == False):
                    sum = sum + self.board[i][j].number
        return sum
    def print(self):
        for i in range(5):
            for j in range (5):
                self.board[i][j].print()
            print("")

def create_boards_from_data(lst_data):
    print(len(lst_data))
    temp_list = []
    num_of_board = int(len(lst_data)/25)
    for i in range(num_of_board):
        board_data = lst_data[25*i:25*i+25]
        print(board_data)
        print("length inputdata:",len(board_data))
        temp_list.append(BingoBoard(board_data))
    return temp_list

def convertregexlist2numberlist(matchlist): #TESTED
    templist = []
    for match in matchlist:
        templist.append(int(match))
    return templist

if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    bingo_number_seq = re.compile (r"(\d+),",re.MULTILINE)
    bingo_board_seq = re.compile (r"(\d+)\s",re.MULTILINE)
    numbermatchs = []
    numbermatchs2 = []
    boardmatchs = []   
    boardmatchs2 = [] 
    for line in input_file:
        numbermatchs.append(list(bingo_number_seq.findall(line)))
        boardmatchs.append(list(bingo_board_seq.findall(line)))
 
    for match in numbermatchs:
        if match == []:
            continue
        else:
            for number in match:
                numbermatchs2.append(number)

    for match in boardmatchs:
        if match == []:
            continue
        else:
            for number in match:
                boardmatchs2.append(number)

    bingo_numbers = convertregexlist2numberlist(numbermatchs2)
    # print("bingo_numbers is",bingo_numbers)
    bingo_boards_data = convertregexlist2numberlist(boardmatchs2)
    print(bingo_boards_data)
    numberOfBingo = 0
    bingo_boards = create_boards_from_data(bingo_boards_data)
    stopppart1 = False
    stopppart2 = False
    number_of_board = len(bingo_boards)
    print("number_of_board",number_of_board)
    for index,num in enumerate(bingo_numbers):  
        print("current number:",num)        
        for board in bingo_boards:
            if board.isBINGO() == False:
                board.check_number_mark(num)
                if board.isBINGO():
                    numberOfBingo = numberOfBingo+1
                    print("found_Bingo")   
                    board.print()               
                    print("numberOfBingoboard:",numberOfBingo)       
                    if stopppart1 == False:
                        stopppart1 = True
                        print("part 1 result: ",num*board.sumofunmarked())
                    if (numberOfBingo == number_of_board):
                        stopppart2 = True
                        print("found last Bingo Board")
                        print(num)
                        print(board.sumofunmarked())
                        print("part 2 result: ",num*board.sumofunmarked())
                        break
                    # bingo_boards.remove(board)
                    # print(len(bingo_boards))
        if stopppart2 == True:
            break
    input()