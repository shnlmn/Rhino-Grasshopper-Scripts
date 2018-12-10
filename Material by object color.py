import rhinoscriptsyntax as rs

sourceObjects = rs.GetObjects(message="Select Objects to use color", preselect=True, select=False)

for obj in sourceObjects:
    obj_color = rs.ObjectColor(obj)
    obj_mat = rs.ObjectMaterialIndex(obj)
    if obj_mat == -1:
        obj_mat = rs.AddMaterialToObject(obj)
    rs.MaterialColor(obj_mat, obj_color)
    rs.ObjectPrintColor(obj, color=rs.ObjectColor(obj))