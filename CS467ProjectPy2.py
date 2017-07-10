import sys
from Game import Game
import json

def loadGame(game):
	jsonData = json.load(open("savedGames.txt"))
	print "\n"
	for i in range(len(jsonData["list"])):
		print i+1,"\b.",jsonData["list"][i]["name"]
	loadNum = input("> ")
	game.currentRoom = jsonData["list"][loadNum-1]["room"]
	game.gameName = jsonData["list"][loadNum-1]["name"]
	for i in jsonData["list"][loadNum-1]["bag"]:
		game.bag.items.append(i)
	return game

def startNewGame(game):
    print("\nWelcome.")
    print("Enter a name for the save file.")
    saveName = raw_input("> ")
    game.gameName = saveName
    jsonToWrite = {"room":game.currentRoom, "bag":game.bag.items, "name":game.gameName}

    with open('savedGames.txt', 'r+') as f:
        data = json.load(f)
        data["list"].append(jsonToWrite)
        f.seek(0)
        json.dump(data, f)


def main():

	game = Game()

	print("                             __                     __                    ")
	print("      .----.-----. .---.-.--|  |.--.--.-----.-----.|  |_.--.--.----.-----.")
	print("      |  __|__ --| |  _  |  _  ||  |  |  -__|     ||   _|  |  |   _|  -__|")
	print("      |____|_____| |___._|_____| \___/|_____|__|__||____|_____|__| |_____|\n")
	print("Select an option.")
	print("1. Start new game")
	print("2. Load saved game")
	print("3. Quit\n")

	choice = raw_input("> ")
	if (choice == "1"):
		startNewGame(game)

	elif (choice == "2"):
		game = loadGame(game)

	elif (choice == "3"):
		print("quit")

	else:
		print("Please enter a valid choice.")


if __name__ == "__main__":
	main()