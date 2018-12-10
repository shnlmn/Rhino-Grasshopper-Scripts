import rhinoscriptsyntax as rs
import re
import scriptcontext
import Rhino


allLayers = rs.LayerNames()
printList = []
for layer in allLayers:
    if rs.LayerChildCount(layer) > 0:
        if re.search("^L\d",layer) or re.search("^P\d",layer):
            printList.append(layer)

topList = []
for layer in printList:
    hidelayers = []
    topList = list(printList)
    topList.remove(layer)
    for hidelayer in topList:
        scriptcontext.doc = Rhino.RhinoDoc.ActiveDoc
        rs.LayerVisible(hidelayer, False)
        rs.ExpandLayer(hidelayer, False)
    rs.LayerVisible(layer, True)
    rs.MessageBox("Layer"+layer)