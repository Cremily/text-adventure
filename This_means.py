import sys
import math
p1 = ['5', '3', '2', '7', '8', '7', '5', '5', '6', '5', '4', '6', '6', '3', '3', '7', '4', '4', '7', '4', '2', '6', '8', '3', '2', '2']
p2 = ['A', '9', 'K', 'K', 'K', 'K', '1', '1', '9', 'Q', 'J', '1', '8', 'Q', 'J', 'A', 'J', 'A', 'Q', 'A', 'J', '1', '9', '8', 'Q', '9']
p1_new = []
p2_new = []
for character in p1:
    if character == 'A':
        p1_new.append(14)
    elif character == 'K':
        p1_new.append(13)
    elif character == 'Q':
        p1_new.append(12)
    elif character == 'J':
        p1_new.append(11)
    else:
        p1_new.append(int(character))
for character in p2:
    if character == 'A':
        p2_new.append(14)
    elif character == 'K':
        p2_new.append(13)
    elif character == 'Q':
        p2_new.append(12)
    elif character == 'J':
        p2_new.append(11)
    else:
        p2_new.append(int(character))
p1 = p1_new
p2 = p2_new
print(p1,p2)
rounds = 0
p1_war = []
p2_war = []
def normal_win(winner_list,loser_list):
    winner_list.append(winner_list[0])
    winner_list.append(loser_list[0])
    del(winner_list[0])
    del(loser_list[0])
def war_replace():
    global p1_war
    global p2_war
    global p1
    global p2
    for x in range(0,4):
        p1_war.append(p1[x])
        p2_war.append(p2[x])
    p1 = p1[4:]
    p2 = p2[4:]

while (len(p1) != 0 and len(p2) != 0):
    rounds += 1
    if p1[0] < p2[0]: #player 2 wins!
        normal_win(p2,p1)
    elif p1[0] > p2[0]: #player 1 wins!
        normal_win(p1,p2)
    else: # THIS MEANS WAR!
        war_replace()
        print(p1,p2)
        while len(p1) != 0 or len(p2) != 0:
            if p1[0] == p2[0]:
                #the war continues!
                war_replace
                continue
            elif p2[0] < p1[0]:
                #player 1 wins the war!
                p1.append(p1_war)
                p1.append(p2_war)
                p1_war = []
                p2_war = []


                

                
            

else:
    if len(p1) == 0:
        print("2 " + str(rounds) )
    elif len(p2) == 0:
        print("1 " + str(rounds) )
    else:
        print("PAT")
        
        