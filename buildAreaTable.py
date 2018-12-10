import rhinoscriptsyntax as rs
import os
import re
        
def getParent(object):
    """ Get the parent layer of an object """    
    return(rs.ObjectLayer(object).split("::")[0])
    
def getLayerType(object):
    """ Will get the type of hatch based on the layer structure "LAYER::A-HATCH-TYPE" """
    if getParent(object) in parentLayers and rs.ObjectLayer(object) in hatchLayers:
        return(rs.ObjectLayer(object).split("-")[2])

areasTable = {}
hatchnames = set([])
layers = rs.LayerNames()
levelLayers = [x for x in layers if re.match("^L\d+|^P\d+|^M\d+", x)]
parentLayers = [x for x in levelLayers if "::" not in x]
hatchLayers = [x for x in levelLayers if "HATCH" in x]
requestType = rs.GetBoolean("Choose output data", ("Output", "Gross_Area", "Unit_Areas"), False)
requestType = requestType[0]
#Gather all the different hatch types for area analysis
for layer in levelLayers:
    hlayers = [x.split("::")[1] for x in rs.LayerChildren(layer) if "HATCH" in x]
    if len(hlayers)>0:
        sublay = ([x.split("-")[2] for x in hlayers])
        hatchnames = hatchnames.union(sublay)
        

# sort the level keys
L1 = False
M1 = False
outputLevels = []
inputLevels = list(parentLayers)
if "L1" in inputLevels:
    L1 = True
    inputLevels.remove("L1")
if "M1" in inputLevels:
    M1 = True
    inputLevels.remove("M1")
P_Levels = []
L_Levels = []
for level in inputLevels:
    if re.search('^P', level):
        P_Levels.append(level)
    elif re.search('^L', level):
        L_Levels.append(level)
outputLevels.extend(list(reversed(sorted(P_Levels))))
outputLevels.extend(["L1"])
if M1 == True:
    outputLevels.extend(["M1"]) 
outputLevels.extend(sorted(L_Levels))

# Build Area Table for population
for level in outputLevels:
    if requestType == False:
        areasTable[level] = {x: [0] for x in list(hatchnames)}
    else:
        areasTable[level] = {x: [] for x in list(hatchnames)}

        
#get all the hatches in the document
allHatch = rs.ObjectsByType(65536)

for hatch in allHatch:
    if getLayerType(hatch):
        if requestType == False:
            areasTable[getParent(hatch)][getLayerType(hatch)][0] += rs.Area(hatch)
        else:
            if getLayerType(hatch) == "RESIDENTIAL":
                areasTable[getParent(hatch)][getLayerType(hatch)].append(rs.Area(hatch))

if requestType == True: hatchnames = ["RESIDENTIAL"]
outputList = "Level, " + ",".join(hatchnames)+"\n\n"

for lev in reversed(outputLevels):
    max_list = 0
    for hlev in hatchnames:
        if len(areasTable[lev][hlev]) > max_list: max_list = len(areasTable[lev][hlev])
    for row in range(max_list):
        outputList += lev+","
        for hname in hatchnames:
            areasTable[lev][hname] = sorted(areasTable[lev][hname])
            try:
                outputList += str(areasTable[lev][hname][row]) + ","
            except:
                outputList += "0,"
        outputList = outputList[:-1] + '\n'
    if requestType == True: outputList += '\n'
print(outputList)
##open file
csv_path = rs.OpenFileName()
csv_write = open(csv_path, "w")
csv_write.write(outputList)
csv_write.close()


#for key in areasTable:
#    print(key)