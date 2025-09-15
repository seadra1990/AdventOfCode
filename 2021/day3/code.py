import re
import sys

def getthemostcommonvalue(lst,index):
    number1cnt = 0
    number0cnt = 0
    for rowindex,match_line in enumerate(lst):
        try:
            if match_line[index] == '1':
                number1cnt = number1cnt+1
            elif match_line[index] == '0':
                number0cnt = number0cnt+1
            else:
                print("ERROR processing regex")
        except:
            print(index)
            print("ERROR happened for trying process regex output")
            break
    if number1cnt > number0cnt:
        mostcommon = '1'
        leastcommon = '0'
    elif number1cnt < number0cnt:
        mostcommon = '0'
        leastcommon = '1'
    else:
        mostcommon = '1'
        leastcommon = '1'
    print ("counter: ",number1cnt,number0cnt)
    return mostcommon,leastcommon

def removedatabychar(lst,index,char):
    length = len(lst)
    remove_index = []

    for i in range(length):
        try:
            print("index :",i,"data :",lst[i])
            if lst[i][index] == char:
                print("data removed! ")
                remove_index.append(i)
        except:
            print("ERROR at index: ",i)
    for i in reversed(list(remove_index)):
        lst.pop(i)
    # return lst

def decodebinarr2decnumber(lst):
    temp = 0
    print(lst)
    for i in range(len(lst)):
        try:
            if lst[i] == '1':
                temp = temp + (1<<(len(lst)-1-i))
            elif lst[i] == '0':
                temp = temp + (0<<(len(lst)-1-i))
            else:
                
                print("ERROR number 0 and 1 is not equal")
        except:
            print("ERROR in index:",i)
            raise Exception
    return temp

if __name__ == '__main__':
    file_name = sys.argv[1]
    input_file = open(file_name, "r")
    rx_sequence = re.compile (r"(\d)",re.MULTILINE)
    matchs = []
    for line in input_file:
        matchs.append(list(rx_sequence.findall(line)))
    gamma = 0
    epsilon = 0

    numberofbit = 0

    number0 = []
    number1 = []

    for rowindex,match_line in enumerate(matchs):
        # print(len(match_line))
        numberofbit = max(numberofbit, len(match_line))

    for i in range(numberofbit):
        number0.append(0)
        number1.append(0)

    for rowindex,match_line in enumerate(matchs):
        for columnindex,char in reversed(list(enumerate(match_line))):#process from bit 0
            try:
                if char == '1':
                    number1[columnindex] = number1[columnindex]+1
                elif char == '0':
                    number0[columnindex] = number0[columnindex]+1
                else:
                    print("ERROR processing regex")
            except:
                print("ERROR happened for trying process regex output")
                break

    print("number 0: ",number0)
    print("number 1: ",number1)
    for i in range(numberofbit):
        if number1[i] > number0[i]:
            print("1 at position " +str(numberofbit-1-i) )
            gamma = gamma + (1<<(numberofbit-1-i))
            # print("gama is: " ,gamma)
        elif number1[i] < number0[i]:
            print("0 at position "+str(numberofbit-1-i) )
            epsilon = epsilon + (1<<numberofbit-1-i)
            # print("epsilon is: " ,epsilon)
        else:
            print("ERROR number 0 and 1 is equal")

    multiple = gamma*epsilon


    oxygen_data = list(matchs)
    co2_data = list(matchs)
    found_oxygen = False
    found_co2 = False
    index = 0
    last_mc = '1'
    last_lc = '0'
    while(found_oxygen != True):
        print("index master: ", index)
        mc,lc = getthemostcommonvalue(oxygen_data,index)
        remove_count = 0
        remove_count1 = 0
        if (mc == lc):
            mc = '1'
            lc = '0'
        print(mc,lc)
        print("oxygen before:", len(oxygen_data))
        removedatabychar(oxygen_data,index,lc)
        print("oxygen after:", len(oxygen_data))

        if len(oxygen_data) == 1:
            found_oxygen = True   
        index = index +1
        if index == numberofbit:
            found_oxygen = True

    index1 = 0    
    while(found_co2 != True):
        print("index master: ", index1)
        mc,lc = getthemostcommonvalue(co2_data,index1)
        remove_count = 0
        remove_count1 = 0
        if (mc == lc):
            mc = '1'
            lc = '0'
        print(mc,lc)
        print("co2 before:", len(co2_data))
        removedatabychar(co2_data,index1,mc)
        print("co2 after:", len(co2_data))

        if len(co2_data) == 1:
            found_co2 = True   
        index1 = index1 +1
        if index1 == numberofbit:
            found_co2 = True

    oxygen = decodebinarr2decnumber(oxygen_data[0])
    co2 = decodebinarr2decnumber(co2_data[0])
    print((oxygen))
    print((co2))
    print(oxygen*co2)

    input()