import rhinoscriptsyntax as rs
import random
text = rs.GetString(message="Enter elevation")+"'"
basePoint = rs.GetPoint(message="Select location for elevation bug.")
radius = rs.GetReal(message="Enter bug radius", number=1, minimum= 0.1)
textSize = rs.GetString(message="Text Size", defaultString="2")
directions = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0]]
basePoint = rs.AddPoint(basePoint)
bug = []
groupName = "elevBug_"+str(random.randint(1,100000))
rs.AddGroup(group_name=groupName)
rs.EnableRedraw(enable=False)
rs.AddCircle(basePoint, radius)
lineLen=radius*1.5
for i in range(4):
    endPt = rs.CopyObject(basePoint, rs.VectorScale(directions[i], lineLen))
    bug.append(rs.AddLine(basePoint, endPt))
    rs.DeleteObject(endPt)
    
    

textPt = rs.CopyObject(basePoint, rs.VectorScale([radius/2,radius/2,0], lineLen*1.2))
elevText = rs.AddText(text, textPt, height=float(textSize))
angle = rs.VectorAngle(rs.ViewCPlane().XAxis, [1,0,0])
rs.RotateObject(bug, basePoint, -angle)
rs.DeleteObject(basePoint)
rs.DeleteObject(textPt)
rs.AddObjectsToGroup(bug,groupName)
rs.AddObjectsToGroup(elevText,groupName)

activeLayer = rs.CurrentLayer()
rs.ObjectLayer(bug, activeLayer+"::A-ANNO-NOTE")
rs.ObjectLayer(elevText, activeLayer+"::A-ANNO-NOTE")

#rs.AddLine(basePoint, rs.MoveObject(basePoint, [0,0,lineLen]))