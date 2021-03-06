class Room(object):
    def __init__(self, name, items, itemsAreDroppable, hiddenItems):
        self.name = name
        self.hasBeenVisited = False
        self.items = items
        self.itemsAreDroppable = itemsAreDroppable
        self.hiddenItems = hiddenItems
    def setNeighbors(self, neighborArr):
        self.neighbors = neighborArr
    def setLongDescription(self, desc):
        self.longDesc = desc
    def setShortDescription(self, desc):
        self.shortDesc = desc
    def dropItem(self, item):
        self.items.append(item)