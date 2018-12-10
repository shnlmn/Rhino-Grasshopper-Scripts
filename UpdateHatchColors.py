#------------------------------------------------------
# Name:        Update HatchFiles
# Purpose:     Change layer colors based on layer name
# Author:      Shane Leaman
#------------------------------------------------------

"""
For use with the Feasibility Study Workflow. 
See "F:\Resource\Strategic Initiatives\0702013.20 Research Initiative\Rhino Workflow"

This script also requires getLayerList.py to be in the same folder, as well as
colors.csv.

Using an excel file named ColorStandard.xlsm, you can create a color palette for 
the hatches. The excel file will export the 'colors.csv' file.

"""


import rhinoscriptsyntax as rs
import os
import re
from getLayerList import getLayers

def ToList(str):
    return list(map(lambda x: int(x), str[1:-1].split(",")))
def cleanLayerList(layers):
    return list(filter(lambda x: not rs.IsLayerReference(x), layers))
    

file_name = os.path.dirname(os.path.realpath(__file__))+("\colors.csv")
file = open(file_name, 'r')
lines = file.readlines()
file.close()

del lines[0]

layerDict = {}

for line in lines:
    line = line.strip()
    line_data = line.split("|")
    prefix = "A-HATCH-"
    if line_data[0] not in ["BOH", "PARKING", "AMENITY"]:
        layerDict[prefix+line_data[0]] = {"LayerColor" : line_data[2],
                                              "LayerPrintColor" : line_data[2]}
        if line_data[0] == "RESIDENTIAL":
            line_data[0] = "RES"
            
        layerDict[prefix+line_data[0]+"_LOBBY"] = {"LayerColor" : line_data[1],
                                              "LayerPrintColor" : line_data[1]}
        layerDict[prefix+line_data[0]+"_BOH"] = {"LayerColor" : line_data[3],
                                              "LayerPrintColor" : line_data[3]}
    else:
        layerDict[prefix+line_data[0]] = {"LayerColor" : line_data[1],
                                          "LayerPrintColor" : line_data[1]}
                                          
rs.EnableRedraw(False)

layers = cleanLayerList(rs.LayerNames())

#
#print(layers)
#print(layerDict)

for layer in layers:
    for key, val  in layerDict.items():
        if layer+"::"+key in rs.LayerChildren(layer):
            
            rs.LayerColor(layer+"::"+key, rs.coercecolor(ToList(val["LayerColor"])))
            rs.LayerPrintColor(layer+"::"+key, rs.coercecolor(ToList(val["LayerPrintColor"])))



rs.EnableRedraw(True)
