import rhinoscriptsyntax as rs
import re
    
copy = rs.GetBoolean("Do you want to copy this layer?", ("Copy", "No", "Yes"), True)

def duplicateLayer(name, source, destination):
    newLayer = rs.AddLayer(name, color=rs.LayerColor(source), parent = destination)
    rs.ParentLayer(newLayer, destination)
#    print(name, source, destination)
    matchLayer(newLayer, source)
    return(newLayer)

def matchLayer(name, source):
    rs.LayerLinetype(name, linetype = rs.LayerLinetype(source))
    rs.LayerPrintColor(name, color = rs.LayerPrintColor(source))
    rs.LayerPrintWidth(name, width = rs.LayerPrintWidth(source))


sourceObjects = rs.GetObjects(message="Select Object to Move", preselect=True, select=False)

allLayers = rs.LayerNames()
topList = []
for layer in allLayers:
    if re.search("::", layer):
            layer = layer.split("::")[0]
    if rs.LayerChildCount(layer) > 0:
        topList.append(layer)

topList = sorted(list(set(topList)))
topList = [(x, False) for x in topList]
destinationLayer = rs.CheckListBox(topList)
rs.EnableRedraw(enable=False)
for obj in sourceObjects:
    objLayer = rs.ObjectLayer(obj)
    
    parent, child = objLayer.split("::")[-2:]

        
    for dLayer in destinationLayer:
        if dLayer[1] == True:
            fullDLayer = dLayer[0] + "::" + child
            if not rs.IsLayer(fullDLayer):
                print(dLayer[0]+"::"+child, objLayer)
                fullDLayer = duplicateLayer(child, objLayer, dLayer[0])   
            if copy[0] == True:
                copyObj = rs.CopyObject(obj, translation=None)
                rs.ObjectLayer(copyObj, layer=fullDLayer)
            else:
                rs.ObjectLayer(obj, layer=fullDLayer)
                
rs.EnableRedraw(enable=True)