import rhinoscriptsyntax as rs
import re

allLayers = rs.LayerNames()

for layer in allLayers:
    
    if re.search("A-WALL",layer):
        print(layer)
        objects = rs.ObjectsByLayer(layer, True)
        rs.SelectObjects(objects)
        rs.Command("_BringToFront", True)
        