class Room(object):
    def __init__(self, name, key, anotherItem, thirdItem):
        self.name = name
        self.hasBeenVisited = False
        self.key = key
        self.anotherItem = anotherItem
        self.thirdItem = thirdItem
    def setNeighbors(self, neighborArr):
        self.neighbors = neighborArr
    def setLongDescription(self, desc):
        self.longDesc = desc
    def setShortDescription(self, desc):
        self.shortDesc = desc