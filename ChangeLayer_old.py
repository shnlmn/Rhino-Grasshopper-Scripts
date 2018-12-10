import rhinoscriptsyntax as rs
import re
import scriptcontext as sc
import Rhino

def main():
    rs.EnableRedraw(enable=False)
    
    notes = sc.doc.Notes
    if notes:
        variables = notes.split("\r")
        vardict = {}
        for variable in variables:
            var = variable.split("=")
            var = list([x.strip() for x in var])
            vardict[var[0]] = var[1]

    allLayers = rs.LayerNames()
    topList = []
    for layer in allLayers:
        if rs.LayerChildCount(layer) > 0:
            if re.search("::", layer):
                layer = layer.split("::")[0]
            if re.search("^L\d",layer) or re.search("^R\d",layer) or re.search("^M\d",layer) or re.search("^P\d",layer) or re.search("^SECTION ", layer) or re.search("^ROOFPLAN", layer) or re.search("^SOLIDS", layer):
                topList.append(layer)
    topList = sorted(list(set(topList)))
    thisLayer = rs.CurrentLayer()
    
    topList.append("TURN ALL ON")
    destinationLayer = rs.ListBox(topList, "Layer To Activate")
    
    
    
    if not destinationLayer:
        print("No Layer Selected")
        return None
    elif destinationLayer == "TURN ALL ON":
        topList.remove(destinationLayer)
        for layer in topList:
            sc.doc = Rhino.RhinoDoc.ActiveDoc
            rs.LayerVisible(layer, True)
            rs.ExpandLayer(layer, False)
    else:
        topList.remove("TURN ALL ON")
        topList.remove(destinationLayer)
        rs.CurrentLayer(layer = destinationLayer)
        rs.ExpandLayer(destinationLayer, True)
        for layer in topList:
            sc.doc = Rhino.RhinoDoc.ActiveDoc
            rs.LayerVisible(layer, False)
            rs.ExpandLayer(layer, False)
    print(destinationLayer)
    rs.EnableRedraw(enable=True)

if __name__=="__main__":
    main()