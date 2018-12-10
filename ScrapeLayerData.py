import rhinoscriptsyntax as rs
import re
from System.Drawing import Color

layernames = rs.LayerNames()
for layer in layernames:
    if re.search("L01::", layer):
        layername = layer.split("::")[2]
        print(
            'layerDict["'+layername+'"] = {'+
            '"LayerColor" : '+ str(Color.ToArgb(rs.LayerColor(layer))) +
            ', "LayerPrintColor" : '+ str(Color.ToArgb(rs.LayerPrintColor(layer))) +
            ', "LayerLinetype" : "'+ str(rs.LayerLinetype(layer)) +
            '", "LayerPrintWidth" : '+ str(rs.LayerPrintWidth(layer)) +
            '}')