import rhinoscriptsyntax as rs

theObjs = rs.SelectedObjects()

if len(theObjs) == 0:
    
    theObjs = rs.GetObject("Select objects to move")

target = rs.GetObject("Select object on destination layer")

if target:
#    options = ("Move", "No", "Yes")
    makeCurrent = rs.MessageBox("Make "+rs.ObjectLayer(target)+" layer the current active layer?", 3)
    targetLayer = rs.ObjectLayer(target)
    rs.ObjectLayer(theObjs, targetLayer)
    if makeCurrent == 6:
        rs.CurrentLayer(targetLayer)
