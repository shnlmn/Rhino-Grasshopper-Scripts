import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

opobj = rs.GetObjects(message="Select objects to remove from.", filter=16, preselect=True)
diffobj = rs.GetObjects(message="Select objects to cut with.", filter=16, preselect=True)

if len(diffobj) > 1:
    cutBrep = []
    for o in diffobj:
        cutBrep.append(rs.coercebrep(sc.doc.Objects.Find(o).Geometry))
else:
    cutObj = sc.doc.Objects.Find(diffobj).Geometry
    cutBrep = rs.coercebrep(cutObj)


offset = rs.GetReal(message="Offset Distance", number = 0.25)



def offsetBrep(obj2):
    out_brep, out_blends, out_walls = Rhino.Geometry.Brep.CreateOffsetBrep(obj2, offset, False, True, .001)
    for x in out_brep:
        return(sc.doc.Objects.AddBrep(x))

def makeCut(obj1, obj2):
    cutter = offsetBrep(obj2)
    rs.BooleanDifference(obj1, cutter, False)
    rs.DeleteObject(obj)
    rs.DeleteObject(cutter)

if len(opobj) > 1:
    for obj in opobj:
        if len(cutBrep) > 1:
            for cutobj in cutBrep:
                makeCut(obj, cutobj)
        else:
            makeCut(obj, cutBrep)
else:
    if len(cutBrep) > 1:
        for cutobj in cutBrep:
            makeCut(opobj, cutobj)
    else:
        makeCut(opobj, cutBrep)
        
rs.Redraw()