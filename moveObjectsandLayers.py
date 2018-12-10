import rhinoscriptsyntax as rs

moveObjects = rs.GetObjects(message="Select Objects to Move", preselect=True, select=False)
parentLayer = rs.GetLayer(title="Select Layer to move Objects to", show_new_button=True)
sourceLayer = []


rs.EnableRedraw(enable=False)

for obj in moveObjects: 
    refLayer = rs.ObjectLayer(obj)
    if refLayer not in sourceLayer:
        sourceLayer.append(refLayer)
        rs.AddLayer(name=refLayer, color=rs.LayerColor(refLayer), parent=parentLayer)
    for source in sourceLayer:
        print(source)
        if refLayer == source:
            dup = rs.CopyObject(obj)
            rs.ObjectLayer(dup, layer=parentLayer+"::"+source)
            
            
rs.EnableRedraw(enable=True)