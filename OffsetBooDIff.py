import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
opobj = rs.GetObjects(message="Select objects to remove from.", filter=16)

diffobj = rs.GetObject(message="Select objects to cut with.", filter=16)
diffobj_r = sc.doc.Objects.Find(diffobj).Geometry
offset = rs.GetReal(message="Offset Distance", number = 0.4)
# print(rs.OffsetSurface(diffobj, offset, create_solid=True))
diffobj_r = rs.coercebrep(diffobj_r)

out_brep, out_blends, out_walls = Rhino.Geometry.Brep.CreateOffsetBrep(diffobj_r, offset, False, True, .001)

for x in out_brep:
    cutBrep = sc.doc.Objects.AddBrep(x)
    print(cutBrep)
#sc.doc.Objects.AddBrep(diffobj_off[0][1])
if len(opobj) > 1:
    for obj in opobj:
        print(obj)
        rs.BooleanDifference(obj, cutBrep, False)
        rs.DeleteObject(obj)
else:
    rs.BooleanDifference(opobj, cutBrep, False)
    rs.DeleteObject(opobj)
         
rs.DeleteObject(cutBrep)
rs.Redraw()