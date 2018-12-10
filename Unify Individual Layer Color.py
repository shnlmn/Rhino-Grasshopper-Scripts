import rhinoscriptsyntax as rs

layers = rs.CurrentLayer()

def unifyColor(layer):
    layer_c = rs.LayerColor(layer)
    layer_m = rs.LayerMaterialIndex(layer)
    if layer_m == -1:
        layer_m = rs.AddMaterialToLayer(layer)
    rs.MaterialColor(layer_m, layer_c)
    rs.LayerPrintColor(layer, layer_c)
    
if __name__ == "__main__":
    
    if rs.LayerChildCount(layers) > 0:
        sublayers = rs.LayerChildren(layers)
        for i in sublayers:
            print(i)
            unifyColor(i)
    else:
        unifyColor(layers)