import rhinoscriptsyntax as rs

origPt = rs.GetPoint(message="Select Origin Point for View")
camLoc = (3582,1528,500)
targetLoc = (3582,1528,0)
newLoc = [ co + camLoc[i] for i, co in enumerate(origPt)]
newTarget = [ co + targetLoc[i] for i, co in enumerate(origPt)]
print(newLoc, newTarget)
#rs.ViewCamera(camera_location=newLoc)
rs.ViewCameraTarget(camera = newLoc, target = newTarget)
