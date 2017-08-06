import sys
from Game import Game
import json
from Stuff import Stuff

def readRoomFiles(roomFileNames, listOfRooms):
    for i in range(0, len(roomFileNames)):
        with open(roomFileNames[i], 'r') as name:
            listOfRooms.update(json.load(name))
    return listOfRooms

#verb with object
actionVerb = ["look", "go", "take", "drop", "hit", "eat", "open"]
directionVerb = ["north", "south", "east", "west"]
menuVerb = ["start", "loadgame", "savegame", "quit"]
#verb without object
singleVerb = ["help", "inventory"]

# verbs method ---------------------------------------

# repeats the long form explanation of the room
def lookItem(restOfTheCommand, game):
	#print restOfTheCommand[0]
    words = restOfTheCommand
	#if preposition provided
    if words and words[0] == "at":
        pos = words.index("at")
        item = " ".join(words[i] for i in range(pos+1, len(words)))
        itemValid = False
        for stuff in game.currentRoom.items:
            if item == stuff.name:
                print stuff.description
                itemValid = True
        if not itemValid:
            print "Nothing to look at."
    else:
        print game.currentRoom.longDesc

def enterRoom(room, game):
    print "Entering",
    print game.currentRoom.name

    if game.currentRoom.hasBeenVisited == False:
        print game.currentRoom.longDesc
        game.currentRoom.hasBeenVisited = True
    else:
        print game.currentRoom.shortDesc

    showItemsInTheRoom(game)
    
    print "Neighboring rooms:"
    for i in room.neighbors:
        print i.name

def directionWhere(direction, game):
    isValidNeighbor = False
    for i in game.rooms:
        if i == game.currentRoom:
            if direction in game.currentRoom.neighborDirections:
                isValidNeighbor = True
                game.currentRoom = game.currentRoom.neighborDirections[direction]
                enterRoom(game.currentRoom, game)
                return
            else:
                print "You cannot go in that direction."

def goWhere(restOfTheCommand, game):
    words = restOfTheCommand
    if len(words) == 2:
        location = words[-2] + " " + words[-1]
    else:
        location = words[-1]

    isValidNeighbor = False
    enteredNewRoom = False
    
    for i in game.rooms:
        if i == game.currentRoom:
            for j in i.neighbors:
                if (location in game.currentRoom.neighborDirections) and (enteredNewRoom == False):
                    isValidNeighbor = True
                    game.currentRoom = game.currentRoom.neighborDirections[location]
                    enterRoom(game.currentRoom, game)
                    enteredNewRoom = True

                elif j.name == location: #for context 'go room'
                    isValidNeighbor = True
                    game.currentRoom = j
                    enterRoom(j, game)

    if isValidNeighbor == False:
        print "Please choose a valid neighboring room."

def roomWhere(roomName, game):
    for i in game.rooms:
        if i.name == roomName:
            game.currentRoom = i
            enterRoom(i, game)

#acquire an object, putting it into your inventory
def takeItem(item, game):
    if len(item) == 2:
        item = item[-2] + " " + item[-1]
    else:
        item = item[-1]

    isAlreadyInBag = False
    for i in game.bag.items:
        if i == item:
            isAlreadyInBag = True
    if isAlreadyInBag == True:
        print "Your bag already contains that item!"
    else:
        itemFound = False
        for stuff in game.currentRoom.items:
            if item == stuff.name:
                game.bag.items.append(stuff)
                game.currentRoom.items.remove(stuff)
                itemFound = True
                print "Placed", stuff.name, "in bag."
        if itemFound == False:
            print "No", item, "to pick up."            

#drop object in current room, removing it from your inventory
def dropItem(item, game):
    if len(item) == 2:
        item = item[-2] + " " + item[-1]
    else:
        item = item[-1]

    foundInTheBag = False
    for stuff in game.bag.items:
        if stuff.name == item:
            foundInTheBag = True
            if game.currentRoom.itemsAreDroppable == True:
                game.bag.items.remove(stuff)
                game.currentRoom.dropItem(stuff)
                print "Dropped", stuff.name
            else:
                print "Can't drop that here!"
    if not foundInTheBag:
        print "No", item, "in bag."

