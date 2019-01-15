import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

### Get objects to cut with, place in dictionary with information about object ###
opobj = rs.GetObjects(message="Select objects to remove from.", filter=16)
op_dict = {}
for obj in opobj:  
    op_dict[str(obj)] = {"Layer": rs.ObjectLayer(obj), "Object": obj, "isCut": False}
    

### Get objects to cut with and offset, offset objects, then place them in array ###
diffobjs = rs.GetObjects(message="Select objects to cut with.", filter=16)
diffobjsarray = [rs.coercebrep(sc.doc.Objects.Find(x).Geometry) for x in diffobjs]
offset = rs.GetReal(message="Offset Distance", number = 0.4) # default offset value
cutBreps = []

for o in diffobjsarray:
    out_brep, out_blends, out_walls = Rhino.Geometry.Brep.CreateOffsetBrep(o, offset, False, True, .001) #CreateOffsetBrep returns a list, for some reason
    offsetobjs = sc.doc.Objects.AddBrep(out_brep[0]) # add the brep to the document
    cutBreps.append(offsetobjs) # Add the brep to a list of cutters

for object in op_dict.keys():
    for cutter in cutBreps:
#        print(op_dict[object]["Object"], cutter)
        resultBrep = rs.BooleanDifference(op_dict[object]['Object'], cutter, False)
#        print("result brep ",resultBrep)
        if resultBrep:
            rs.DeleteObject(op_dict[object]['Object'])
            op_dict[object]["Object"] = resultBrep[0]
            rs.ObjectLayer(op_dict[object]["Object"], layer=op_dict[object]["Layer"])
#            rs.DeleteObject(resultBrep)
#            print("Deleted", resultBrep)

    
for cutBrep in cutBreps:
    rs.DeleteObject(cutBrep)
rs.Redraw()