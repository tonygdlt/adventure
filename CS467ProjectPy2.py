import sys
from Game import Game
import json

actionVerb = ["look", "go", "take"]
#preposition = ["to", ]
menuVerb = ["start", "loadgame", "savegame"]
singleVerb = ["help", "inventory"]

# verbs method ---------------------------------------

# repeats the long form explanation of the room
def lookItem(restOfTheCommand, game):
	#print restOfTheCommand[0]
	words = restOfTheCommand
	#if preposition provided
	if words[0] == "at":
		item = words[1]
	else:
		item = words[0]
	print "look", item

def goWhere(restOfTheCommand, game):
	#print restOfTheCommand[0]
	words = restOfTheCommand
	#if preposition provided
	#if words[0] == "to":
		#item = words[0]
	#else:
		#item = words[0]
	item = words[-1]
	print "go", item

#acquire an object, putting it into your inventory
def takeItem(item, game):
	print "take", item

#list a set of verbs the game understands
def helpUser(game):
	print "following is the list of verbs the game understands:"
	for verb in dispatch:
		print verb
#
def checkInventory(game):
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
    game.currentRoom = jsonData["list"][loadNum-1]["room"]
    game.gameName = jsonData["list"][loadNum-1]["name"]
    for i in jsonData["list"][loadNum-1]["bag"]:
        game.bag.items.append(i)
    print "Game successfully loaded."

def saveGame(game):
    print "Enter a name for the save file."
    saveName = raw_input("> ")
    game.gameName = saveName
    jsonToWrite = {"room":game.currentRoom, "bag":game.bag.items, "name":game.gameName}

    with open('savedGames.txt', 'r+') as f:
        data = json.load(f)
        data["list"].append(jsonToWrite)
        f.seek(0)
        json.dump(data, f)
    print "Game successfully saved."

#--------------------------------------------------------


dispatch = {"start": startGame, "loadgame": resumeGame, "savegame": saveGame, 
			"look": lookItem, "go": goWhere, "take": takeItem, "help": helpUser,
			"inventory": checkInventory}

# helper ------------------------------------------------
def isActionVerb(verb):
	return verb in actionVerb

def isMenuVerb(verb):
	return verb in menuVerb

def isSingleVerb(verb):
	return verb in singleVerb
#--------------------------------------------------------

def commandParsing(userInput, game):
	#print "this is the input", userInput
	#required verbs and phrases
	verb = userInput.split()[0].lower()
	#check the verb is in the list
	if isActionVerb(verb) or isMenuVerb(verb) or isSingleVerb(verb):
		if isMenuVerb(verb) or isSingleVerb(verb):
			dispatch[verb](game)
		else:
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
    while True:
        command = raw_input("> ")
        commandParsing(command, game)

if __name__ == "__main__":
	main()