#list a set of verbs the game understands
def helpUser(game):
	print "following is the list of verbs the game understands:"
	for verb in dispatch:
		print verb

#
def hitItem(item, game):
    if len(item) == 2:
        item = item[-2] + " " + item[-1]
    else:
        item = item[-1]

    itemFound = False
    for stuff in game.currentRoom.items:
        if stuff.name == item:
            itemFound = True
            if "hit" in stuff.availableVerbs:
                print "Hit", stuff.name
            else:
                print "You can't hit that."

    if itemFound == False:
        print "No", item, "to hit."


def eatItem(item, game):
    if len(item) == 2:
        item = item[-2] + " " + item[-1]
    else:
        item = item[-1]

    itemFound = False
    for stuff in game.currentRoom.items:
        if stuff.name == item:
            itemFound = True
            if "eat" in stuff.availableVerbs:
                game.currentRoom.items.remove(stuff)
                print "Ate", stuff.name
            else:
                print "You can't eat that."

    if itemFound == False:
        print "No", item, "to eat."

def openItem(item, game):
    #when player opens a door to access another room
    if item[-1] == "lock":
        openDoor(item, game)
        return
    #when player opens item
    if len(item) == 2:
        item = item[-2] + " " + item[-1]
    else:
        item = item[-1]

    itemFound = False
    for stuff in game.currentRoom.items:
        if stuff.name == item:
            itemFound = True
            if "open" in stuff.availableVerbs:
                #game.currentRoom.items.remove(stuff)
                print "opened", stuff.name
                empty = True
                for item in game.currentRoom.items:
                    if stuff.relatedItems[0] == item.name:
                        empty = False
                if empty:
                    print "nothing inside of", stuff.name
                else:
                    print "found", stuff.relatedItems[0]
            else:
                print "You can't open that."

    if itemFound == False:
        print "No", item, "to open."

#
def openDoor(restOfTheCommand, game):
    #check if player with key
    foundKey = False
    for item in game.bag.items:
        if item.name == "key":
            foundKey = True
    if foundKey:
        print "open door"
    else:
        print "you need key to open it"

#
def checkInventory(game):
    if not game.bag.items:
        print "Bag is empty."
    for stuff in game.bag.items:
        print stuff.name

def startGame(game):
    print "Welcome!"

def resumeGame(game):
    print "Choose a saved game."
    jsonData = json.load(open("savedGames.txt"))
    for i in range(len(jsonData["list"])):
        print i+1,"\b.",jsonData["list"][i]["name"]
    loadNum = input("> ")

    roomName = jsonData["list"][loadNum-1]["room"]
    for i in game.rooms:
        if i.name == roomName:
            game.currentRoom = i
    game.gameName = jsonData["list"][loadNum-1]["name"]

    del game.bag.items[:]
    for i in jsonData["list"][loadNum-1]["bag"]:
        for j in game.stuff:
            if j.name == i:
                game.bag.items.append(j)

    for i in jsonData["list"][loadNum-1]["items"]:
        roomItemNames = []
        for j in jsonData["list"][loadNum-1]["items"][i]:
            roomItemNames.append(j)

        roomItems = []
        for roomItem in roomItemNames:
            for item in game.stuff:
                if item.name == roomItem:
                    roomItems.append(item)

        for room in game.rooms:
            if i == room.name:
                room.items = roomItems

    print "Game successfully loaded."

def saveGame(game):
    roomList = {}
    for room in game.rooms:
        itemList = []
        for item in room.items:
            itemList.append(item.name)
        roomList.update({room.name:itemList})

    itemList = []
    for item in game.bag.items:
        itemList.append(item.name)

    print "Enter a name for the save file."
    saveName = raw_input("> ")
    game.gameName = saveName
    jsonToWrite = {"room":game.currentRoom.name, "bag":itemList, "name":game.gameName, "items":roomList}
    
    with open('savedGames.txt', 'r+') as f:
        data = json.load(f)
        data["list"].append(jsonToWrite)
        f.seek(0)
        json.dump(data, f)
    print "Game successfully saved."

