import rhinoscriptsyntax as rs
import random

def FindCentroidOfPoints(ids):
    
    if not ids: return
    
    # first point
    pt_sum = rs.PointCoordinates(rs.CreatePoint(ids[0]))
    
    # sum rest of points
    for i in xrange(1, len(ids)):
        pt_sum += rs.PointCoordinates(ids[i])
    
    # divide with amount of points to get average
    pt_sum = pt_sum / len(ids)
    
    return pt_sum


widgets = rs.GetObjects()
rotate = rs.GetBoolean("Rotate items?", ("Rotate", "No", "Yes"), (True))
bounds = rs.BoundingBox(widgets)
print(bounds)
x_dist = rs.Distance(bounds[0], bounds[1])
y_dist = rs.Distance(bounds[1], bounds[2])
z_dist = rs.Distance(bounds[3], bounds[4])
for ind,w in enumerate(widgets):
#    print(rotate)
#    if rotate:
#        print("ROTATE")
#        centerPt = FindCentroidOfPoints(bounds)
#        print(centerPt)
#        rs.RotateObject(w, centerPt, random.uniform(0,360))
#    
    x = random.uniform(0, x_dist)
    y = random.uniform(0, y_dist)
    z = random.uniform(0, z_dist)    
    randVec = rs.VectorCreate((0,0,0), (x,y,z))
    rs.MoveObject(w, randVec)
   

print(x_dist, y_dist, z_dist)