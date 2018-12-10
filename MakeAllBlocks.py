import rhinoscriptsyntax as rs

theObjs = rs.SelectedObjects()

rs.EnableRedraw(enable = False)

for i in range(len(theObjs)):
    obj = [theObjs[i]]
    objName = str(rs.ObjectLayer(obj[0]))+str(i)
    block = rs.AddBlock(obj, (0,0,0), objName, True)
    rs.InsertBlock(block, (0,0,0))

rs.EnableRedraw(enable=True)