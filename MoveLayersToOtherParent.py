import rhinoscriptsyntax as rs
    
copy = rs.GetBoolean("Do you want to copy this layer?", ("Copy", "No", "Yes"), True)
print(copy)
def duplicateLayer(name, source, destination):
    newLayer = rs.AddLayer(name, color=rs.LayerColor(source), parent = destination)
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
    if rs.LayerChildCount(layer) > 0:
        topList.append(layer)

destinationLayer = rs.ListBox(topList)

rs.EnableRedraw(enable=False)

for obj in sourceObjects:
    objLayer = rs.ObjectLayer(obj)
    parent, child = objLayer.split("::")
    fullDLayer = destinationLayer + "::" + child
    if not rs.IsLayer(fullDLayer):
        fullDLayer = duplicateLayer(child, objLayer, destinationLayer)    
    if copy[0] == True:
        copyObj = rs.CopyObject(obj, translation=None)
        rs.ObjectLayer(copyObj, layer=fullDLayer)
    else:
         rs.ObjectLayer(obj, layer=fullDLayer)


rs.EnableRedraw(enable=True)