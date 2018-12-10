import rhinoscriptsyntax as rs

rs.EnableRedraw(enable = False)
groups = rs.GroupNames()
selected = rs.SelectedObjects()
if groups:
    for i, group in enumerate(groups):
        objs = rs.ObjectsByGroup(group)
        if objs:
            objName = group+str(i)
            block = rs.AddBlock(objs, (0,0,0), objName, True)
            rs.InsertBlock(block, (0,0,0))

selected = rs.SelectedObjects()

for i in range(len(selected)):
    obj = [selected[i]]
    objName = str(rs.ObjectLayer(obj[0]))+str(i)
    block = rs.AddBlock(obj, (0,0,0), objName, True)
    rs.InsertBlock(block, (0,0,0))


rs.EnableRedraw(enable = True)