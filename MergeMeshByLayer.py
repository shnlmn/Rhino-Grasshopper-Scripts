import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

for l in rs.LayerNames():
    rs.CurrentLayer(l)
    print(l)
    meshes = rs.ObjectsByLayer(l)
    print(meshes)
    meshes = rs.JoinMeshes(meshes, True)
    rs.SplitDisjointMesh(meshes, True)