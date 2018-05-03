nodes = [[1, 2, 3], [0, 3, 7], [0, 3, 6],
            [0, 1, 2, 4, 5, 6, 7], [3, 7], [3, 6], [2, 3, 5], [1, 3, 4]]
gateways = [4, 5]
dist_dict = {}
def cut_link(n1,n2):
    global nodes
    n1_index = nodes[n2].index(n1)
    n2_index = nodes[n1].index(n2)
    global ans
    ans = "%s %s" % (n1,n2)
    del nodes[n1][n2_index]
    del nodes[n2][n1_index]
for gateway in gateways:
    dist_dict.update({gateway:{}})
def dist_func():
    global nodes
    global gateways
    global dist_dict
    node_list = gateways
    for gateway in node_list:
        dist = 1
        connectors = [gateway]
        node_list = []
        node_list.append(gateway)
        while dist < len(nodes):
            dist_list = []
            for connector in connectors:
                print(gateway,connector,nodes[connector])
                for connec_node in nodes[connector]:
                    if connec_node not in node_list:
                        node_list.append(connec_node)
                        dist_list.append(connec_node)
                dist_dict[gateway].update({dist:dist_list})
            connectors = dist_list
            dist += 1
    return True
agent = 0
def find_path_to_gateway(agent,gateway):
    global nodes
    connec_list = [agent]
    total_nodes = []
    for dist in range(1,len(nodes)):
        for node in connec_list:
            if gateway in nodes[node]:
                return([gateway,dist,node])
        for node in connec_list:
            if node not in total_nodes:
                total_nodes.append(node)
                connec_list = nodes[node]
                break
    print(connec_list)
def path_picker(agent):
    global gateways
    global nodes
    gateway_dist = []
    for gateway in gateways:
        if len(nodes[gateway]) != 0:
            gateway_dist.append(find_path_to_gateway(agent,gateway))
    for gateway in gateway_dist:
        if gateway[1] == 1:
            return([gateway[0],gateway[2]])
    lowest = 10000000
    gateway_chosen = []
    for gateway in gateway_dist:
        if gateway[1] <= lowest:
            lowest = gateway[1]
            gateway_chosen.append([gateway[0],gateway[2]])
    sec_node_list = []
    for gateway in gateway_chosen:
        if len(nodes[gateway[0]]) > 1:
            sec_node_list.append(gateway)
    if len(sec_node_list) > 2:
        print("I WAS WRONG")
    if len(sec_node_list) == 1:
        return(sec_node_list[0])
    elif len(sec_node_list) == 2:
        return(sec_node_list[0])
    else:
        return(gateway_chosen[0])

            


dist_func()
print(find_path_to_gateway(1,4))
result = path_picker(agent)
cut_link(result[0],result[1])
print(ans)
agent = 3
result = path_picker(agent)
cut_link(result[0],result[1])
print(ans)
agent = 1
result = path_picker(agent)
cut_link(result[0],result[1])
print
