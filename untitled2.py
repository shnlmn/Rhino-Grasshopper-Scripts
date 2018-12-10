import rhinoscriptsyntax as rs


sourceObjects = rs.GetObjects(message="Select Surfaces to Extrude", filter=8, preselect=True, select=False)
height = rs.GetReal(message="Input Extrusion Height", number=10)
guide = rs.AddLine((0,0,0), (0,0,height))
for obj in sourceObjects:
    objlayer = rs.ObjectLayer(obj)
    extruded = rs.ExtrudeSurface(obj,guide)
    rs.ObjectLayer(extruded, layer=objlayer)
    
rs.DeleteObject(guide)