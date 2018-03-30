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
def remove_item(name):
    if name in PLAYER_INV:
        del PLAYER_INV[name]

class Room:
    """This is a room."""
    def __init__(self,name):
        self.name = name
    def room_def(self,description,directions,items,interacts):
        self.desc = description
        self.direc = directions
        self.item = items
        self.interact = interacts
    def add_item(self,item_pair):
        self.item.append(item_pair)
    def add_direc(self,direc_pair):
        self.direc.update(direc_pair)
    def add_interacts(self,inter_pair):
        self.interact.update(inter_pair)
    def read_room(self):

        direc_string = "You can go "
        for count,key in enumerate(self.direc):
            if len(self.direc) == 1:
                direc_string += key + "."
            elif count <(len(self.direc)-1):
                direc_string += key + ", "
            else:
                direc_string += "and " + key + "."

        item_string = "There is a "
        for count,key in enumerate(self.item):
            if len(self.item) == 1:
                item_string += key.name + "."
            elif count < (len(self.item) -2):
                item_string += key.name + ", a "
            elif count < (len(self.item)-1):
                item_string += key.name + ", "
            else:
                item_string += "and a " + key.name + "."

        inter_string = "You can see a "
        for count,key in enumerate(self.interact):
            if len(self.interact) == 1:
                inter_string += key.name + "."
            elif count <(len(self.item)-2):
                inter_string += key.name + ", a "
            elif count < (len(self.item)-1):
                item_string += key.name + ", "
            else:
                item_string += "and a " + key.name + "."

        print(Fore.RED + self.name + Style.RESET_ALL)
        print(self.desc)
        if direc_string != "You can go ":
            print(direc_string)
        if item_string != "There is a ":
            print(item_string)
        if inter_string != "You can see a ":
            print(inter_string)
       
        
    def read_item(self,obj):
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
    def delete_item(self,del_item):
        if del_item.name in self.item:
            new_item_list = []
            for item in self.item:
                if item != del_item.name:
                    new_item_list.append(item)
            self.item = new_item_list 
    def delete_interact(self,del_inter):
        if del_inter.name in self.interact:
            new_inter_list = []
            for interact in self.interact:
                if interact != del_inter.name:
                    new_inter_list.append(interact)
            self.inter = new_inter_list
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
                self.read_Item(phrase)
            if verb == "use":
                nphrase = phrase.split(" on ")
                test_phrase = ""
                for x in nphrase:
                    test_phrase += x
                if test_phrase == phrase:
                    nphrase = phrase.split(" with ")
                self.use_item(nphrase[0],nphrase[1])
        else: 
            print("You are amazing! Well Done!")                          
    def end_game(self):
        global GAME_ON
        GAME_ON = False
        return
    def use_item(self,first,second):
        inter_obj = ""
        item_obj = ""
        for inter in self.interact:
            print(inter.name.lower(),second)
            if inter.name.lower() == second:
                inter_obj = inter
        if inter_obj == "":
            print("I don't see a %s in this room!" % (second))
            return
        for item in PLAYER_INV:
            if item.name.lower() == first:
                item_obj = item
        for item in self.item:
            print(item.name.lower(),first)
            if item.name.lower() == first:
                item_obj = item
        if item_obj == "":
            print("I don't see a %s to use!" % (first))
            return
        if isinstance(inter_obj,Chest):
            if isinstance(item_obj,Key):
                inter_obj.unlock_chest(self,item_obj)
        
        

                
        
class Item:
    def __init__(self,name,description):
        self.name = name
        self.description = description
class Key(Item):
    def __init__(self,name,description):
        Item.__init__(self,name,description)
class Chest(Item):
    def __init__(self,name,description,keys,contents):
        Item.__init__(self,name,description)
        self.key = keys
        self.content = contents
    def unlock_chest(self,room,key):
            for unlock_keys in self.key:
                if key.name == unlock_keys.name:
                    for item in self.content:
                        print(item)
                        room.add_item(item)
                    break
            else:
                print("That key doesn't open this chest!")
SmallKey = Key("Useless key","Opens nothing.")
BigKey = Key("Stone Key","Opens the big chest.")
AnItem = Item("Test Item","Comes from the test chest!")          
TestChest = Chest("Chest","This is a test",[BigKey],[AnItem])
TestRoom = Room("Testing Room")
NextRoom = Room("Testing Room 2")
TestRoom.room_def("This is a room!",{'North':NextRoom},[BigKey],[TestChest])
TestRoom.read_room()
TestRoom.take_words()