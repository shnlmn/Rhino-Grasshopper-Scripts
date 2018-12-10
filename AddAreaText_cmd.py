"""
AddAreaText
For use with the Feasibility Study Workflow. 
See "F:\Resource\Strategic Initiatives\0702013.20 Research Initiative\Rhino Workflow"

This script will take a hatch and attempt to place an area "bug" on or near the 
hatch for annotation purposes. The bug is placed on an "A-ANNO" layer. If no layer 
exists, it will create one. The result is grouped for easy moving.

Parameters:
    Objects: selected Hatches that will generate a summed area tag
    Name: Name to label the bug with. Script will attempt to find the most likely
        name as a default.
    Scale: Scale of the bug. 1 as default. This will greatly depend on the 
        document units and size of your project. You can chang the default below


"""

##### DEFAULT SCALE ######
defaultScale = 1
##########################

import rhinoscriptsyntax as rs
import rhinoscript.userinterface
import rhinoscript.geometry
__commandname__ = "AddAreaText"

def object_names(objs):
    
    counter = {}
    maxItemCount = 0
    for obj in objs:
        
        areaName = rs.ObjectName(obj)
        if not areaName:
            areaName = rs.ObjectLayer(obj).split("-")[-1].replace("_", " ")
        else:
            areaName = areaName.upper()
        try:
            counter[areaName]
            counter[areaName] += 1
        except:
            counter[areaName] = 1
        if counter[areaName] > maxItemCount:
            maxItemCount = counter[areaName]
            mostPopularItem = areaName
    print("Most Popular Item: "+mostPopularItem)
    return(mostPopularItem)

def get_area(objs):
    area = 0
    for obj in objs:
        
        areaObjExp = rs.ExplodeHatch(obj)
        try:
            area += rs.Area(areaObjExp)
        except:
            print("Object not a solid hatch")
            rs.DeleteObject(areaObjExp)
            rs.EnableRedraw(True)
        rs.DeleteObject(areaObjExp)
    return area

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    #rs.EnableRedraw(False)
    cplane = rs.ViewCPlane()
    area = 0
    defaultName = ''
    areaObjs = rs.GetObjects("Select Objects", filter=65536, preselect=True)
    
    if not areaObjs:
        rs.EnableRedraw(True)
        print("No object selected. Exiting command.")
        return
        
    areaName = rs.GetString("Enter name of area to be displayed", object_names(areaObjs), ["RETAIL", "RESIDENTIAL", "AMENITY", "BOH", "LOBBY"])
    
    if not areaName:
        rs.EnableRedraw(True)
        return
    
    # GRAPHIC SCALE OPTIONS
    nameOffset = .4 
    nameTextSize = 1
    areaTextSize = .8
    
    scale = rs.GetReal("Text height (in Rhino Units)", defaultScale)
    if not scale:
        print("Text height not entered, exiting command")
        rs.EnableRedraw(True)
        return

    nameOffset = nameOffset*scale
    nameTextSize = nameTextSize*scale
    areaTextSize = areaTextSize*scale

        
    # GET AREA and Format it to Integer with commas
    area = get_area(areaObjs)
    area = area*(rs.UnitScale(9))**2
    area = int(area)
    area = "{:,} SF".format(area)
    bbox = rs.BoundingBox(areaObjs, cplane)
    pt_sum = bbox[0]
    for i in xrange(1, len(bbox)):
        pt_sum += bbox[i]
    area_avg = rs.AddPoint(pt_sum/len(bbox))

    areaCenter = rs.PointCoordinates(rs.MoveObject(area_avg, cplane.YAxis*(nameOffset+areaTextSize)/-2))
    nameCenter = rs.PointCoordinates(rs.MoveObject(area_avg, cplane.YAxis*(nameOffset+nameTextSize)))
    #    print(nameCenter, areaCenter)
    
    # CREATE THE TEXT
    areaText = rs.AddText(area, areaCenter, areaTextSize, justification=2)
    nameText = rs.AddText(areaName, nameCenter, nameTextSize, justification=2)
    
    # CREATE BOX AROUND TEXT
    
    textBounds = rs.BoundingBox(areaText, cplane)
    textBoundary = rs.AddPolyline(textBounds[0:5])

    nameTextHeight = rs.Distance(rs.BoundingBox(nameText, cplane)[2],rs.BoundingBox(nameText, cplane)[1])
    textBorder = rs.OffsetCurve(textBoundary, (0,0,0), .25*scale,style=1)

    rs.DeleteObject(textBoundary)

    rs.ObjectName(nameText, "Name Text")
    rs.ObjectName(areaText, "Area Text")
    rs.ObjectName(textBorder, "Text Border")
    
    
    parent = rs.ParentLayer(rs.ObjectLayer(areaObjs[0]))+'::' if rs.ParentLayer(rs.ObjectLayer(areaObjs[0])) else ''
    # print("LAYER NAME", rs.LayerName(parent+"A-ANNO-NOTE"))
    
    if not rs.IsLayer(parent+"A-ANNO-NOTE"):
        rs.AddLayer(parent+"A-ANNO-NOTE")
    rs.ObjectLayer(nameText, parent+"A-ANNO-NOTE")
    rs.ObjectLayer(areaText, parent+"A-ANNO-NOTE")
    rs.ObjectLayer(textBorder, parent+"A-ANNO-NOTE")


    areasGroup = rs.AddGroup()
    rs.AddObjectsToGroup([areaText, nameText, textBorder], areasGroup)

    rs.SelectObjects(rs.ObjectsByGroup(areasGroup))
    rs.DeleteObject(area_avg)

    rs.EnableRedraw(True)
    
    
RunCommand(True)