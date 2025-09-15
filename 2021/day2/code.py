import re
import sys

move_list = ["forward","up","down"]

file_name = sys.argv[1]
input_file = open(file_name, "r")
rx_sequence = re.compile (r"^(\w+) (\d+)\s",re.MULTILINE)
matchs = list(rx_sequence.finditer (input_file.read()))
posX = 0
posY = 0
aim = 0
# print(move_list[0])
# print(move_list[1])
# print(move_list[2])

for index,match_item in enumerate(matchs):
    try:
        # print(match_item[1])
        # print(match_item[2])
        if  str(match_item[1]).strip() == move_list[0].strip():
            posX = posX + int(match_item[2])
            posY = posY + (aim*int(match_item[2]))
        elif str(match_item[1]).strip() == move_list[1].strip():
            # posY =  posY - int(match_item[2])
            aim = aim - int(match_item[2])
        elif str(match_item[1]).strip() == move_list[2].strip():
            # posY =  posY + int(match_item[2])
            aim = aim + int(match_item[2])
        else:
            print("ERROR happened for regex")

        # print(posX)
        # print(posY)
        # print(aim)
        # print("\n")
    except:
        break

multiply = posX*posY
# print(posX)
# print(posY)
# print(aim)
print(multiply)
input()