influences = [[1, 2], [1, 3], [3, 4], [2, 4], [2, 5], [10, 11], [10, 1], [10, 3]]
node_dict = {}
for lst in influences:
    node_dict.update({lst[0]:[]})
for lst in influences:
    node_dict[lst[0]].append(lst[1])
print(influences)
def distance_from_node(start,node_dict):
    max_path = 2
    prio_list = node_dict[start]
    while max_path < len(influences):
        new_prio = []
        for node in prio_list:
            try:
                add_list = node_dict[node]
                for thing in add_list:
                    new_prio.append(thing)
            except Exception:
                pass
        if new_prio == []:
            break
        max_path += 1
        prio_list = new_prio
    return max_path 
distance_list = []
for node in node_dict:
    distance_list.append((distance_from_node(node,node_dict)))
print(max(distance_list))
