import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc


def ScaleEach():
    factor=2
    objrefs = []
    if sc.sticky.has_key("SCALEFACTOR"):
        factor = sc.sticky["SCALEFACTOR"]
    while True:
        go = Rhino.Input.Custom.GetObject()
        go.AcceptNumber(True, False)
        optFactor = Rhino.Input.Custom.OptionDouble(factor)
        go.AddOptionDouble("Scale",optFactor)
        
        get_rc = go.GetMultiple(1, 0)


        if go.CommandResult()!=Rhino.Commands.Result.Success:

            return go.CommandResult()
            
        if get_rc==Rhino.Input.GetResult.Object:
            for n in range(go.ObjectCount):
                objrefs.append(go.Object(n))
            break
            
        elif get_rc == Rhino.Input.GetResult.Number:
            factor = go.Number()
            sc.sticky["SCALEFACTOR"] = factor
            
        elif get_rc==Rhino.Input.GetResult.Option:
            factor = optFactor.CurrentValue
            sc.sticky["SCALEFACTOR"] = factor
            continue
            
    factor = sc.sticky["SCALEFACTOR"]
    if len(objrefs) == 0: return
    
    rs.EnableRedraw(False)
    for objref in objrefs:
        Id = objref.ObjectId
        obj = sc.doc.Objects.Find(Id)
        bbCen = obj.Geometry.GetBoundingBox(True).Center
        rs.ScaleObject(Id,bbCen,[factor, factor, factor],False)
    rs.EnableRedraw(True)

ScaleEach()