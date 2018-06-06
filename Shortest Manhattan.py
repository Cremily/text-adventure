import sys
import math
from statistics import median
building_list = [[-416604701, 690825290], [-334087877, -290840615], [-28189131, 593661218], [19715507, 470868309], [102460950, 1038903636], [842560881, -116496866], [846505116, -694479954], [938059973, -816049599]]
reverse_list = [[-816049599, 938059973], [-694479954, 846505116], [-290840615, -334087877], [-116496866, 842560881], [470868309, 19715507], [593661218, -28189131], [690825290, -416604701], [1038903636, 102460950]]
wire_y_value = 0
if len(building_list) == 1:
    wire_y_value = building_list[0][0]
    x = building_list[0][0]
elif len(building_list) % 2 == 1:
    n = median(reverse_list)
    wire_y_value = reverse_list[n][0]
else:
    n = (len(reverse_list) // 2)
    wire_y_value = (reverse_list[n-1][0] + reverse_list[n][0]) // 2
length = 0
print(wire_y_value,file=sys.stderr)
x = building_list[0][0]
for building in building_list:
    length += abs(building[1] - wire_y_value)
    length += abs(building[0] - x)
    x = building[0]
print(length)
print(length - 6066790161)