from Bag import Bag
from Room import Room

class Game(object):
    def __init__(self):
        self.bag = Bag()
        self.r1 = Room("room1", [], True)
        self.r2 = Room("room2", ["lamp"], True)
        self.r3 = Room("room3", ["key1"], True)
        self.r4 = Room("room4", ["stick", "key2"], True)
        self.r5 = Room("room5", [], True)

        self.r1.setNeighbors([self.r2, self.r4, self.r5])
        self.r1.neighborDirections = {"north": self.r2, "south": self.r4, "east": self.r5}
        self.r2.setNeighbors([self.r1])
        self.r2.neighborDirections = {"south": self.r1}
        self.r3.setNeighbors([self.r4, self.r5])
        self.r3.neighborDirections = {"west": self.r4, "north": self.r5}
        self.r4.setNeighbors([self.r1, self.r3])
        self.r4.neighborDirections = {"north": self.r1, "east": self.r3}
        self.r5.setNeighbors([self.r1, self.r3])
        self.r5.neighborDirections = {"west": self.r1, "south": self.r3}

        self.r1.setLongDescription("This is the long description for room1")
        self.r2.setLongDescription("This is the long description for room2")
        self.r3.setLongDescription("This is the long description for room3")
        self.r4.setLongDescription("This is the long description for room4")
        self.r5.setLongDescription("This is the long description for room5")

        self.r1.setShortDescription("This is the short description for room1")
        self.r2.setShortDescription("This is the short description for room2")
        self.r3.setShortDescription("This is the short description for room3")
        self.r4.setShortDescription("This is the short description for room4")
        self.r5.setShortDescription("This is the short description for room5")

        self.itemDescriptions = {"lamp": "A dusty lamp that seems to have something inside", "key1": "A long wooden key", "key2": "A small metal key", "stick": "A warbly walking stick"}

        self.rooms = [self.r1, self.r2, self.r3, self.r4, self.r5]
        self.currentRoom = self.r1

    gameName = "nameMe"