import json
from Bag import Bag
from Room import Room
from Stuff import Stuff

class Game(object):
    """description of class"""
    def __init__(self, roomData, itemData):
        self.bag = Bag()
        self.stuff = list()
        self.roomNames = []
        self.rooms = list()

        for item in itemData:
            self.stuff.append(Stuff(itemData[item]["name"], itemData[item]["description"], itemData[item]["availableVerbs"]))

        for idx, room in enumerate(roomData):
            self.roomNames.append(roomData[room]["roomName"])

            self.roomItems = []
            for roomItem in roomData[room]["item"]:
                for item in self.stuff:
                    if item.name == roomItem:
                        self.roomItems.append(item)

            self.rooms.append(Room(roomData[room]["roomName"], self.roomItems, True))
            if self.roomNames[idx] == "front yard":
                self.initialRoom = self.rooms[idx]

        for idx, room in enumerate(roomData):
            neighbors = []
            neighborDirections = {}

            if roomData[room]["north"] in self.roomNames:
                for neighbor in enumerate(self.rooms):
                    if neighbor[1].name == roomData[room]["north"]:
                        neighbors.append(neighbor[1])
                        neighborDirections.update({"north":neighbor[1]})
            if roomData[room]["south"] in self.roomNames:
                for neighbor in enumerate(self.rooms):
                    if neighbor[1].name == roomData[room]["south"]:
                        neighbors.append(neighbor[1])
                        neighborDirections.update({"south":neighbor[1]})
            if roomData[room]["east"] in self.roomNames:
                for neighbor in enumerate(self.rooms):
                    if neighbor[1].name == roomData[room]["east"]:
                        neighbors.append(neighbor[1])
                        neighborDirections.update({"east":neighbor[1]})
                for neighbor in enumerate(self.rooms):
                    if neighbor[1].name == roomData[room]["west"]:
                        neighbors.append(neighbor[1])
                        neighborDirections.update({"west":neighbor[1]})

            self.rooms[idx].setNeighbors(neighbors)
            self.rooms[idx].neighborDirections = neighborDirections

            self.rooms[idx].setLongDescription(roomData[room]["longDescription"])
            self.rooms[idx].setShortDescription(roomData[room]["shortDescription"])
        self.currentRoom = self.initialRoom

    gameName = "nameMe"