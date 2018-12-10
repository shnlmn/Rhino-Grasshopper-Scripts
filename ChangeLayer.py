#------------------------------------------------------
# Name:        ChangeLayer
# Purpose:     Change Layer Visibility for layers matching "L/d"
# Author:      Shane Leaman
# Created:     08/31/2017
#------------------------------------------------------

import rhinoscriptsyntax as rs
import re
import scriptcontext as sc
import Rhino
import getLayerList

def main():
    rs.EnableRedraw(enable=False)

    topList = []
    topList = sorted(getLayerList.getLayers(exclude=[".3dm", "Make2D"]))
    print(topList)
    thisLayer = rs.CurrentLayer()
    
    topList.append("TURN ALL ON")
    destinationLayer = rs.ListBox(topList, "Layer To Activate")
    
    
    
    if not destinationLayer:
        print("No Layer Selected")
        return None
        
    elif destinationLayer == "TURN ALL ON":
        topList.remove(destinationLayer)
        for layer in topList:
            rs.LayerVisible(layer, True)
#            rs.ExpandLayer(layer, False)
            
    else:
        topList.remove("TURN ALL ON")
        topList.remove(destinationLayer)
        rs.CurrentLayer(layer = destinationLayer)
        rs.ExpandLayer(destinationLayer, True)
        for layer in topList:
            rs.LayerVisible(layer, False)
#            rs.ExpandLayer(layer, False)
            
    print(destinationLayer)
    rs.EnableRedraw(enable=True)

if __name__=="__main__":
    main()