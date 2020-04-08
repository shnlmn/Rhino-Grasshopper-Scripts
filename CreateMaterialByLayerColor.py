import rhinoscriptsyntax as rs
import scriptcontext
import System

def setLayerMat(layer, color):
    index = scriptcontext.doc.Materials.Add()
    mat = scriptcontext.doc.Materials[index]
    mat.DiffuseColor = color
    mat.Name = layer
    print((mat.MaterialIndex))
    exist_mat = rs.LayerMaterialIndex(layer)
    if exist_mat == -1:
        
        mat.CommitChanges()
        rs.LayerMaterialIndex(layer, mat.MaterialIndex)
    
for layer in rs.LayerNames():
    print(rs.LayerColor(layer))
    setLayerMat(layer, rs.LayerColor(layer))