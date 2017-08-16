'''
Created on Jul 8, 2017

@author: Penny
'''
import os
import sys
import json


roomList = {}
itemList = {}
featureList ={}
filePath = ("rooms")

#loops through the roomFileNames list, and adds each object to a dictionary
#return a dictionary with all the rooms, and their attributes
def readRoomFile():
    roomDir = os.listdir(filePath)
    for name in roomDir:
        #to avoid reading hidden file, such as .DS_Store on mac
        if name.endswith(".json"):
            with open(os.path.join(filePath, name)) as n:
                roomList.update(json.load(n))
    return roomList

#adds each of the objects in the itemFile to a dictionary
#return a dictionary with all the items, and their attributes
def readItemFile():
    with open("itemFile.json", 'r') as n:
        itemList.update(json.load(n))
    return itemList

#adds each of the objects in the featureFile to a dictionary
#return a dictionary with all the features, and their attributes
def readFeatureList():
    with open("featureFile.json", 'r') as n:
        featureList.update(json.load(n))
    return featureList