def quitGame(game):
    sys.exit()

#--------------------------------------------------------


dispatch = {"start": startGame, "loadgame": resumeGame, "savegame": saveGame, "quit": quitGame,
			"look": lookItem, "go": goWhere, "take": takeItem, "open": openItem, "drop": dropItem, "help": helpUser,
			"inventory": checkInventory, "north": directionWhere, "south": directionWhere,
            "east": directionWhere, "west": directionWhere, "room": roomWhere, "hit": hitItem, "eat": eatItem }

# helper ------------------------------------------------
def isActionVerb(verb):
	return verb in actionVerb

def isMenuVerb(verb):
	return verb in menuVerb

def isSingleVerb(verb):
	return verb in singleVerb

def isDirectionVerb(verb):
    return verb in directionVerb

def isRoomVerb(verb, game):
    for i in game.currentRoom.neighbors:
        #print ">>", verb, i.name, "<<"
        if verb == i.name:
            return True
    return False

def showItemsInTheRoom(game):
    if len(game.currentRoom.items) == 0:
        print "It seems like an empty room."
    else:
        #print game.currentRoom.items
        print "Here are items in the room:"
        for stuff in game.currentRoom.items:
            found = False
            for hidden in game.currentRoom.hiddenItems:
                if hidden.name == stuff.name:
                    found = True
            if found == False:
                print stuff.name
    print " "

#--------------------------------------------------------

def commandParsing(userInput, game):
	#print "this is the input", userInput
	#required verbs and phrases
    verb = userInput.split()[0].lower()
	#check the verb is in the list
    if isActionVerb(verb) or isMenuVerb(verb) or isSingleVerb(verb) or isDirectionVerb(verb) or isRoomVerb(verb, game) or isRoomVerb(userInput, game):
        if isMenuVerb(verb) or isSingleVerb(verb):
            dispatch[verb](game)
        elif isDirectionVerb(verb):
            dispatch[verb](verb, game)
        elif isRoomVerb(verb, game):
            dispatch["room"](verb, game)
        elif isRoomVerb(userInput, game): #2-word room
            dispatch["room"](userInput, game)
        else:
            restOfTheCommand = userInput.lower().split()[1:]
            #print "debug: rest: ", restOfTheCommand, " verb: ", verb
            dispatch[verb](restOfTheCommand, game)
    else:
        print "use 'help' for instruction"
    return

def main():
    roomFileNames = ["frontYard.json", "porch.json", "foyer.json", "downstairs hallway.json", "living room.json"]
    itemFileNames = ["key.json", "lamp.json", "rock.json", "light switch.json", "bench.json", "picture.json", "rug.json", "porch swing.json", "door lock.json", "mirror.json"]
    listOfRooms = {}
    listOfItems = {}

    roomData = readRoomFiles(roomFileNames, listOfRooms)
    itemData = readRoomFiles(itemFileNames, listOfItems)

    game = Game(roomData, itemData)
    print("                             __                     __                    ")
    print("      .----.-----. .---.-.--|  |.--.--.-----.-----.|  |_.--.--.----.-----.")
    print("      |  __|__ --| |  _  |  _  ||  |  |  -__|     ||   _|  |  |   _|  -__|")
    print("      |____|_____| |___._|_____| \___/|_____|__|__||____|_____|__| |_____|\n")
    print("Enter 'start' for a new game, 'loadgame' to load a previous saved game. or 'quit' to exit")

    gameStarted = False
    while gameStarted == False:
        command = raw_input("> ")
        #command = sys.stdin.readline().rstrip('\n')
        if isMenuVerb(command):
            gameStarted = True
            commandParsing(command, game)
        else:
            print "Please enter a valid choice."

    print game.currentRoom.longDesc
    game.currentRoom.hasBeenVisited = True

    showItemsInTheRoom(game)

    print "Neighboring rooms:"
    for i in game.currentRoom.neighbors:
        print i.name

    while True:
        command = raw_input("> ")
        commandParsing(command, game)

if __name__ == "__main__":
	main()