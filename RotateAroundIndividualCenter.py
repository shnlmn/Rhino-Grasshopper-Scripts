import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc


### Objects to rotate about their center ###
opobj = rs.GetObjects(message="Select objects to rotate.")

for obj in opobj:
    bounds = rs.BoundingBox(obj)
    ptAdd = bounds[0]
    for p in bounds[1:4]:
        ptAdd = rs.PointAdd(ptAdd, p)
    
    center = rs.PointDivide(ptAdd, 4)
   
    rs.RotateObject(obj, center, 180)