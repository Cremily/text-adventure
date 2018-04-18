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
            inv_string += key + "."
        elif count <(len(PLAYER_INV)-1):
            inv_string += key + ", "
        else:
            inv_string += "and the " + key + "."
    print(inv_string)
    return True
def remove_item(name):
    if name in PLAYER_INV:
        del PLAYER_INV[name]
class Room:
    """This is a room."""
    def __init__(self,name):
        self.name = name
    def room_def(self,description,directions,items,interacts,look_desc):
        self.desc = description
        self.direc = directions
        self.item = items
        self.interact = interacts
        self.look = look_desc
    def add_item(self,item_pair):
        self.item.append(item_pair)
    def add_direc(self,direc_pair):
        self.direc.update(direc_pair)
    def add_interact(self,inter_pair):
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
                item_string += "and an " + key.name + "."

        inter_string = "You can see a "
        for count,key in enumerate(self.interact):
            if len(self.interact) == 1:
                inter_string += key.name + "."
            elif count <(len(self.interact)-2):
                inter_string += key.name + ", a "
            elif count < (len(self.interact)-1):
                inter_string += key.name + ", "
            else:
                inter_string += "and an " + key.name + "."

        print(Fore.RED + self.name + Style.RESET_ALL)
        print(self.desc)
        if direc_string != "You can go ":
            print(direc_string)
        if item_string != "There is a ":
            print(item_string)
        if inter_string != "You can see a ":
            print(inter_string) 
    def read_obj(self,obj):
        for item in self.item:
            if obj == item.name.lower():
                print(item.description)
                return
        for item in PLAYER_INV:
            if obj == PLAYER_INV[item].name.lower():
                print(item.description)
                return
        for inter in self.interact:
            if obj == inter.name.lower():
                print(inter.description)
                return 
        for direc in self.direc:
            print(direc.lower())
            if obj == direc.lower():
                print(self.direc[direc].look)
                return
        else:
            print("What are you looking at? There's no %s!" % (obj))
            return False
    def take_item(self,item):
        for obj in self.item:
            if obj.name.lower() == item.lower():
                PLAYER_INV.update({obj.name:obj})
                print("You take the %s." % obj.name)
                self.delete_item(obj)
                return True
        else:
            print("There's no %s in this room!" % (item))
            return False
    def change_room(self,direction):
        for room in self.direc:
            if room.lower() == direction:
                if isinstance(self.direc[room],EndRoom):
                    self.end_game()
                    return
                self.direc[room].read_room()
                return self.direc[room]
        else:
            print("You can't go %s! Try a direction in this room!" % direction)
            return self
    def delete_item(self,del_item):
        if del_item in self.item:
            new_item_list = []
            for item in self.item:
                if item != del_item:
                    new_item_list.append(item)
            self.item = new_item_list 
            return
        try:
            del(PLAYER_INV[del_item.name])
        except Exception as e:
            print(del_item.name,e)
    def delete_interact(self,del_inter):
        if del_inter.name in self.interact:
            new_inter_list = []
            for interact in self.interact:
                if interact != del_inter.name:
                    new_inter_list.append(interact)
            self.interact = new_inter_list
    def use_item(self,first,second):
        inter_obj = ""
        item_obj = ""
        for inter in self.interact:
            if inter.name.lower() == second:
                inter_obj = inter
        if inter_obj == "":
            print("I don't see a %s in this room!" % (second))
            return
        for item in PLAYER_INV:
            if PLAYER_INV[item].name.lower() == first:
                item_obj = PLAYER_INV[item]
        for item in self.item:
            if item.name.lower() == first:
                item_obj = item
        if item_obj == "":
            print("I don't see a %s to use!" % (first))
            return
        print(inter_obj,item_obj)
        if isinstance(inter_obj,Chest):
            if isinstance(item_obj,Key):
                inter_obj.unlock_chest(self,item_obj)     
        elif isinstance(inter_obj,Door):
            if isinstance(item_obj,Key):
                inter_obj.unlock_door(self,item_obj)
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
                if word not in ["the","to","at","in"]:
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
                    continue
            if verb == "go" or verb == "move":
                self = self.change_room(phrase)
            if verb == "take" or verb == "grab":
                self.take_item(phrase)
            if verb == "look" and phrase == "room":
                self.read_room()
                continue
            if verb == "look":
                self.read_obj(phrase)
            if verb == "use":
                nphrase = phrase.split(" on ")
                test_phrase = ""
                for x in nphrase:
                    test_phrase += x
                if test_phrase == phrase:
                    nphrase = phrase.split(" with ")
                print(nphrase)
                if len(nphrase) == 1:
                    self.use_inter(nphrase)
                else: 
                    self.use_item(nphrase[0],nphrase[1])
        else: 
            print("You are amazing! Well Done!")                          
    def end_game(self):
        global GAME_ON
        GAME_ON = False
        return
    
class EndRoom(Room):
    def __init__(self,name):
        Room.__init__(self,name)
    def room_def(self,look):
        self.look = look
class Item:
    def __init__(self,name,description):
        self.name = name
        self.description = description
class Key(Item):
    def __init__(self,name,description):
        Item.__init__(self,name,description)
class Chest(Item):
    def __init__(self,name,description,keys,contents,unlock_str):
        Item.__init__(self,name,description)
        self.key = keys
        self.content = contents
        self.string = unlock_str
    def unlock_chest(self,room,key):
            for unlock_keys in self.key:
                if key.name == unlock_keys.name:
                    for item in self.content:
                        room.add_item(item)
                    print(self.string)
                    room.delete_item(key)
                    remove_item(key)
                    room.delete_interact(self)
                    break
            else:
                    print("That doesn't unlock %s!" % (self.name))
class Door(Item):
    def __init__(self,name,description,keys,directions,unlock_str):
        Item.__init__(self,name,description)
        self.key = keys
        self.direction = directions
        self.string = unlock_str
    def unlock_door(self,room,key):
        for unlock_keys in self.key:
            if key.name.lower() == unlock_keys.name.lower():
                for direc in self.direction:
                    room.add_direc({direc:self.direction[direc]})
                print(self.string)
                room.delete_item(key)
                remove_item(key)
                room.delete_interact(self)
                break
        else:
            print("That doesn't unlock the %s!" % (self.name))



SmallKey = Key("Useless key","Opens nothing.")
BigKey = Key("Stone Key","Opens the big chest.")
IronKey = Key("Iron Key","Comes from the test chest!")
TestChest = Chest("Chest","This is a test",[BigKey],[IronKey],"The chest bursts open, revealing a %s" % (IronKey.name))
TestRoom = Room("Testing Room")
NextRoom = Room("Testing Room 2")
Finish = EndRoom("Ending Room")
BigDoor = Door("Iron Door","Big and Iron.",[IronKey],{"East":Finish},"The door unlocks, letting you leave the cave!")
TestRoom.room_def("This is a room!",{'North':NextRoom},[BigKey],[TestChest,BigDoor],"Where you woke up.")
NextRoom.room_def("This is another room!",{'South':TestRoom},[BigKey],[],"Another cave.")
Finish.room_def("The outside!")
TestRoom.read_room()
TestRoom.take_words()