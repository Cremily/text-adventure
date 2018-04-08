from random import randint
test_list = []
results_list = []
winners = []

loop = 0
for x in range(0,100):
    test_list.append([x,0,0])
while len(test_list) > 1:
    indicies = []
    players_left = len(test_list) - 1
    player1 = randint(0,players_left)
    player2 = randint(0,players_left)
    if player1 == player2:
        continue
    loop += 1
    test_list[player1][1] += 1
    test_list[player2][2] += 1
    try:
        if test_list[player1][1] == 12:
            results_list.append(test_list[player1])
            indicies.append(player1)
        if test_list[player2][2] == 3:
            results_list.append(test_list[player2])
            indicies.append(player2)
    except Exception as error:
        print(error)
        print(player1,player2,players_left)
    newindex = sorted(indicies,reverse=True)
    for thing in newindex:
        del test_list[thing]
    if loop % 100 == 0:
        print(loop)
else:
    results_list.append(test_list[0])
    del test_list[0]
for index,winner in enumerate(results_list):
    if winner[2]< 3:
        winners.append(winner)
        del results_list[index] 
print(results_list)
print(winners)