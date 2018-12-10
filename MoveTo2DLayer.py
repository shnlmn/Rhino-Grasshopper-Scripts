#------------------------------------------------------
# Name:        MoveTo2DLayer  
# Purpose:     Move Make2D objects to the 2D layer Structure
# Author:      Shane Leaman
# Created:     08/31/2017
#------------------------------------------------------

import rhinoscriptsyntax as rs
import getLayerList
import re
import scriptcontext as sc


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
    
    
def main():
    
    sourceObjects = rs.GetObjects(message="Select Objects to Move to Other Layers.", preselect = True, select = True)
    
    copy = rs.GetBoolean("Do you want to copy this layer?", ("Copy", "No", "Yes"), False)
    includeList = None
    excludeList = [".3dm", "Make2D"]
    targetLayers = sorted(getLayerList.getLayers(includeList, excludeList))
    targetLayers = [(x, False) for x in targetLayers]
    
    destinationLayer = rs.CheckListBox(targetLayers)
    
    if not destinationLayer:
        return False
    
    rs.EnableRedraw(enable=False)
    
    sourceObjects = list(filter(lambda x: not rs.IsLayerReference(rs.ObjectLayer(x)), sourceObjects))
    
    
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
    
    
if __name__ == "__main__":
    print(main())