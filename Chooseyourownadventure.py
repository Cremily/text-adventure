GAME_ON = True
PLAYER_INV = {}
from colorama import init
init()
from colorama import Fore,Back,Style
def read_inventory():
    if len(PLAYER_INV) == 0:
        print("You aren't carrying anything!")
        return False
    inv_string = "You have a "
    for count,key in enumerate(PLAYER_INV):
        if len(PLAYER_INV) == 1:
            inv_string += PLAYER_INV[key][0] + "."
        elif count <(len(PLAYER_INV)-1):
            inv_string += PLAYER_INV[key][0] + ","
        else:
            inv_string += "and " + PLAYER_INV[key][0] + "."
    print(inv_string)
    return True
class RoomClass:
    """This is a room."""
    def __init__(self,name):
        self.name = name
    def room_def(self,description,directions,items,interacts):
        self.desc = description
        self.direc = directions
        self.item = items
        self.interact = interacts
    def add_item(self,item_pair):
        self.item.update(item_pair)
    def add_direc(self,direc_pair):
        self.direc.update(direc_pair)
    def add_interacts(self,inter_pair):
        self.interact.update(inter_pair)
    def read_room(self):
        direc_string = "You can go "
        for count,key in enumerate(self.direc):
            if len(self.direc) == 1:
                direc_string += self.direc[key][0] + "."
            elif count <(len(self.direc)-1):
                direc_string += self.direc[key][0] + ", "
            else:
                direc_string += "and " + self.direc[key][0] + "."
        item_string = "There is a "
        for count,key in enumerate(self.item):
            if len(self.item) == 1:
                item_string += self.item[key][0] + "."
            elif count < (len(self.item) -2):
                item_string += self.item[key][0] + ", a "
            elif count < (len(self.item)-1):
                item_string += self.item[key][0] + ", "
            else:
                item_string += "and a " + self.item[key][0] + "."
        print(Fore.RED + self.name + Style.RESET_ALL)
        print(self.desc)
        print(direc_string)
        print(item_string)
        for count,key in enumerate(self.interact):
            print(self.interact[key][0])
    def read_object(self,obj):
        if obj in self.item:
            print(self.item[obj][1])
            return True
        if obj in PLAYER_INV:
            print(PLAYER_INV[obj][1])
        elif obj in self.interact:
            print(self.interact[obj][1])
            return True
        else:
            print("What are you looking at? There's no %s" % (obj))
            return False
    def take_item(self,item):
        if item in self.item:
            PLAYER_INV.update({item:self.item[item]})
            print("You take the %s." % (self.item[item][0]))
            del self.item[item]
            return True
        else:
            print("There's no %s in this room!" % (item))
            return False
    def change_room(self,direction):
        if direction in self.direc:
            self.direc[direction][1].read_room()
            return self.direc[direction][1]
        else:
            print("You can't go %s! Try a direction in this room!" % direction)
            return self
    def take_words(self):
        while True:
            player_in = input("What would you like to do? ")
            words = []
            player_in = player_in.split(" ")
            for x in player_in:
                words.append(x.lower())
            if words[0] == "exit" or words[0] == "quit":
                break
            if len(words) == 1:
                if words[0] == "room" or (words[0] == "look"):
                    self.read_room()
                if words[0] == "go" or words[0] == "move":
                    print("Go where? Try again.")
                    continue
                if words[0] == ("take" or "grab"): 
                    print("What would you like to take? Try again.")
                    continue
            if words[0] == "go" or words[0] == "move":
                    self = self.change_room(words[len(words)-1])
            if words[0] == ("take" or "grab"):
                pass

                    
    def end_game(self):
        print("You win the game! You are amazing!")
        GAME_ON = False

CurrRoom = RoomClass("ERROR")   
EmptyCave = RoomClass("Empty Cave")
NextRoom = RoomClass("Another Cave")

EmptyCave.room_def("It's an empty cave!... Except for those twigs. And that door.",
                      {"north":["North",NextRoom]},
                      {"small twig": ["Small Twig","It's small. Twiggy."],
                      "big twig": ["Big Twig","It's big. More Twiggy."],
                      "medium twig":["Medium Twig","It's medium. Somewhat Twiggy."]},
                      {"door":["There is a locked Door.","Big. Stone. Scawwy.","key",EmptyCave.end_game]})
NextRoom.room_def("It's another empty cave!... Except for that key.",
                  {"south":["South",EmptyCave]},
                  {"key":["Key","It's a key. Probably to use on that door, ey?"]},
                  {})
CurrRoom = EmptyCave
CurrRoom.read_room()
CurrRoom.take_words()
