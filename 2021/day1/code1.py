import re
import sys

file_name = sys.argv[1]
input_file = open(file_name, "r")
rx_sequence = re.compile (r"^(\d+)\s",re.MULTILINE)
matchs = rx_sequence.finditer (input_file.read())
measurements = list(matchs)
counter1 = 0
for index,measurement in enumerate(measurements):
    try:
        if int(measurement[1]) < int(measurements[index+1][1]):
            counter1 = counter1 + 1
    except:
        break

# print(counter1)
counter2 = 0
for index,measurement in enumerate(measurements):
    try:
        if int(measurements[index][1]) < int(measurements[index+3][1]):
            counter2 = counter2 + 1
    except:
        break

print(counter2)
input()