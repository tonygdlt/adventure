import sys
from Game import Game
import json

actionVerb = ["look", "go", "take", "drop"]
directionVerb = ["north", "south", "east", "west"]
#preposition = ["to", ]
menuVerb = ["start", "loadgame", "savegame"]
singleVerb = ["help", "inventory"]

# verbs method ---------------------------------------

# repeats the long form explanation of the room
def lookItem(restOfTheCommand, game):
	#print restOfTheCommand[0]
    words = restOfTheCommand
	#if preposition provided
    if words and words[0] == "at":
        item = words[1]
        if words[1] in game.currentRoom.items:
            print game.itemDescriptions[words[1]]
        else:
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

def goWhere(restOfTheCommand, game):
	#print restOfTheCommand[0]
    words = restOfTheCommand
	#if preposition provided
	#if words[0] == "to":
		#location = words[0]
	#else:
		#location = words[0]
    location = words[-1]

    isValidNeighbor = False
    for i in game.rooms:
        if i == game.currentRoom:
            for j in i.neighbors:
                if location in game.currentRoom.neighborDirections:
                    isValidNeighbor = True
                    game.currentRoom = game.currentRoom.neighborDirections[location]
                    enterRoom(game.currentRoom, game)

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
    isAlreadyInBag = False
    for i in game.bag.items:
        if i == item[0]:
            isAlreadyInBag = True
    if isAlreadyInBag == True:
        print "Your bag already contains that item!"
    else:
        if item[0] in game.currentRoom.items:
            game.bag.items.append(item[0])
            game.currentRoom.items.remove(item[0])
            print "Placed", item[0], "in bag."
        else:
            print "No", item[0], "to pick up."

#drop object in current room, removing it from your inventory
def dropItem(item, game):
    if item[0] in game.bag.items:
        if game.currentRoom.itemsAreDroppable == True:
            game.bag.items.remove(item[0])
            game.currentRoom.dropItem(item[0])
            print "Dropped", item[0]
        else:
            print "Can't drop that here!"
    else:
        print "No", item[0], "in bag."

#list a set of verbs the game understands
def helpUser(game):
	print "following is the list of verbs the game understands:"
	for verb in dispatch:
		print verb
#
def checkInventory(game):
    if not game.bag.items:
        print "Bag is empty."
    for i in game.bag.items:
        print i

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
    for i in jsonData["list"][loadNum-1]["bag"]:
        game.bag.items.append(i)

    roomCnt = 0
    for i in jsonData["list"][loadNum-1]["items"]:
        game.rooms[roomCnt].items = i
        roomCnt = roomCnt+1

    print "Game successfully loaded."

def saveGame(game):
    roomItemsGen = (i.items for i in game.rooms)
    roomItems = []
    for i in roomItemsGen:
        roomItems.append(i)

    print "Enter a name for the save file."
    saveName = raw_input("> ")
    game.gameName = saveName
    jsonToWrite = {"room":game.currentRoom.name, "bag":game.bag.items, "name":game.gameName, "items":roomItems}

    with open('savedGames.txt', 'r+') as f:
        data = json.load(f)
        data["list"].append(jsonToWrite)
        f.seek(0)
        json.dump(data, f)
    print "Game successfully saved."

#--------------------------------------------------------


dispatch = {"start": startGame, "loadgame": resumeGame, "savegame": saveGame, 
			"look": lookItem, "go": goWhere, "take": takeItem, "drop": dropItem, "help": helpUser,
			"inventory": checkInventory, "north": directionWhere, "south": directionWhere,
            "east": directionWhere, "west": directionWhere, "room": roomWhere}

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
        if verb == i.name:
            return True
    return False
#--------------------------------------------------------

def commandParsing(userInput, game):
	#print "this is the input", userInput
	#required verbs and phrases
    verb = userInput.split()[0].lower()
	#check the verb is in the list
    if isActionVerb(verb) or isMenuVerb(verb) or isSingleVerb(verb) or isDirectionVerb(verb) or isRoomVerb(verb, game):
        if isMenuVerb(verb) or isSingleVerb(verb):
            dispatch[verb](game)
        elif isDirectionVerb(verb):
            dispatch[verb](verb, game)
        elif isRoomVerb(verb, game):
            dispatch["room"](verb, game)
        else:
            isRoomVerb(verb, game)
            restOfTheCommand = userInput.lower().split()[1:]
            dispatch[verb](restOfTheCommand, game)
    else:
        print "use 'help' for instruction"
    return

def main():
    game = Game()
    print("                             __                     __                    ")
    print("      .----.-----. .---.-.--|  |.--.--.-----.-----.|  |_.--.--.----.-----.")
    print("      |  __|__ --| |  _  |  _  ||  |  |  -__|     ||   _|  |  |   _|  -__|")
    print("      |____|_____| |___._|_____| \___/|_____|__|__||____|_____|__| |_____|\n")
    print("Enter 'start' for a new game, 'loadgame' to load a previous saved game. or 'quit' to exit")

    gameStarted = False
    while gameStarted == False:
        command = raw_input("> ")
        if isMenuVerb(command):
            gameStarted = True
            commandParsing(command, game)
        else:
            print "Please enter a valid choice."

    print game.r1.longDesc
    game.r1.hasBeenVisited = True

    print "Neighboring rooms:"
    for i in game.r1.neighbors:
        print i.name

    while True:
        command = raw_input("> ")
        commandParsing(command, game)

if __name__ == "__main__":
	main()