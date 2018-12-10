import rhinoscriptsyntax as rs

sourceObject = rs.GetObject(message="Select Object to use color", preselect=True, select=False)
sourceColor = rs.ObjectColor(sourceObject)
rs.LayerColor(rs.CurrentLayer(), color=sourceColor)