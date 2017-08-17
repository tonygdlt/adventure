'''
Created on Jul 15, 2017

@author: Penny
'''
import ReadDataFiles
from Room import Room
from Stuff import Stuff
from Feature import Feature

roomNames = ["frontYard", "foyer", "porch", "livingRoom"]
itemNames = ["frontDoorKey", "lamp", "key2", "stick"]
featureNames = []

roomObjects = {}
stuffObjects = {}
featureObjects = {}

#This function uses data read in by ReadDataFiles to create a dict containing Room objects
def createRooms():
    roomList = ReadDataFiles.readRoomFile()
    
    for i in roomNames:
        roomObjects[i] = roomObj(roomList[i])
    return roomObjects

def roomObj(roomIn):
    newRoom = Room(roomIn["name"], roomIn["items"], True)
    newRoom.setLongDescription(roomIn["longDescription"])
    newRoom.setShortDescription(roomIn["shortDescription"])
    newRoom.setNeighbors(roomIn["neighbors"])
    return newRoom

#This function uses data read in by ReadDataFiles to create a dict containing Stuff objects
def createStuff():
    stuffList = ReadDataFiles.readItemFile()
    
    for i in itemNames:
        stuffObjects[i] = stuffObj(stuffList[i])
    return stuffObjects

def stuffObj(stuffIn):
    newStuff = Stuff(stuffIn["name"],stuffIn["description"],stuffIn["availableVerbs"])
    return newStuff

#This function uses data read in by ReadDataFiles to create a dict containing Feature objects
def createFeatures():
    featureList = ReadDataFiles.readFeatureList()
    
    for i in featureNames:
        featureObjects[i] = featureObj(featureList[i])
    return featureObjects

def featureObj(featureIn):
    newFeature = Feature(featureIn["itemName"],featureIn["description"],featureIn["availableVerbs"])
    return newFeature
