global PLAYER_INV
PLAYER_INV = {}
GAME_ON = True
from colorama import init
init()
from colorama import Fore,Back,Style
def read_inventory():
    if len(PLAYER_INV) == 0:
        print("You aren't carrying anything!")
        return False
    inv_string = "You have the "
    for count,key in enumerate(PLAYER_INV):
        if len(PLAYER_INV) == 1:
            inv_string += PLAYER_INV[key][0] + "."
        elif count <(len(PLAYER_INV)-1):
            inv_string += PLAYER_INV[key][0] + ", "
        else:
            inv_string += "and the " + PLAYER_INV[key][0] + "."
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
        if direc_string != "You can go ":
            print(direc_string)
        if item_string != "There is a ":
            print(item_string)
        for count,key in enumerate(self.interact):
            print(self.interact[key][0])
    def read_object(self,obj):
        if obj in self.item:
            print(self.item[obj][1])
            return True
        if obj in PLAYER_INV:
            print(PLAYER_INV[obj][1])
            return True
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
    def use_item(self,item,room):
        if item in PLAYER_INV:
            try:
                if item == self.interact[room][2]:
                    print("You used the %s on the %s" % (item,room))
                    print(self.interact[room][3])
                    for command in self.interact[room][4]:
                        exec(command)
                else:
                    print("I don't know how to use %s on %s" % (item,room))
            except Exception as e:
                print(e)
        else:
            print("You don't have an %s" % (item))
    def take_words(self):
        while GAME_ON == True:
            player_in = input("What would you like to do? ")
            verb = ""
            phrase = ""
            words = []
            unclean_input = []
            player_in = player_in.split(" ")
            for x in player_in:
                unclean_input.append(x.lower())
            for word in unclean_input:
                if word != "the" and word != "to" and word != "at":
                    words.append(word)
            verb = words[0]
            del(words[0])
            for length,word in enumerate(words):
                if length != len(words) - 1:
                    phrase += word + " "
                else:
                    phrase += word
            if verb == "exit" or verb == "quit":
                print('Goodbye!')
                break
            if phrase == '':
                if verb == "room" or (verb == "look"):
                    self.read_room()
                    continue
                if verb == "go" or verb == "move":
                    print("Go where? Try again.")
                    continue
                if verb == ("take" or "grab"): 
                    print("What would you like to take? Try again.")
                    continue
                if verb == "inventory" or verb == "inv":
                    read_inventory()
            if verb == "go" or verb == "move":
                self = self.change_room(phrase)
            if verb == "take" or verb == "grab":
                self.take_item(phrase)
            if verb == "look":
                self.read_object(phrase)
            if verb == "use":
                nphrase = phrase.split(" on ")
                if str(nphrase) == phrase:
                    nphrase = nphrase.split(" with ")
                self.use_item(nphrase[0],nphrase[1])
        else: 
            print("You are amazing! Well Done!")                          
    def end_game(self):
        global GAME_ON
        GAME_ON = False
        return

CurrRoom = RoomClass("ERROR")   
EmptyCave = RoomClass("Empty Cave")
NextRoom = RoomClass("Another Cave")
global Door_Key
Door_Key = {"stone key":["Stone Key","It's a stone key. Looks like it's for the door."]}
EmptyCave.room_def("It's an empty cave!... Except for those twigs. And that door.",
                      {"north":["North",NextRoom]},
                      {"small twig": ["Small Twig","It's small. Twiggy."],
                      "big twig": ["Big Twig","It's big. More Twiggy."],
                      "medium twig":["Medium Twig","It's medium. Somewhat Twiggy."]},
                      {"door":["There is a locked Door.","Big. Stone. Scawwy.","stone key","self.end_game()"],
                       "chest":["There is a locked Chest.","Same stone as the door.", "key","The chest reveals a stone key! You discard the chest.",["self.add_item(Door_Key)","""del self.interact["chest"]""","""del PLAYER_INV[key]"""]]})
NextRoom.room_def("It's another empty cave!... Except for that key.",
                  {"south":["South",EmptyCave]},
                  {"key":["Key","It's a key. Probably to use on that chest, ey?"]},
                  {})
CurrRoom = NextRoom
CurrRoom.take_item("key")
CurrRoom = EmptyCave
print(PLAYER_INV)
CurrRoom.read_room()
CurrRoom.take_words()
