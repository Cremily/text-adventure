import sys
import math
r = 1
l = 11
num_list = []
num_list.append(r)
count = 0
curr_list = []
def look_nice(number_list):
    string = ""
    for number in number_list:
        string += (str(number) + " ")
    return string[:-1]
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
while count < l:
    index = 0
    x = 0
    check_value = num_list[0]
    while index != len(num_list):
        if num_list[index] == check_value:
            x += 1
            index += 1
            continue
        else:   
            curr_list.append([check_value,x])
            x = 0
            check_value = num_list[index]
    else:
        curr_list.append([check_value,x])
    num_list = []
    for number in curr_list:
        num_list.append(number[1])
        num_list.append(number[0])
    num_dict = {}
    count += 1
    curr_list = []
    print(look_nice(num_list))
