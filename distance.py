nodes = [[1, 6, 7, 9, 10, 11], [0, 2, 3, 4, 6, 7], [1, 3, 4, 5, 33, 34, 35], [1, 2, 8, 19, 20, 33], [1, 2, 5, 6], [2, 4, 35], [0, 1, 4, 11, 12], [0, 1, 9, 13, 36], [3, 16, 17, 19, 36], [0, 7, 10, 13, 14], [0, 9, 11, 14], [0, 6, 10, 12], [6, 11], [7, 9, 14, 15, 16, 36], [9, 10, 13, 15], [13, 14, 16, 23, 24], [8, 13, 15, 17, 23, 27, 30], [8, 16, 18, 19, 31, 32], [17, 19, 22, 32], [3, 8, 17, 18, 20, 21, 22], [3, 19, 21], [19, 20, 22, 32], [18, 19, 21, 32], [15, 16, 24, 25, 27], [15, 23, 25], [23, 24, 26, 27], [25, 27, 28], [16, 23, 25, 26, 28, 29, 30], [26, 27, 29], [27, 28, 30], [16, 27, 29], [17, 32], [17, 18, 21, 22, 31], [2, 3, 34], [2, 33, 35], [2, 5, 34], [7, 8, 13]]
gateways = [0, 16, 18, 26]
def cut_link(n1,n2):
    global nodes
    n1_index = nodes[n2].index(n1)
    n2_index = nodes[n1].index(n2)
    global ans
    ans = "%s %s" % (n1,n2)
    del nodes[n1][n2_index]
    del nodes[n2][n1_index]
    print(ans)
    return True
def distance_func(agent):
    global nodes
    global gateways
    dist_dict = {}
    for index,_ in enumerate(nodes):
        dist_dict.update({index:[float("inf"),-1]})
    dist_dict.update({agent:[0,agent]})
    prio_list = [agent]
    done_list = [agent]
    dist = 1
    while dist < (len(nodes)):
        new_prio = []
        for base in prio_list:
            done_list.append(base)
            for node in nodes[base]:
                if node not in done_list:
                    new_prio.append(node)
                if dist < dist_dict[node][0]:
                    dist_dict.update({node:[dist,base]})
        prio_list = set(new_prio)
        new_prio = list(prio_list)
        dist += 1
    return dist_dict
while True:
    ans = ""
    agent = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    #calculates distance to gateways from agent
    
    dist_dict = distance_func(agent)
    #print(dist_dict,file=sys.stderr)
    gateway_dist = []
    for index,gateway in enumerate(gateways):
        gateway_dist.append(dist_dict[gateway])
        gateway_dist[index].append(gateway)
    if len(gateway_dist) == 0:
        print('OOPSIE DOODLES THE LIST IS EMPTY!')
    gateway_dist.sort()
    #finds gateways with minimal distance
    lowest_value = gateway_dist[0][0]
    dist_list = []
    for gateway in gateway_dist:
        if gateway[0] == lowest_value:
            dist_list.append(gateway)
    gateway_dist = dist_list
    #finishes if dist = 1
    for gateway in gateway_dist:
        if gateway[0] == 1:
            cut_link(gateway[1],gateway[2])
            break
    if ans != "":
        continue
    # finds nodes with max gateways
    value_dict = {}
    for node in range(len(nodes)):
        value_dict.update({node:0})
    for gateway in gateways:
        for node in nodes[gateway]:
            value_dict[node] += 1
    finish_dict = {}
    top_value = 0
    for value in value_dict:
        if value_dict[value] > top_value:
            top_value = value_dict[value]
            finish_dict = {value:value_dict[value]}
        elif value_dict[value] == top_value:
            finish_dict.update({value:value_dict[value]})
    final_node = []
    for index,pair in enumerate(finish_dict):
        final_node.append(pair)
    for index,node in enumerate(final_node):
        for gateway in gateways:
            if node in nodes[gateway]:
                final_node[index] = [0,node,gateway]
                break
    for node in final_node:
        node[0] = dist_dict[node[1]][0]
    lowest = float("inf")
    final_final_node = []
    for node in final_node:
        if node[0] < lowest:
            final_final_node = node
            lowest = node[0]
    final_node = final_final_node
        
    #if final_node not empty, select one
    if len(final_final_node) == 3:
        n1 = final_node[1]
        n2 = final_node[2]
        cut_link(n1,n2)
        continue
    # finds gateways with max nodes
    gateway_connectors = {}
    for gateway in gateway_dist:
        gateway_connectors.update({gateway[2]:0})
        for node in nodes[gateway[2]]:
            gateway_connectors[gateway[2]] += 1
    max_value = 0
    final_connector = []
    for gateway in gateway_connectors:
        if gateway_connectors[gateway] > max_value:
            max_value = gateway_connectors[gateway]
            final_connector = [gateway]
        elif gateway_connectors[gateway] == max_value:
            final_connector.append(gateway)
    #checks if either nodes/connectors have one candidate
    if len(final_node) == 1:
        final_gateway = final_node[0]
    elif len(final_connector) == 1:
        for gateway in gateway_dist:
            if gateway[2] == final_connector[0]:
                final_gateway = gateway
    else:
        final_gateway = gateway_dist[0]
    cut_link(final_gateway[1],final_gateway[2])
   # print(nodes,file=sys.stderr)
    #print(gateways,file=sys.stderr)
            
   # print(nodes,file=sys.stderr)
    #print(gateways,file=sys.stderr)
            