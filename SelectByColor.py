import rhinoscriptsyntax as rs

sourceObject = rs.GetObject(message="Select object", preselect=True, select=False)

objColor = rs.ObjectColor(sourceObject)

visObjects = rs.AllObjects()
selObjects = []

rs.EnableRedraw(enable=False)

for obj in visObjects:
    if rs.ObjectColor(obj) == objColor:
        selObjects.append(obj)

rs.SelectObjects(selObjects)

rs.EnableRedraw(enable=True)