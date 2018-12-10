import rhinoscriptsyntax as rs
import Rhino
import os
import re
import getLayerList


includeList = None
excludeList = [".3dm", "Make2D"]
    
    
def getNotes():
    layers = getLayerList.getLayers(includeList, excludeList)
    layerList = []
    for layer in layers:
        layerList.extend(rs.LayerChildren(layer))
    noteObjs = []
    print(layers)
    #noteLayers = [x if re.search('A-ANN0-NOTE', x.split("::")[-1]) else None for x in layers]
    for layer in layerList:
        if re.search("A-ANNO-NOTE", layer.split("::")[-1]):
            noteObjs.extend(rs.ObjectsByLayer(layer))
    return(noteObjs)



# AUTOSELECT OBJECTS
noteObjs = getNotes()
print(noteObjs, "NOTES")
groupSet = []
# filter out objects not in groups
for noteObj in noteObjs:
    if rs.ObjectGroups(noteObj):
        groupSet.append(noteObj)

groupSet = list(set([rs.ObjectGroups(x)[0] for x in groupSet]))
###
print(groupSet)
filename = rs.SaveFileName("Save CSV File", "*.csv", None,  "areaExport", "csv")

file = open(filename, 'w')

headerline = "Area Name, Area in SF\n"
file.write(headerline)

returnList = []

for groupObj in groupSet:
    objs = rs.ObjectsByGroup(groupObj)
    for obj in objs:
        print(rs.TextObjectText(obj))
        if rs.ObjectName(obj) == "Area Text":
            areaText = rs.TextObjectText(obj)
        elif rs.ObjectName(obj) == "Name Text":
            nameText = rs.TextObjectText(obj)
        objLayer = rs.ObjectLayer(obj)
    parentLayer = rs.ParentLayer(objLayer)
    if not parentLayer:
        parentLayer = "ROOT"
    else:
        parentLayer = parentLayer.split("::")[-1]
        
    returnList.append([parentLayer, nameText.replace('\r', '').replace('\n', ' '), areaText])
    
returnList = sorted(returnList, key=lambda x: x[0])
for item in returnList:
    line = "{}, {}, {} \n".format(item[0], item[1], float((item[2].split(" ")[0]).replace(",","")))
    file.write(line)

file.close()