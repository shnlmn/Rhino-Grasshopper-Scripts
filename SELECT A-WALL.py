"""
For use with the Feasibility Study Workflow. 
See "F:\Resource\Strategic Initiatives\0702013.20 Research Initiative\Rhino Workflow"

This script selects all curves on layers with names defined in 'wallLayers' variable 
below to create boundary hatches.
"""

######### List of layers you want included in wall selection. ######### 
wallLayers = ["A-WALL", "A-AREA-BOUNDARY", "A-WALL-INTR", "I-WALL"]
######### 

import rhinoscriptsyntax as rs
import re

def main():
    rs.EnableRedraw(enable=False)
    
    walls = []
    parentFolder = rs.CurrentLayer()
    if re.search("::", parentFolder):
        parentFolder = parentFolder.rsplit("::", 1)[0]
    walls = []
    for wallLayer in wallLayers:
        try:
            walls.extend(rs.ObjectsByLayer(parentFolder + "::" + wallLayer))
        except ValueError:
            print("No curves on layer "+parentFolder + "::" + wallLayer)
            pass

    if not walls:
        print("No walls on this floor.")
        return None
    
    curves = []
    
    for wall in walls:
        if rs.IsCurve(wall):
            curves.append(wall)
    rs.SelectObjects(curves)
    
    rs.EnableRedraw(enable=True)
    
    
if __name__=="__main__":
    main()