import rhinoscriptsyntax as rs
import re
from System.Drawing import Color
import Rhino
layerDict = {}
layerNames = list(filter(lambda x: not rs.IsLayerReference(x), rs.LayerNames()))
print(layerNames)
rs.EnableRedraw(enable=False)


layerDict["A-WALL"] = {"LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.6}
layerDict["A-BLDG-SHAFT"] = {"LayerLinetype" : "dashed", "LayerPrintWidth" : 0.3cl }
layerDict["S-COL"] = {"LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.3}
layerDict["S-COLS"] = layerDict["S-COL"]
layerDict["A-WALL-INTR"] = {"LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.3}
layerDict["I-WALL"] = layerDict["A-WALL-INTR"]
layerDict["A-GLAZ"] = {"LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.6}
layerDict["A-HATCH-STORAGE"] = {"LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.3}
layerDict["A-BLDG-OTLN-ABOV"] = {"LayerLinetype" : "HIDDEN2", "LayerPrintWidth" : 0.3}
layerDict["A-BLDG-OTLN-BLOW"] = {"LayerLinetype" : "Dashed", "LayerPrintWidth" : 0.3}
layerDict["A-FLOR"] = {"LayerLinetype" : "Continuous2", "LayerPrintWidth" : 0.3}
layerDict["A-ANNO-NOTE"] = {"LayerLinetype" : "Continuous2", "LayerPrintWidth" : 0.1}

print(layerNames)


for layer in layerNames:
    for entry in layerDict:
        if re.search(entry+"$", layer):
            rs.LayerLinetype(layer, layerDict[entry]['LayerLinetype'])
            rs.LayerPrintWidth(layer, layerDict[entry]['LayerPrintWidth'])
            
rs.EnableRedraw(enable=True)
